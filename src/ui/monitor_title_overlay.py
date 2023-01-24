from gi.repository import Adw, Gtk, Pango, GObject


class MonitorTitleOverlay(Adw.Bin):
    def __init__(self, html_color_code):
        super().__init__()

        self._html_color_code = html_color_code
        self._title_label = self._build_title_label()
        self._value_label = self._build_value_label()

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.set_valign(Gtk.Align.CENTER)
        box.append(Gtk.Label())
        box.append(self._title_label)
        box.append(self._value_label)

        self.set_child(box)

    def set_title(self, title):
        GObject.idle_add(self._title_label.set_markup, f"<span weight='bold' color='#{self._html_color_code}'>{title}</span>")

    def set_value(self, value):
        value_as_str = value if value is not None else ""
        markup = f"<span size='small' weight='bold' color='#{self._html_color_code}'>{value_as_str}</span>"
        GObject.idle_add(self._value_label.set_markup, markup)

    def _build_title_label(self):
        label = Gtk.Label()
        label.set_margin_start(10)
        label.set_margin_end(10)
        label.set_ellipsize(Pango.EllipsizeMode.MIDDLE)

        return label

    def _build_value_label(self):
        label = Gtk.Label()
        return label
