from context import configs
import sys

"""Initialize the config manager using the config files found in the test dir"""
def init_manager():
    paths = {
        "secrets": "tests/secrets.json",
        "alert-configs": "tests/alert-configs.json"
    }
    return configs.ConfigManager(paths=paths)

"""Test that the config manager loads the alert configs properly"""
def test_configs_alert_configs():
    config_manager = init_manager()
    assert config_manager.alert_configs != {}
    assert config_manager.alert_configs["testu"]["hotspots"][0] == "Test Hotspot"
    assert config_manager.secrets != {}
    assert config_manager.secrets["ebird"]["user_credentials"]["testu"] == "testp"
    assert config_manager.secrets["ebird"]["apikey"] == "test-apikey"

"""Test that getting the user credentials is working properly"""
def test_configs_get_user_credentials():
    config_manager = init_manager()
    password = config_manager.get_user_credentials("testu")
    assert password == "testp"

if __name__ == "__main__":
    test_configs_alert_configs()
    test_configs_get_user_credentials()