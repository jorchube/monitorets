from gi.repository import Adw, Gtk

from ..preference_switch import PreferenceSwitch
from ...preferences import Preferences
from ...preference_keys import PreferenceKeys
from ...theme import Theme
from ...layout import Layout
from .temperature_units_toggle_widget import TemperatureUnitsToggleWidget
from .redraw_frequency_toggle_widget import RedrawFrequencyToggleWidget


@Gtk.Template(
    resource_path="/org/github/jorchube/monitorets/gtk/preferences-page-appearance.ui"
)
class PreferencesPageAppearance(Adw.PreferencesPage):
    __gtype_name__ = "PreferencesPageAppearance"

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
    _grid_layout_action_row = Gtk.Template.Child()

    _smooth_graphs_action_row = Gtk.Template.Child()
    _show_current_value_action_row = Gtk.Template.Child()
    _temperature_units_action_row = Gtk.Template.Child()
    _redraw_frequency_action_row = Gtk.Template.Child()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._vertical_check_button = Gtk.CheckButton()
        self._horizontal_check_button = Gtk.CheckButton()
        self._grid_check_button = Gtk.CheckButton()
        self._init_toggles()

        theme = Preferences.get(PreferenceKeys.THEME)
        self._set_active_toggle_for_theme(theme)

        layout = Preferences.get(PreferenceKeys.LAYOUT)
        self._set_active_toggle_for_layout(layout)

        self._system_theme_toggle_button.connect(
            "clicked", self._on_system_theme_button_clicked
        )
        self._light_theme_toggle_button.connect(
            "clicked", self._on_light_theme_button_clicked
        )
        self._dark_theme_toggle_button.connect(
            "clicked", self._on_dark_theme_button_clicked
        )

        self._vertical_check_button.connect(
            "toggled", self._on_vertical_check_button_toggled
        )
        self._horizontal_check_button.connect(
            "toggled", self._on_horizontal_check_button_toggled
        )
        self._grid_check_button.connect("toggled", self._on_grid_check_button_toggled)

    def _init_toggles(self):
        self._system_theme_toggle_button_image_big.set_from_resource(
            "/org/github/jorchube/monitorets/gtk/icons/system.png"
        )
        self._system_theme_toggle_button_image_small.set_from_resource(
            "/org/github/jorchube/monitorets/gtk/icons/system.png"
        )

        self._light_theme_toggle_button_image_big.set_from_resource(
            "/org/github/jorchube/monitorets/gtk/icons/light.png"
        )
        self._light_theme_toggle_button_image_small.set_from_resource(
            "/org/github/jorchube/monitorets/gtk/icons/light.png"
        )

        self._dark_theme_toggle_button_image_big.set_from_resource(
            "/org/github/jorchube/monitorets/gtk/icons/dark.png"
        )
        self._dark_theme_toggle_button_image_small.set_from_resource(
            "/org/github/jorchube/monitorets/gtk/icons/dark.png"
        )

        self._vertical_layout_action_row.add_prefix(self._vertical_check_button)
        self._vertical_layout_action_row.set_activatable_widget(
            self._vertical_check_button
        )

        self._horizontal_check_button.set_group(self._vertical_check_button)
        self._horizontal_layout_action_row.add_prefix(self._horizontal_check_button)
        self._horizontal_layout_action_row.set_activatable_widget(
            self._horizontal_check_button
        )

        self._grid_check_button.set_group(self._vertical_check_button)
        self._grid_layout_action_row.add_prefix(self._grid_check_button)
        self._grid_layout_action_row.set_activatable_widget(self._grid_check_button)

        smooth_graph_switch = PreferenceSwitch(PreferenceKeys.SMOOTH_GRAPH)
        self._smooth_graphs_action_row.add_suffix(smooth_graph_switch)
        self._smooth_graphs_action_row.set_activatable_widget(smooth_graph_switch)

        show_current_value_switch = PreferenceSwitch(PreferenceKeys.SHOW_CURRENT_VALUE)
        self._show_current_value_action_row.add_suffix(show_current_value_switch)
        self._show_current_value_action_row.set_activatable_widget(
            show_current_value_switch
        )

        self._temperature_units_action_row.add_suffix(TemperatureUnitsToggleWidget())

        self._redraw_frequency_action_row.add_suffix(RedrawFrequencyToggleWidget())

    def _on_system_theme_button_clicked(self, user_data):
        Preferences.set(PreferenceKeys.THEME, Theme.SYSTEM)

    def _on_light_theme_button_clicked(self, user_data):
        Preferences.set(PreferenceKeys.THEME, Theme.LIGHT)

    def _on_dark_theme_button_clicked(self, user_data):
        Preferences.set(PreferenceKeys.THEME, Theme.DARK)

    def _set_active_toggle_for_theme(self, theme):
        theme_to_toggle_button_map = {
            Theme.SYSTEM: self._system_theme_toggle_button,
            Theme.LIGHT: self._light_theme_toggle_button,
            Theme.DARK: self._dark_theme_toggle_button,
        }
        theme_to_toggle_button_map[theme].set_active(True)

    def _set_active_toggle_for_layout(self, layout):
        layout_to_toggle_button_map = {
            Layout.HORIZONTAL: self._horizontal_check_button,
            Layout.VERTICAL: self._vertical_check_button,
            Layout.GRID: self._grid_check_button,
        }
        layout_to_toggle_button_map[layout].set_active(True)

    def _on_vertical_check_button_toggled(self, toggle_button):
        if toggle_button.get_active():
            Preferences.set(PreferenceKeys.LAYOUT, Layout.VERTICAL)

    def _on_horizontal_check_button_toggled(self, toggle_button):
        if toggle_button.get_active():
            Preferences.set(PreferenceKeys.LAYOUT, Layout.HORIZONTAL)

    def _on_grid_check_button_toggled(self, toggle_button):
        if toggle_button.get_active():
            Preferences.set(PreferenceKeys.LAYOUT, Layout.GRID)
