from context import configs
import pytest

def test_configs_alert_configs():
    """Test that the config manager loads the alert configs properly"""
    paths = {
        "secrets": "secrets/valid_secrets.json",
        "alert-configs": "alert-configs.json"
    }
    config_manager = configs.ConfigManager(paths=paths)
    assert config_manager.alert_configs != {}
    assert config_manager.alert_configs["testu"]["hotspots"][0] == "Test Hotspot"
    assert config_manager.secrets != {}
    assert config_manager.secrets["ebird"]["user_credentials"]["testu"] == "testp"
    assert config_manager.secrets["ebird"]["apikey"] == "test-apikey"

def test_configs_get_user_credentials():
    """Test that getting the user credentials is working properly"""
    paths = {
        "secrets": "secrets/valid_secrets.json",
        "alert-configs": "alert-configs.json"
    }
    config_manager = configs.ConfigManager(paths=paths)
    password = config_manager.get_user_credentials("testu")
    assert password == "testp"

def test_configs_invalid_secrets():
    """Testing that the config manager throws an error when it can't find ebird as a key at the root level"""
    paths = {
        "secrets": "secrets/invalid_secrets.json",
        "alert-configs": "alert-configs.json"
    }
    with pytest.raises(Exception):
        config_manager = configs.ConfigManager(paths=paths)

if __name__ == "__main__":
    test_configs_alert_configs()
    test_configs_get_user_credentials()