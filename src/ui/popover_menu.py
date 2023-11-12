from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(resource_path="/io/github/jorchube/monitorets/gtk/popover-menu.ui")
class PopoverMenu(Gtk.Popover):
    __gtype_name__ = "PopoverMenu"

    _preferences_button = Gtk.Template.Child()
