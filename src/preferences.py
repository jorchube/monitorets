import json
import os
from xdg import xdg_config_home

from .event_broker import EventBroker
from . import events


class Preferences:
    _folder_name = "io.github.jorchube.monitorets"
    _file_name = "preferences.json"

    _default_preferences = {
        "general.theme": "system",
        "cpu_monitor.enabled": True,
        "cpu_monitor.sampling_frequency_seconds": 0.1,
        "gpu_monitor.enabled": False,
        "gpu_monitor.sampling_frequency_seconds": 0.1,
        "memory_monitor.enabled": True,
        "memory_monitor.sampling_frequency_seconds": 0.1,
    }

    _preferences = {}

    @classmethod
    @property
    def CPU_monitor(self):
        return self._cpu_monitor_preferences

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
