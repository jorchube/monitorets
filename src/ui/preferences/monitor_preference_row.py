from gi.repository import Adw, Gtk
from .rename_monitor_popover import RenameMonitorPopover
from ..preference_switch import PreferenceSwitch
from ...preferences import Preferences
from ...translatable_strings import preference_toggle_description


class MonitorPreferenceRow(Adw.ActionRow):
    def __init__(self, monitor_type, title, preference_key, subtitle=None, is_label_customizable=False):
        super().__init__()

        self._monitor_type = monitor_type

        self.set_title(title)

        self._custom_name_label = self._create_custom_name_label()
        self.add_suffix(self._custom_name_label)

        self._rename_popover = RenameMonitorPopover(self._on_rename)

        self._edit_button = self._create_edit_button()
        self.add_suffix(self._edit_button)

        switch = PreferenceSwitch(preference_key)
        self.add_suffix(switch)
        self.set_activatable_widget(switch)

        custom_name = Preferences.get_custom_name(self._monitor_type)
        if custom_name:
            self._set_custom_name(custom_name, persist=False)

        if subtitle is not None:
            self.set_subtitle(subtitle)

        self._install_motion_event_controller()



    def _on_rename(self, new_name):
        if new_name:
            self._set_custom_name(new_name)
        else:
            self._reset_name()

    def _create_custom_name_label(self):
        label = Gtk.Label()
        label.add_css_class("dim-label")
        label.add_css_class("caption-heading")
        label.set_valign(Gtk.Align.CENTER)
        label.set_xalign(0)

        return label

    def _set_custom_name(self, custom_name, persist=True):
        self._custom_name = custom_name
        self._custom_name_label.set_size_request(120, -1)
        self._custom_name_label.set_markup(f"<span weight=\"normal\" style=\"oblique\">{preference_toggle_description.SHOWN_AS}:\n</span><span>{custom_name}</span>")

        self._rename_popover.set_text(custom_name)

        if persist is True:
            Preferences.set_custom_name(self._monitor_type, custom_name)

    def _reset_name(self):
        self._custom_name = None
        self._custom_name_label.set_size_request(-1, -1)
        self._custom_name_label.set_label("")
        Preferences.set_custom_name(self._monitor_type, None)

    def _create_edit_button(self):
        edit_button = Gtk.MenuButton()
        edit_button.set_icon_name("document-edit-symbolic")
        edit_button.add_css_class("flat")
        edit_button.set_valign(Gtk.Align.CENTER)
        edit_button.set_opacity(0)
        edit_button.set_popover(self._rename_popover)
        return edit_button

    def _install_motion_event_controller(self):
        controller = Gtk.EventControllerMotion()
        controller.connect("enter", self._on_mouse_enter)
        controller.connect("leave", self._on_mouse_leave)
        self.add_controller(controller)

    def _on_mouse_enter(self, motion_controller, x, y):
        self._edit_button.set_opacity(1)

    def _on_mouse_leave(self, motion_controller):
        self._edit_button.set_opacity(0)
