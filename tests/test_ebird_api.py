from context import ebird_api_lib
from context import configs
import os
import pytest


@pytest.fixture()
def ebird_api() -> ebird_api_lib.EbirdApiWrapper:
    paths = {
        "secrets": os.path.abspath(os.path.join(os.path.dirname(__file__), "../secrets.json")),
        "alert-configs": "alert-configs.json",
    }
    config_manager = configs.ConfigManager(paths=paths)
    ebird_api = ebird_api_lib.EbirdApiWrapper(config_manager.get_ebird_apikey())
    return ebird_api


@pytest.mark.skip(reason="Integration test meant to be used with a valid apikey")
def test_get_bird_taxonomy(ebird_api):
    """Test that you're able to call the ebird API using your key and get bird taxonomy"""
    resp = ebird_api.get_bird_taxonomy("easkin")
    assert resp.status_code == 200


@pytest.mark.skip(reason="Integration test meant to be used with a valid apikey")
def test_get_checklist(ebird_api):
    """Test that you're able to call the ebird API using your key and get a checklist"""
    resp = ebird_api.get_checklist("S29893687")
    assert resp.status_code == 200


@pytest.mark.skip(reason="Integration test meant to be used with a valid apikey")
def test_get_recent_checklists(ebird_api):
    """Test that you're able to call the ebird API using your key and get recent checklists"""
    resp = ebird_api.get_recent_checklists("US", 2)
    assert resp.status_code == 200
