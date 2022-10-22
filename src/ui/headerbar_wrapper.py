from gi.repository import Adw, Gtk


class HeaderBarWrapper:
    def __init__(self, preferences_box):
        self._preferences_box = preferences_box
        self._settings_button = self._build_settings_button()
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
        headerbar.set_vexpand(False)
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
        popover.set_child(self._preferences_box)
        button.set_popover(popover)
        return button
