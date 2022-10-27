from gi.repository import Adw, Gtk

from ..event_broker import EventBroker
from .. import events


class HeaderBarWrapper:
    def __init__(self, preferences_box):
        self._preferences_popover = Gtk.Popover()
        self._preferences_box = preferences_box
        self._preferences_button = self._build_preferences_button(self._preferences_box, self._preferences_popover)
        self._headerbar = self._build_headerbar(self._preferences_button)

        self._set_not_focused()

        EventBroker.subscribe(events.ABOUT_DIALOG_TRIGGERED, self._dismiss_preferences_popover)

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

    def _build_headerbar(self, preferences_button):
        headerbar = Adw.HeaderBar()
        headerbar.set_vexpand(False)
        headerbar.add_css_class("flat")
        headerbar.set_title_widget(Gtk.Label(label=""))
        headerbar.pack_start(preferences_button)

        return headerbar

    def _build_preferences_button(self, preferences_box, popover):
        button = Gtk.MenuButton()
        button.set_icon_name("document-properties-symbolic")
        button.add_css_class("circular")
        button.add_css_class("flat")
        button.set_vexpand(False)
        button.set_valign(Gtk.Align.CENTER)

        popover.set_child(preferences_box)
        button.set_popover(popover)

        return button

    def _dismiss_preferences_popover(self, *args, **kwargs):
        self._preferences_popover.popdown()
