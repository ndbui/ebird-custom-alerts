import json
import sys
import os

class ConfigManager():
    """Class to access various config values used in the project including secrets"""

    def __init__(self, paths={"secrets": "secrets.json", "alert-configs": "alert-configs.json"}):
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
        self.paths = paths
        self.load_secrets()
        self.load_alert_configs()
        if 'ebird' not in self.secrets:
            raise Exception(f"Cannot find ebird key in {paths['secrets']}")
    

    def load_secrets(self):
        """Load secrets from the valid_secrets.json file into the manager"""
        with open(self.paths["secrets"], "r") as f:
            self.secrets = json.load(f)


    def load_alert_configs(self):
        """Load hotspot and alert configs per user from the alert-configs.json into the manager"""
        with open(self.paths["alert-configs"], "r") as f:
            self.alert_configs = json.load(f)


    def get_user_credentials(self, user):
        """
        Return the password of a user

        Args:
            user: (string) username that you want to get credentials for

        Returns:
            string: password belonging to the specified user in the params
        """
        if user not in self.secrets["ebird"]["user_credentials"]:
            raise Exception(f"Following user does not exist in the manager: {user}")
        else:
            return self.secrets["ebird"]["user_credentials"][user]

    def get_ebird_apikey(self):
        """Gets the ebird api key from the config manager secrets"""
        if "apikey" not in self.secrets['ebird']:
            raise Exception(f"Cannot find ebird API key in {self.paths['secrets']}")
        else:
            return self.secrets['ebird']['apikey']