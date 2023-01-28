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

from .headerbar_wrapper import HeaderBarWrapper
from .window_layout_manager import WindowLayoutManager
from ..preferences import Preferences
from ..preference_keys import PreferenceKeys
from ..window_geometry import WindowGeometry


@Gtk.Template(resource_path="/org/github/jorchube/monitorets/gtk/single-window.ui")
class SingleWindow(Adw.ApplicationWindow):
    __gtype_name__ = "SingleWindow"

    _overlay = Gtk.Template.Child()
    _monitors_container_bin = Gtk.Template.Child()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        window_geometry = Preferences.get(PreferenceKeys.WINDOW_GEOMETRY)
        self.set_default_size(window_geometry.width, window_geometry.height)

        self._headerbar_wrapper = HeaderBarWrapper(parent_window=self)
        self._overlay.add_overlay(self._headerbar_wrapper.root_widget)
        self._monitors_container_bin.set_child(
            WindowLayoutManager.get_container_widget()
        )

        self.connect("close-request", self._close_request)
        self._install_motion_event_controller()

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
        for monitor in self._enabled_monitors.values():
            if monitor is not None:
                monitor.stop()

    def _persist_window_geometry(self):
        window_geometry = WindowGeometry(
            width=self.get_width(), height=self.get_height()
        )
        Preferences.set(PreferenceKeys.WINDOW_GEOMETRY, window_geometry)
