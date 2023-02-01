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

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gio, Adw
from .controller import Controller
from .ui.preferences.preferences_window import PreferencesWindow
from .ui.single_window import SingleWindow
from .ui.tips_window import TipsWindow
from . import discover_temperature_monitors
from .translators import translators_credits
from . import events
from .event_broker import EventBroker


class MonitorApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(
            application_id="io.github.jorchube.monitorets",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
        )

        self.window = None

        self.create_action("quit", self.on_quit, ["<primary>q"])
        self.create_action("about", self.on_about_action)
        self.create_action("tips", self.on_tips_action)
        self.create_action(
            "preferences", self.on_preferences_action, ["<primary>comma"]
        )

        self._discover_dynamic_monitors()

        Controller.initialize(application=self)

        EventBroker.subscribe(events.CLOSE_APPLICATION_REQUESTED, self.on_quit)

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """

        self.window = SingleWindow(application=self)
        self.window.present()
        Controller.show_monitors()

    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(
            transient_for=self.props.active_window,
            application_name="Monitorets",
            application_icon="io.github.jorchube.monitorets",
            developer_name="Jordi Chulia",
            version="0.8.0",
            developers=["Jordi Chulia"],
            copyright="© 2022 Jordi Chulia",
            translator_credits=translators_credits.strip(),
        )
        about.present()

    def on_tips_action(self, widget, _):
        tips_window = TipsWindow(transient_for=self.props.active_window)
        tips_window.present()

    def on_quit(self, *args, **kwargs):
        Controller.stop_all_monitors()
        for window in self.get_windows():
            window.close()
        self.quit()

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        print("app.preferences action activated")
        preferences_window = PreferencesWindow(transient_for=self.props.active_window)
        preferences_window.present()

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

    def _discover_dynamic_monitors(self):
        discover_temperature_monitors.execute()


def main(version):
    """The application's entry point."""
    app = MonitorApplication()
    return app.run(sys.argv)
