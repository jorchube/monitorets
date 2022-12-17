from gi.repository import Adw, Gtk

from .preferences.preferences_window import PreferencesWindow
from ..event_broker import EventBroker
from .. import events
from ..translatable_strings import headerbar as headerbar_strings

class HeaderBarWrapper:
    def __init__(self, parent_window):
        self._parent_window = parent_window
        self._preferences_button = self._build_preferences_button()
        self._headerbar = self._build_headerbar(self._preferences_button)

        self._set_not_focused()

        EventBroker.subscribe(events.ABOUT_DIALOG_TRIGGERED, self._dismiss_preferences_popover)
        EventBroker.subscribe(events.TIPS_DIALOG_TRIGGERED, self._dismiss_preferences_popover)

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
        drag_icon = Gtk.Image.new_from_icon_name("list-drag-handle-symbolic")
        drag_icon.set_tooltip_text(headerbar_strings.DRAG_TOOLTIP)

        headerbar = Adw.HeaderBar()
        headerbar.set_vexpand(False)
        headerbar.set_valign(Gtk.Align.START)
        headerbar.set_title_widget(drag_icon)
        headerbar.set_decoration_layout(":close")
        headerbar.pack_start(preferences_button)

        return headerbar

    def _build_preferences_button(self):
        button = Gtk.Button()
        button.set_icon_name("document-properties-symbolic")
        button.add_css_class("circular")
        button.add_css_class("flat")
        button.set_vexpand(False)
        button.set_valign(Gtk.Align.CENTER)
        button.set_tooltip_text(headerbar_strings.PREFERENCES_TOOLTIP)

        button.connect("clicked", self._present_preferences_window)

        return button

    def _present_preferences_window(self, data):
        preferences_window = PreferencesWindow(transient_for=self._parent_window)
        preferences_window.present()

    def _dismiss_preferences_popover(self, *args, **kwargs):
        self._preferences_popover.popdown()
