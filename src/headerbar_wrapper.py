from gi.repository import Adw, Gtk


class HeaderBarWrapper():
    def __init__(self, title):
        self._label = self._build_title_label(title)
        self._settings_button = self._build_settings_button()
        self._headerbar = self._build_headerbar()

        self.set_invisible()

    @property
    def headerbar(self):
        return self._headerbar

    def set_visible(self):
        self._settings_button.set_visible(True)

    def set_invisible(self):
        self._settings_button.set_visible(False)

    def _build_headerbar(self):
        headerbar = Adw.HeaderBar()
        headerbar.add_css_class("flat")
        headerbar.set_title_widget(self._label)
        headerbar.pack_start(self._settings_button)
        return headerbar

    def _build_settings_button(self):
        button = Gtk.Button()
        button.set_icon_name("document-properties-symbolic")
        button.add_css_class("circular")
        button.add_css_class("flat")
        button.set_vexpand(False)
        button.set_valign(Gtk.Align.CENTER)
        return button

    def _build_title_label(self, title):
        label = Gtk.Label()
        label.set_markup(f"<span weight='bold'>{title}</span>")
        return label
