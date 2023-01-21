from gi.repository import Adw, Gtk

from ..event_broker import EventBroker
from .. import events


class HeaderBarWrapper:
    def __init__(self, parent_window):
        self._parent_window = parent_window
        self._headerbar = self._build_headerbar()

        self._set_not_focused()

    @property
    def root_widget(self):
        return self._headerbar

    def on_mouse_enter(self):
        self._set_focused()

    def on_mouse_exit(self):
        self._set_not_focused()

    def _set_not_focused(self):
        self._headerbar.set_opacity(0)

    def _set_focused(self):
        self._headerbar.set_opacity(1)

    def _build_headerbar(self):
        headerbar = Adw.HeaderBar()
        headerbar.set_vexpand(True)
        headerbar.add_css_class("flat")
        headerbar.set_title_widget(Gtk.Label())
        headerbar.set_decoration_layout(":")

        close_button = self._build_close_button()
        menu_button = self._build_menu_button()

        headerbar.pack_start(self._build_headerbar_button_box(menu_button))
        headerbar.pack_end(self._build_headerbar_button_box(close_button))

        return headerbar

    def _build_headerbar_button_box(self, button):
        control_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        control_box.set_valign(Gtk.Align.START)
        control_box.append(button)

        return control_box

    def _close_button_clicked(self, *args, **kwargs):
        EventBroker.notify(events.CLOSE_APPLICATION_REQUESTED)

    def _build_close_button(self):
        button = Gtk.Button()
        button.set_icon_name("window-close")
        button.add_css_class("circular")
        button.add_css_class("raised")
        button.connect("clicked", self._close_button_clicked)

        return button

    def _build_menu_button(self):
        button = Gtk.MenuButton()
        button.set_icon_name("open-menu-symbolic")
        button.add_css_class("circular")
        button.add_css_class("raised")

        builder = Gtk.Builder.new_from_resource(
            "/org/github/jorchube/monitorets/gtk/main-menu-model.ui"
        )
        menu = builder.get_object("main_menu")

        popover = Gtk.PopoverMenu.new_from_model(menu)

        button.set_popover(popover)

        return button
