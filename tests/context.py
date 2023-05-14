import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import webscraper.ebird as ebirdscraper
import configs.manager as configs
import ebird.api as ebird_api_lib