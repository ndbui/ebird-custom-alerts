import json
import sys
import os

"""Class to access various config values used in the project including secrets"""
class ConfigManager():
    def __init__(self, paths={"secrets": "secrets.json", "alert-configs": "alert-configs.json"}):
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
        self.paths = paths
        self.load_secrets()
        self.load_alert_configs()
    
    """Load secrets from the secrets.json file into the manager"""
    def load_secrets(self):
        with open(self.paths["secrets"], "r") as f:
            self.secrets = json.load(f)

    """Load hotspot and alert configs per user from the alert-configs.json into the manager"""
    def load_alert_configs(self):
        with open(self.paths["alert-configs"], "r") as f:
            self.alert_configs = json.load(f)

    """
    Return the username and password of a user
    
    Parameters:
        user (string): user name that you want to get credentials for

    Returns:
        string: password belonging to the specified user in the params
    """
    def get_user_credentials(self, user):
        if user not in self.secrets["ebird"]["user_credentials"]:
            raise Exception(f"Following user does not exist in the manager: {user}")
        else:
            return self.secrets["ebird"]["user_credentials"][user]

