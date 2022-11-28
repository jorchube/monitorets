from gi.repository import Adw
from gi.repository import Gtk

from ..translatable_strings import tips


@Gtk.Template(resource_path='/org/github/jorchube/monitorets/gtk/tips-window.ui')
class TipsWindow(Adw.Window):
    __gtype_name__ = 'TipsWindow'

    _headerbar = Gtk.Template.Child()
    _tips_box = Gtk.Template.Child()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        title_label = Gtk.Label()
        title_label.set_markup(f"<span weight=\"bold\">{tips.WINDOW_TITLE}</span>")
        self._headerbar.set_title_widget(title_label)

        tip = self._new_tip_content(
            tips.ALWAYS_ON_TOP_TITLE,
            tips.ALWAYS_ON_TOP_BODY
        )

        self._tips_box.append(tip)

        self.set_default_size(400, 20)

    def _new_tip_content(self, title, description):
        title_label = self._build_title_label(title)
        description_label = self._build_description_label(description)

        box = Gtk.Box()
        box.set_halign(Gtk.Align.START)
        box.add_css_class("card")
        box.set_orientation(Gtk.Orientation.VERTICAL)
        box.append(title_label)
        box.append(description_label)

        return box

    def _build_title_label(self, title):
        label = Gtk.Label(label=title)
        label.set_margin_top(10)
        label.set_margin_bottom(5)
        label.set_margin_start(20)
        label.set_margin_end(20)
        label.add_css_class("heading")

        return label

    def _build_description_label(self, description):
        label = Gtk.Label()
        label.set_markup(description)
        label.set_margin_top(5)
        label.set_margin_bottom(20)
        label.set_margin_start(20)
        label.set_margin_end(20)
        label.set_wrap(True)

        return label
