from webscraper.ebird import EbirdWebScraper
from ebird.alert_manager import EbirdAlertManager
import os

if __name__ == "__main__":
    paths = {
        "secrets": os.path.abspath(os.path.join(os.path.dirname(__file__), "./secrets.json")),
        "alert-configs": os.path.abspath(os.path.join(os.path.dirname(__file__), "./alert-configs.json"))
    }

    alert_manager = EbirdAlertManager(paths)
    # user = "nicbui"
    # with EbirdWebScraper(user,alert_manager.config_manager.get_user_credentials(user)) as scraper:
    #     life_list = scraper.get_life_list()
    # print(life_list)
    alert_manager.get_life_lists()
    print("test")

