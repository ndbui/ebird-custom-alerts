from context import ebird_api_lib
from context import configs
import os
def init_test_env():
    paths = {
        "secrets": os.path.abspath(os.path.join(os.path.dirname(__file__), "../secrets.json")),
        "alert-configs": "alert-configs.json"
    }
    config_manager = configs.ConfigManager(paths=paths)
    ebird_api = ebird_api_lib.EbirdApiWrapper(config_manager.get_ebird_apikey())
    return ebird_api

def test_get_bird_taxonomy():
    """Test that you're able to call the ebird API using your key and get bird taxonomy"""
    ebird_api = init_test_env()
    resp = ebird_api.get_bird_taxonomy("easkin")
    assert resp.status_code == 200

def test_get_checklist():
    """Test that you're able to call the ebird API using your key and get a checklist"""
    ebird_api = init_test_env()
    resp = ebird_api.get_checklist("S29893687")
    assert resp.status_code == 200

def test_get_recent_checklists():
    """Test that you're able to call the ebird API using your key and get recent checklists"""
    ebird_api = init_test_env()
    resp = ebird_api.get_recent_checklists("US", 2)
    assert resp.status_code == 200

if __name__ == "__main__":
    test_get_bird_taxonomy()
    test_get_checklist()
    test_get_recent_checklists()