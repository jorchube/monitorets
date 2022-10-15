from gi.repository import Adw, Gtk

from .preferences import PreferencesBox

class HeaderBarWrapper:
    def __init__(self, title):
        self._title_label = self._build_title_label(title)
        self._settings_button = self._build_settings_button()
        self._headerbar = self._build_headerbar()

        self.title_overlay = Gtk.Overlay()
        self.title_overlay.set_child(self._title_label)
        self.title_overlay.add_overlay(self._headerbar)

        self._title_label.set_opacity(0.5)

        self.on_mouse_exit()

    @property
    def root_widget(self):
        return self.title_overlay

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
        headerbar.add_css_class("flat")
        headerbar.set_title_widget(Gtk.Label(label=""))
        headerbar.pack_start(self._settings_button)
        return headerbar

    def _build_settings_button(self):
        button = Gtk.MenuButton()
        button.set_icon_name("document-properties-symbolic")
        button.add_css_class("circular")
        button.add_css_class("flat")
        button.set_vexpand(False)
        button.set_valign(Gtk.Align.CENTER)

        popover = Gtk.Popover()
        popover.set_child(PreferencesBox())
        button.set_popover(popover)
        return button

    def _build_title_label(self, title):
        label = Gtk.Label(label="")
        label.set_markup(f"<span weight='bold'>{title}</span>")
        return label
