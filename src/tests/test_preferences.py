from unittest import mock
import pytest

from ..preferences import Preferences
from ..event_broker import EventBroker
from .. import events
from time import sleep


class TestPreferences:
    @pytest.fixture
    def settings_content(self):
        return '''{
            "cpu_monitor.enabled": true,
            "gpu_monitor.enabled": false,
            "memory_monitor.enabled": true
        }
        '''

    @pytest.fixture(autouse=True)
    def default_preferences(self):
        Preferences._default_preferences = {
            "cpu_monitor.enabled": True,
            "gpu_monitor.enabled": True,
            "memory_monitor.enabled": True,
        }

    @pytest.fixture
    def mock_file_exists(self):
        with mock.patch('src.preferences.Preferences._file_exists') as mock_exists:
            mock_exists.return_value = True
            yield mock_exists

    @pytest.fixture
    def mock_read_file(self, settings_content):
        with mock.patch('src.preferences.Preferences._read_file') as mock_read:
            mock_read.return_value = settings_content
            yield mock_read

    @pytest.fixture
    def mock_write_file(self):
        with mock.patch('src.preferences.Preferences._write_file') as mock_write:
            yield mock_write

    @pytest.mark.usefixtures("mock_file_exists", "mock_read_file")
    def test_it_loads_preferences_from_file_when_requested_to_load_them(self):
        Preferences.load()

        assert Preferences.get("cpu_monitor.enabled") is True
        assert Preferences.get("gpu_monitor.enabled") is False
        assert Preferences.get("memory_monitor.enabled") is True

    @pytest.mark.usefixtures("mock_read_file")
    def test_it_writes_default_preferences_when_requested_to_load_them_and_do_not_exist(self, mock_write_file):
        Preferences.load()

        mock_write_file.assert_called_once_with(
            mock.ANY,
            '{"cpu_monitor.enabled": true, "gpu_monitor.enabled": true, "memory_monitor.enabled": true}'
        )

    @pytest.mark.usefixtures("mock_read_file", "mock_file_exists", "mock_write_file")
    def test_it_changes_preference_when_a_preference_has_changed(self):
        Preferences.load()

        Preferences.set("memory_monitor.enabled", False)

        assert Preferences.get("memory_monitor.enabled") is False

    @pytest.mark.usefixtures("mock_read_file", "mock_file_exists")
    def test_it_persists_preferences_when_a_preference_has_changed(self, mock_write_file):
        Preferences.load()

        Preferences.set("memory_monitor.enabled", False)

        mock_write_file.assert_called_once_with(
            mock.ANY,
            '{"cpu_monitor.enabled": true, "gpu_monitor.enabled": false, "memory_monitor.enabled": false}'
        )

    @pytest.mark.usefixtures("mock_file_exists", "mock_read_file", "mock_write_file")
    def test_it_notifies_preferences_changed_when_a_preference_has_changed(self):
        mock_subscription = mock.MagicMock()
        EventBroker.initialize()
        EventBroker.subscribe(events.PREFERENCES_CHANGED, mock_subscription)
        Preferences.load()

        Preferences.set("memory_monitor.enabled", False)

        retries = 5
        while mock_subscription.call_count == 0 and retries > 0:
            sleep(0.1)
            retries = retries - 1

        mock_subscription.assert_called_once()

    @pytest.mark.usefixtures("mock_file_exists", "mock_read_file", "mock_write_file")
    def test_it_adds_new_fields_when_default_preferences_has_more_fields_than_persisted_preferences(self):
        Preferences._default_preferences["new.key"] = "new value"

        Preferences.load()

        assert Preferences.get("new.key") == "new value"
        assert Preferences.get("cpu_monitor.enabled") is True
        assert Preferences.get("gpu_monitor.enabled") is False
        assert Preferences.get("memory_monitor.enabled") is True
