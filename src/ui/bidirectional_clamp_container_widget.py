from gi.repository import Adw, Gtk


class BidirectionalClampContainerWidget(Adw.Bin):
    _MAX_HORIZONTAL_SIZE = 500
    _HORIZONTAL_TIGHTENING_THRESHOLD = 250
    _MAX_VERTICAL_SIZE = 200
    _VERTICAL_TIGHTENING_THRESHOLD = 100

    def __init__(self):
        super().__init__()

        self._h_clamp = Adw.Clamp()
        self._h_clamp.set_orientation(Gtk.Orientation.HORIZONTAL)
        self._h_clamp.set_maximum_size(self._MAX_HORIZONTAL_SIZE)
        self._h_clamp.set_tightening_threshold(self._HORIZONTAL_TIGHTENING_THRESHOLD)

        self._v_clamp = Adw.Clamp()
        self._v_clamp.set_orientation(Gtk.Orientation.VERTICAL)
        self._v_clamp.set_maximum_size(self._MAX_VERTICAL_SIZE)
        self._v_clamp.set_tightening_threshold(self._VERTICAL_TIGHTENING_THRESHOLD)

        super().set_child(self._h_clamp)
        self._h_clamp.set_child(self._v_clamp)

    def set_child(self, widget):
        self._v_clamp.set_child(widget)

    def get_child(self):
        return self._v_clamp.get_child()
