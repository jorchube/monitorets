from gi.repository import Gtk


class WindowLayoutManager:
    _SENSIBILITY = 1.5

    def __init__(self, window, set_horizontal_layout_callback, set_vertical_layout_callback):
        self._window = window
        self._set_horizontal_layout = set_horizontal_layout_callback
        self._set_vertical_layout = set_vertical_layout_callback

        self._paintable = Gtk.WidgetPaintable()
        self._paintable.set_widget(self._window)

        self._paintable.connect("invalidate-size", self._size_changed)

    def _size_changed(self, *args, **kwargs):
        new_width = self._window.get_width()
        new_height = self._window.get_height()

        if (new_width / new_height) > self._SENSIBILITY:
            self._set_horizontal_layout()

        if (new_height / new_width) > self._SENSIBILITY:
            self._set_vertical_layout()
