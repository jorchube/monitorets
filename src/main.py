# main.py
#
# Copyright 2022 Jordi Chulia
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw, GLib, GObject
from . import events
from .event_broker import EventBroker
from .monitor_windows.cpu_monitor_window import CPUMonitorWindow
from .monitor_windows.gpu_monitor_window import GPUMonitorWindow
from .monitor_windows.memory_monitor_window import MemoryMonitorWindow
from .monitor_type import MonitorType
from .ui.preferences import MonitorEnableSwitch


class MonitorApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id='org.github.jorchube.gpumonitor',flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.create_action('quit', self.on_quit, ['<primary>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)

        EventBroker.subscribe(events.MONITOR_ENABLED_CHANGED, self._on_monitor_enabled_changed)

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        self._present_monitor_windows(MonitorType.CPU)
        self._present_monitor_windows(MonitorType.GPU)
        self._present_monitor_windows(MonitorType.Memory)

    def _on_monitor_enabled_changed(self, monitor_type, enabled):
        if enabled:
            GObject.idle_add(self._present_monitor_windows, monitor_type)

        if not enabled:
            GObject.idle_add(self._close_monitor_windows, monitor_type)

    def _present_monitor_windows(self, monitor_type):
        if monitor_type == MonitorType.CPU:
            CPUMonitorWindow(application=self).present()
        if monitor_type == MonitorType.GPU:
            GPUMonitorWindow(application=self).present()
        if monitor_type == MonitorType.Memory:
            MemoryMonitorWindow(application=self).present()

    def _close_monitor_windows(self, type):
        for monitor_window in self.get_windows():
            if monitor_window.monitor_type == type:
                monitor_window.close()

    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(transient_for=self.props.active_window,
                                application_name='gpumonitor',
                                application_icon='org.github.jorchube.gpumonitor',
                                developer_name='Jordi Chulia',
                                version='0.1.0',
                                developers=['Jordi Chulia'],
                                copyright='© 2022 Jordi Chulia')
        about.present()

    def on_quit(self, *args, **kwargs):
        for window in self.get_windows():
            window.close()

        self.quit()

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        print('app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)

def main(version):
    """The application's entry point."""

    # GObject.type_register(MonitorEnableSwitch)
    # GObject.signal_new('mierdas', MonitorEnableSwitch, GObject.SIGNAL_RUN_FIRST, GObject.TYPE_NONE, ())

    EventBroker.initialize()
    app = MonitorApplication()
    return app.run(sys.argv)
