# window.py
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

from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import GObject

import traceback
from .headerbar_wrapper import HeaderBarWrapper
from .window_layout_manager import WindowLayoutManager
from ..event_broker import EventBroker
from .. import events
from ..monitor_descriptors import monitor_descriptor_list
from ..preferences import Preferences
from ..preference_keys import PreferenceKeys
from ..window_geometry import WindowGeometry


@Gtk.Template(resource_path="/org/github/jorchube/monitorets/gtk/single-window.ui")
class SingleWindow(Adw.ApplicationWindow):
    __gtype_name__ = "SingleWindow"

    _overlay = Gtk.Template.Child()
    _monitors_box = Gtk.Template.Child()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._available_monitors = self._build_available_monitors_dict()
        self._monitor_bins = self._build_monitor_bins_dict()

        self._layout_managet = WindowLayoutManager(
            self, self._set_horizontal_layout, self._set_vertical_layout
        )

        window_geometry = Preferences.get(PreferenceKeys.WINDOW_GEOMETRY)
        self.set_default_size(window_geometry.width, window_geometry.height)

        EventBroker.subscribe(events.MONITOR_ENABLED, self._handle_on_monitor_enabled)
        EventBroker.subscribe(events.MONITOR_DISABLED, self._handle_on_monitor_disabled)

        self._headerbar_wrapper = HeaderBarWrapper(parent_window=self)
        self._overlay.add_overlay(self._headerbar_wrapper.root_widget)
        self._add_monitor_bins_to_monitors_box(self._monitor_bins, self._monitors_box)

        self.connect("close-request", self._close_request)
        self._install_motion_event_controller()

    def _build_available_monitors_dict(self):
        monitors_dict = {}
        for descriptor in monitor_descriptor_list:
            monitors_dict[descriptor["type"]] = descriptor["monitor_class"]

        return monitors_dict

    def _build_monitor_bins_dict(self):
        bins_dict = {}
        for descriptor in monitor_descriptor_list:
            bins_dict[descriptor["type"]] = Adw.Bin()

        return bins_dict

    def _add_monitor_bins_to_monitors_box(self, monitor_bins, monitor_box):
        for bin in monitor_bins.values():
            monitor_box.append(bin)

    def _handle_on_monitor_enabled(self, type):
        GObject.idle_add(self._on_monitor_enabled, type)

    def _handle_on_monitor_disabled(self, type):
        GObject.idle_add(self._on_monitor_disabled, type)

    def _on_monitor_enabled(self, type):
        if self._monitor_bins[type].get_child() is not None:
            return

        try:
            self._enable_monitor(type)
        except Exception as e:
            print(f"Exception: {e}")
            traceback.print_exc()

    def _enable_monitor(self, type):
        monitor = self._available_monitors[type]()
        monitor.start()
        self._set_monitor_bin_enabled_style(self._monitor_bins[type])
        self._monitor_bins[type].set_child(monitor)

    def _on_monitor_disabled(self, type):
        if self._monitor_bins[type].get_child() is None:
            return

        monitor = self._monitor_bins[type].get_child()
        self._monitor_bins[type].set_child(None)
        self._set_monitor_bin_disabled_style(self._monitor_bins[type])
        monitor.stop()

    def _set_horizontal_layout(self):
        self._monitors_box.set_orientation(Gtk.Orientation.HORIZONTAL)

    def _set_vertical_layout(self):
        self._monitors_box.set_orientation(Gtk.Orientation.VERTICAL)

    def _install_motion_event_controller(self):
        controller = Gtk.EventControllerMotion()
        controller.connect("enter", self._on_mouse_enter)
        controller.connect("leave", self._on_mouse_leave)
        self._overlay.add_controller(controller)

    def _on_mouse_enter(self, motion_controller, x, y):
        self._headerbar_wrapper.on_mouse_enter()

    def _on_mouse_leave(self, motion_controller):
        self._headerbar_wrapper.on_mouse_exit()

    def _close_request(self, user_data):
        self._persist_window_geometry()

        for monitor_bin in self._monitor_bins.values():
            monitor = monitor_bin.get_child()
            if monitor:
                monitor.stop()

    def _set_monitor_bin_disabled_style(self, monitor_bin):
        monitor_bin.set_margin_top(0)
        monitor_bin.set_margin_bottom(0)
        monitor_bin.set_margin_start(0)
        monitor_bin.set_margin_end(0)

    def _set_monitor_bin_enabled_style(self, monitor_bin):
        monitor_bin.set_margin_top(4)
        monitor_bin.set_margin_bottom(4)
        monitor_bin.set_margin_start(4)
        monitor_bin.set_margin_end(4)

    def _persist_window_geometry(self):
        window_geometry = WindowGeometry(
            width=self.get_width(), height=self.get_height()
        )
        Preferences.set(PreferenceKeys.WINDOW_GEOMETRY, window_geometry)
