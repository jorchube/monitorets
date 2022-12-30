import json
import os
from xdg import xdg_config_home

from .event_broker import EventBroker
from . import events
from .preference_keys import PreferenceKeys
from .theme import Theme
from .layout import Layout


class Preferences:
    _folder_name = "io.github.jorchube.monitorets"
    _file_name = "preferences.json"

    _default_preferences = {
        PreferenceKeys.THEME: Theme.SYSTEM,
        PreferenceKeys.LAYOUT: Layout.VERTICAL,
        PreferenceKeys.CPU_MONITOR_ENABLED: True,
        PreferenceKeys.CPU_PER_CORE_MONITOR_ENABLED: False,
        PreferenceKeys.GPU_MONITOR_ENABLED: False,
        PreferenceKeys.MEMORY_MONITOR_ENABLED: True,
        PreferenceKeys.SWAP_MONITOR_ENABLED: False,
        PreferenceKeys.DOWNLINK_MONITOR_ENABLED: False,
        PreferenceKeys.UPLINK_MONITOR_ENABLED: False,
        PreferenceKeys.HOME_USAGE_MONITOR_ENABLED: False,
        PreferenceKeys.ROOT_USAGE_MONITOR_ENABLED: False,
        "gpu_monitor.sampling_frequency_seconds": 0.1,
        "cpu_monitor.sampling_frequency_seconds": 0.1,
        "memory_monitor.sampling_frequency_seconds": 0.1,
    }

    _preferences = {}

    @classmethod
    def get(self, preference_path):
        return self._preferences[preference_path]

    @classmethod
    def set(self, preference_path, value):
        self._preferences[preference_path] = value
        self._persist_preferences()
        EventBroker.notify(events.PREFERENCES_CHANGED, preference_path, value)

    @classmethod
    def _persist_preferences(self):
        file_path = self._build_file_path()
        self._write_preferences(self._preferences, file_path)

    @classmethod
    def load(self):
        file_path = self._build_file_path()
        if not self._file_exists(file_path):
            self._write_preferences(self._default_preferences, file_path)

        self._preferences = self._default_preferences | self._read_preferences(file_path)

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
