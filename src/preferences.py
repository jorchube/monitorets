import json
import os
from xdg import xdg_config_home

from .event_broker import EventBroker
from . import events
from .preference_keys import PreferenceKeys
from .theme import Theme
from .layout import Layout
from .window_geometry import WindowGeometry


class Preferences:
    _folder_name = "io.github.jorchube.monitorets"
    _file_name = "preferences.json"

    _default_preferences = {
        PreferenceKeys.THEME: Theme.SYSTEM,
        PreferenceKeys.LAYOUT: Layout.VERTICAL,
        PreferenceKeys.SMOOTH_GRAPH: True,
        PreferenceKeys.SHOW_CURRENT_VALUE: False,
        PreferenceKeys.WINDOW_GEOMETRY: WindowGeometry(width=180, height=40).as_dict(),
        PreferenceKeys.CPU_MONITOR_ENABLED: True,
        PreferenceKeys.CPU_PER_CORE_MONITOR_ENABLED: False,
        PreferenceKeys.GPU_MONITOR_ENABLED: False,
        PreferenceKeys.MEMORY_MONITOR_ENABLED: True,
        PreferenceKeys.SWAP_MONITOR_ENABLED: False,
        PreferenceKeys.DOWNLINK_MONITOR_ENABLED: False,
        PreferenceKeys.UPLINK_MONITOR_ENABLED: False,
        PreferenceKeys.HOME_USAGE_MONITOR_ENABLED: False,
        PreferenceKeys.ROOT_USAGE_MONITOR_ENABLED: False,
        PreferenceKeys.UNIFIED_SCALE_FOR_NETWORK_MONITORS_ENABLED: False,
        "gpu_monitor.sampling_frequency_seconds": 0.1,
        "cpu_monitor.sampling_frequency_seconds": 0.1,
        "memory_monitor.sampling_frequency_seconds": 0.1,
        "custom_name": {},
    }

    _preferences = dict()
    _custom_key_handler = dict()

    @classmethod
    def initialize(self):
        self._custom_key_handler[PreferenceKeys.WINDOW_GEOMETRY] = {
            "set": self._set_window_geometry,
            "get": self._get_window_geometry,
        }

    @classmethod
    def get(self, preference_path):
        if preference_path in self._custom_key_handler:
            return self._custom_key_handler[preference_path]["get"]()

        return self._default_get_handler(preference_path)

    @classmethod
    def set(self, preference_path, value):
        if preference_path in self._custom_key_handler:
            self._custom_key_handler[preference_path]["set"](value)
            return

        self._default_set_handler(preference_path, value)

    @classmethod
    def _default_set_handler(self, preference_path, value):
        self._preferences[preference_path] = value
        self._persist_preferences()
        EventBroker.notify(events.PREFERENCES_CHANGED, preference_path, value)

    @classmethod
    def _default_get_handler(self, preference_path):
        return self._preferences[preference_path]

    @classmethod
    def get_custom_name(self, monitor_type):
        return self._preferences["custom_name"].get(monitor_type)

    @classmethod
    def set_custom_name(self, monitor_type, name):
        self._preferences["custom_name"][monitor_type] = name
        self._persist_preferences()
        EventBroker.notify(events.MONITOR_RENAMED, monitor_type, name)

    @classmethod
    def _persist_preferences(self):
        file_path = self._build_file_path()
        self._write_preferences(self._preferences, file_path)

    @classmethod
    def load(self):
        file_path = self._build_file_path()
        if not self._file_exists(file_path):
            self._write_preferences(self._default_preferences, file_path)

        self._preferences = self._default_preferences | self._read_preferences(
            file_path
        )

        self._migrate_deprecated_adaptive_layout_value()

    @classmethod
    def _read_preferences(self, file_path):
        json_content = self._read_file(file_path)
        return json.loads(json_content)

    @classmethod
    def _write_preferences(self, preferences, file_path):
        json_default_preferences = json.dumps(preferences)
        self._write_file(file_path, json_default_preferences)

    @classmethod
    def _file_exists(self, file_path):
        return file_path.exists()

    @classmethod
    def _read_file(self, file_path):
        return file_path.read_text()

    @classmethod
    def _write_file(self, file_path, content):
        os.makedirs(file_path.parent, exist_ok=True)
        file_path.write_text(content)

    @classmethod
    def _build_file_path(self):
        base = xdg_config_home()
        full_path = base / self._folder_name / self._file_name
        return full_path

    @classmethod
    def register_preference_key_default(self, key, default_value):
        self._default_preferences[key] = default_value

    @classmethod
    def _migrate_deprecated_adaptive_layout_value(self):
        if Preferences.get(PreferenceKeys.LAYOUT) == "adaptive":
            Preferences.set(PreferenceKeys.LAYOUT, Layout.VERTICAL)

    @classmethod
    def _set_window_geometry(self, window_geometry):
        self._default_set_handler(
            PreferenceKeys.WINDOW_GEOMETRY, window_geometry.as_dict()
        )

    @classmethod
    def _get_window_geometry(self):
        window_geometry_dict = self._default_get_handler(PreferenceKeys.WINDOW_GEOMETRY)
        return WindowGeometry.from_dict(window_geometry_dict)
