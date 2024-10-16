from ebird.webscraper import EbirdWebScraper
from configs.manager import ConfigManager
import os

if __name__ == "__main__":
    config_manager = ConfigManager()
    user = "nicbui"
    with EbirdWebScraper(user, config_manager.get_user_credentials(user)) as scraper:
        life_list = scraper.get_life_list()

    base_dir = os.path.join("E:\\", "Photography", "Identifications")
    existing_dirs = os.listdir(base_dir)
    for id, name in life_list.items():
        if name not in existing_dirs:
            os.mkdir(os.path.join(base_dir, name))
            os.mkdir(os.path.join(base_dir, name, "positive"))
            os.mkdir(os.path.join(base_dir, name, "negative"))
