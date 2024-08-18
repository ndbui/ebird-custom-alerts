import pytest
import os
from typing import Dict
import configs.manager as configs


@pytest.fixture()
def valid_config_paths() -> Dict[str, str]:
    return {
        "secrets": os.path.join(os.path.dirname(__file__), "secrets", "valid_secrets.json"),
        "alert-configs": os.path.join(os.path.dirname(__file__), "alert-configs.json"),
    }


@pytest.fixture()
def invalid_config_paths() -> Dict[str, str]:
    return {
        "secrets": os.path.join(os.path.dirname(__file__), "secrets", "invalid_secrets.json"),
        "alert-configs": os.path.join(os.path.dirname(__file__), "alert-configs.json"),
    }


@pytest.fixture(scope="function")
def valid_config_manager(valid_config_paths) -> configs.ConfigManager:
    return configs.ConfigManager(paths=valid_config_paths)


def test_configs_alert_configs(valid_config_manager):
    """Test that the config manager loads the alert configs properly"""
    assert valid_config_manager.alert_configs != {}
    assert valid_config_manager.alert_configs["testu"]["hotspots"][0] == "Test Hotspot"
    assert valid_config_manager.secrets != {}
    assert valid_config_manager.secrets["ebird"]["user_credentials"]["testu"] == "testp"
    assert valid_config_manager.secrets["ebird"]["apikey"] == "test-apikey"


def test_configs_get_user_credentials(valid_config_manager):
    """Test that getting the user credentials is working properly"""
    password = valid_config_manager.get_user_credentials("testu")
    assert password == "testp"


def test_configs_invalid_secrets(invalid_config_paths):
    """Testing that the config manager throws an error when it can't find ebird as a key at the root level"""
    with pytest.raises(Exception):
        configs.ConfigManager(paths=invalid_config_paths)


if __name__ == "__main__":
    test_configs_alert_configs()
    test_configs_get_user_credentials()
