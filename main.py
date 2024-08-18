from ebird.webscraper import EbirdWebScraper
from configs.manager import ConfigManager

if __name__ == "__main__":
    config_manager = ConfigManager()
    user = "dummy_user"
    with EbirdWebScraper(user, config_manager.get_user_credentials(user)) as scraper:
        life_list = scraper.get_life_list()
    print(life_list)
