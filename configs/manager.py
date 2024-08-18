import json
import sys
import os
from typing import Self, Dict


class ConfigManager:
    """Class to access various config values used in the project including secrets"""

    def __init__(
        self: Self, paths: Dict[str, str] = {"secrets": "secrets.json", "alert-configs": "alert-configs.json"}
    ):
        """Initialize configs into the ConfigManager

        Args:
            paths (Dict[str, str], optional): Paths to all config files. Defaults to
                {"secrets": "secrets.json", "alert-configs": "alert-configs.json"}.
        """
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
        self.paths = paths
        self.load_secrets()
        self.load_alert_configs()
        if "ebird" not in self.secrets:
            raise Exception(f"Cannot find ebird key in {paths['secrets']}")

    def load_secrets(self: Self):
        """Load secrets from the valid_secrets.json file into the manager"""
        with open(self.paths["secrets"], "r") as f:
            self.secrets = json.load(f)

    def load_alert_configs(self: Self):
        """Load hotspot and alert configs per user from the alert-configs.json into the manager"""
        with open(self.paths["alert-configs"], "r") as f:
            self.alert_configs = json.load(f)

    def get_user_credentials(self, user: str) -> str:
        """Get the credentials of a user

        Args:
            user (str): username that you want to get credentials for

        Returns:
            str: credentials for the given user
        """
        if user not in self.secrets["ebird"]["user_credentials"]:
            raise Exception(f"Following user does not exist in the manager: {user}")
        else:
            return self.secrets["ebird"]["user_credentials"][user]

    def get_ebird_apikey(self: Self) -> str:
        """Gets the ebird api key from the config manager secrets

        Returns:
            str: Ebird API key
        """
        if "apikey" not in self.secrets["ebird"]:
            raise Exception(f"Cannot find ebird API key in {self.paths['secrets']}")
        else:
            return self.secrets["ebird"]["apikey"]
