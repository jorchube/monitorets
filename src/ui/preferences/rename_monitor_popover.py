from gi.repository import Adw, Gtk


@Gtk.Template(
    resource_path="/io/github/jorchube/monitorets/gtk/rename-monitor-popover.ui"
)
class RenameMonitorPopover(Gtk.Popover):
    __gtype_name__ = "RenameMonitorPopover"

    _text_entry = Gtk.Template.Child()
    _rename_button = Gtk.Template.Child()

    def __init__(self, rename_callback):
        super().__init__()
        self._rename_button.connect("clicked", self._on_rename_clicked)
        self._text_entry.connect("activate", self._on_enter_pressed_on_text_entry)
        self._rename_callback = rename_callback
        self._current_name = None

    def set_text(self, text):
        if text:
            self._text_entry.get_buffer().set_text(text, len(text))

    def _on_rename_clicked(self, user_data):
        self._apply_rename()

    def _on_enter_pressed_on_text_entry(self, user_data):
        self._apply_rename()

    def _apply_rename(self):
        text = self._text_entry.get_buffer().get_text().strip()
        self._rename_callback(text)
        self.popdown()
