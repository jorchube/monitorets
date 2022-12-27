from gi.repository import Adw, Gtk

from ..theme_toggle_manager import ThemeToggleManager
from ..layout_toggle_manager import LayoutToggleManager


@Gtk.Template(resource_path='/org/github/jorchube/monitorets/gtk/preferences-page-appearance.ui')
class PreferencesPageAppearance(Adw.PreferencesPage):
    __gtype_name__ = 'PreferencesPageAppearance'

    _system_theme_toggle_button = Gtk.Template.Child()
    _light_theme_toggle_button = Gtk.Template.Child()
    _dark_theme_toggle_button = Gtk.Template.Child()

    _system_theme_toggle_button_image_big = Gtk.Template.Child()
    _system_theme_toggle_button_image_small = Gtk.Template.Child()
    _light_theme_toggle_button_image_big = Gtk.Template.Child()
    _light_theme_toggle_button_image_small = Gtk.Template.Child()
    _dark_theme_toggle_button_image_big = Gtk.Template.Child()
    _dark_theme_toggle_button_image_small = Gtk.Template.Child()

    _system_theme_toggle_image_squeezer = Gtk.Template.Child()

    _horizontal_layout_action_row = Gtk.Template.Child()
    _vertical_layout_action_row = Gtk.Template.Child()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._vertical_check_button = Gtk.CheckButton()
        self._horizontal_check_button = Gtk.CheckButton()
        self._init_toggles()

        self._theme_toggle_manager = ThemeToggleManager(self)
        self._layout_toggle_manager = LayoutToggleManager(self)

    def _init_toggles(self):
        self._system_theme_toggle_button_image_big.set_from_resource("/org/github/jorchube/monitorets/gtk/icons/system.png")
        self._system_theme_toggle_button_image_small.set_from_resource("/org/github/jorchube/monitorets/gtk/icons/system.png")

        self._light_theme_toggle_button_image_big.set_from_resource("/org/github/jorchube/monitorets/gtk/icons/light.png")
        self._light_theme_toggle_button_image_small.set_from_resource("/org/github/jorchube/monitorets/gtk/icons/light.png")

        self._dark_theme_toggle_button_image_big.set_from_resource("/org/github/jorchube/monitorets/gtk/icons/dark.png")
        self._dark_theme_toggle_button_image_small.set_from_resource("/org/github/jorchube/monitorets/gtk/icons/dark.png")

        self._vertical_layout_action_row.add_prefix(self._vertical_check_button)
        self._vertical_layout_action_row.set_activatable_widget(self._vertical_check_button)

        self._horizontal_check_button.set_group(self._vertical_check_button)
        self._horizontal_layout_action_row.add_prefix(self._horizontal_check_button)
        self._horizontal_layout_action_row.set_activatable_widget(self._horizontal_check_button)
