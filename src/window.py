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
from .sampler import Sampler
from .graph_area import GraphArea

@Gtk.Template(resource_path='/org/github/jorchube/gpumonitor/gtk/main-window.ui')
class MonitorWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    _overlay = Gtk.Template.Child()

    def __init__(self, title, sampler_file, **kwargs):
        super().__init__(**kwargs)

        self._drawing_area = Gtk.DrawingArea()
        self._drawing_area.set_hexpand(True)
        self._drawing_area.set_vexpand(True)

        self._overlay.set_child(self._drawing_area)

        self._set_title(title)

        self.connect("close-request", self._close_request)

        self._graph_area = GraphArea(self._drawing_area)
        self._sampler = Sampler(sampler_file, self._graph_area.add_value)
        self._sampler.start()

    def _set_title(self, title):
        label = Gtk.Label()
        label.set_markup(f"<span weight='bold'>{title}</span>")

        headerbar = Adw.HeaderBar()
        headerbar.set_title_widget(label)
        headerbar.add_css_class("flat")

        self._overlay.add_overlay(headerbar)


    def _close_request(self, user_data):
        self._sampler.stop()
