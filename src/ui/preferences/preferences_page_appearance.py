from gi.repository import Adw, Gtk

from ..theme_toggle_manager import ThemeToggleManager
from ..layout_toggle_manager import LayoutToggleManager


@Gtk.Template(resource_path='/org/github/jorchube/monitorets/gtk/preferences-page-appearance.ui')
class PreferencesPageAppearance(Adw.PreferencesPage):
    __gtype_name__ = 'PreferencesPageAppearance'

    _system_theme_toggle_button = Gtk.Template.Child()
    _light_theme_toggle_button = Gtk.Template.Child()
    _dark_theme_toggle_button = Gtk.Template.Child()

    _adaptive_layout_toggle_button = Gtk.Template.Child()
    _horizontal_layout_toggle_button = Gtk.Template.Child()
    _vertical_layout_toggle_button = Gtk.Template.Child()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._theme_toggle_manager = ThemeToggleManager(self)
        self._layout_toggle_manager = LayoutToggleManager(self)
