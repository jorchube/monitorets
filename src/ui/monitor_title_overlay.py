from gi.repository import Adw, Gtk, Pango, GObject


class MonitorTitleOverlay(Adw.Bin):
    _SMALL_VIEW_SIZE_LIMIT = 100
    _BIG_VIEW_SIZE_LIMIT = 200

    def __init__(self, html_color_code):
        super().__init__()

        self._html_color_code = html_color_code

        self._huge_view = _HugeMonitorTitleOverlayView(self._html_color_code)
        self._big_view = _BigMonitorTitleOverlayView(self._html_color_code)
        self._small_view = _SmallMonitorTitleOverlayView(self._html_color_code)

        self._squeezer = Adw.Squeezer()
        self._squeezer.set_transition_duration(500)
        self._squeezer.set_transition_type(Adw.SqueezerTransitionType.CROSSFADE)
        self._squeezer_page_big = self._squeezer.add(self._big_view)
        self._squeezer_page_small = self._squeezer.add(self._small_view)
        self._squeezer_page_huge = self._squeezer.add(self._huge_view)

        self.set_child(self._squeezer)

        self._paintable = Gtk.WidgetPaintable()
        self._paintable.set_widget(self)
        self._paintable.connect("invalidate-size", self._on_size_changed)

        self._refresh_visible_view()


    def set_title(self, title):
        self._huge_view.set_title(title)
        self._big_view.set_title(title)
        self._small_view.set_title(title)

    def set_value(self, value):
        self._huge_view.set_value(value)
        self._big_view.set_value(value)
        self._small_view.set_value(value)

    def _on_size_changed(self, paintable):
        self._refresh_visible_view()

    def _refresh_visible_view(self):
        width = self.get_width()
        height = self.get_height()

        if height < self._SMALL_VIEW_SIZE_LIMIT or width < self._SMALL_VIEW_SIZE_LIMIT:
            self._squeezer_page_huge.set_enabled(False)
            self._squeezer_page_big.set_enabled(False)
            self._squeezer_page_small.set_enabled(True)
            return

        if height < self._BIG_VIEW_SIZE_LIMIT or width < self._BIG_VIEW_SIZE_LIMIT:
            self._squeezer_page_huge.set_enabled(False)
            self._squeezer_page_small.set_enabled(False)
            self._squeezer_page_big.set_enabled(True)
            return

        self._squeezer_page_small.set_enabled(False)
        self._squeezer_page_big.set_enabled(False)
        self._squeezer_page_huge.set_enabled(True)


class _MonitorTitleOverlayView(Gtk.Box):
    def __init__(self, html_color_code):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)

        self._html_color_code = html_color_code
        self._title_label = self._build_title_label()
        self._value_label = self._build_value_label()

        self.set_valign(Gtk.Align.CENTER)
        self.append(self._title_label)
        self.append(self._value_label)

    def _build_title_label(self):
        label = Gtk.Label()
        label.set_margin_start(10)
        label.set_margin_end(10)
        label.set_ellipsize(Pango.EllipsizeMode.MIDDLE)

        return label

    def _build_value_label(self):
        label = Gtk.Label()
        return label

    def set_title(self, title):
        markup = f"<span weight='{self._title_weight()}' size='{self._title_size()}' color='#{self._html_color_code}'>{title}</span>"
        GObject.idle_add(self._title_label.set_markup, markup)

    def set_value(self, value):
        value_as_str = value if value is not None else ""
        markup = f"<span weight='{self._value_weight()}' size='{self._value_size()}' color='#{self._html_color_code}'>{value_as_str}</span>"
        GObject.idle_add(self._value_label.set_markup, markup)

    def _title_size(self):
        raise NotImplementedError

    def _title_weight(self):
        raise NotImplementedError

    def _value_size(self):
        raise NotImplementedError

    def _value_weight(self):
        raise NotImplementedError


class _SmallMonitorTitleOverlayView(_MonitorTitleOverlayView):
    def _title_size(self):
        return "medium"

    def _title_weight(self):
        return "bold"

    def _value_size(self):
        return "small"

    def _value_weight(self):
        return "bold"


class _BigMonitorTitleOverlayView(_MonitorTitleOverlayView):
    def _title_size(self):
        return "large"

    def _title_weight(self):
        return "bold"

    def _value_size(self):
        return "medium"

    def _value_weight(self):
        return "bold"


class _HugeMonitorTitleOverlayView(_MonitorTitleOverlayView):
    def _title_size(self):
        return "xx-large"

    def _title_weight(self):
        return "ultrabold"

    def _value_size(self):
        return "large"

    def _value_weight(self):
        return "bold"
