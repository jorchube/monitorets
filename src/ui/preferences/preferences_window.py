from gi.repository import Adw, Gtk

from .preferences_page_appearance import PreferencesPageAppearance
from .preferences_page_monitors import PreferencesPageMonitors


@Gtk.Template(resource_path="/org/github/jorchube/monitorets/gtk/preferences-window.ui")
class PreferencesWindow(Adw.PreferencesWindow):
    __gtype_name__ = "PreferencesWindow"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_modal(True)

        self.add(PreferencesPageAppearance())
        self.add(PreferencesPageMonitors())
