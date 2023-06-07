from webscraper.ebird import EbirdWebScraper
from configs.manager import ConfigManager
from ebird.api import EbirdApiWrapper 

class EbirdAlertManager():
    """Manages the custom ebird alerts. Gets differences between a users life list and hotspot checklists"""

    def __init__(self, config_paths, api_delay=0.5):
        """
        Initialize the config manager with secrets and alert configurations and the Ebird api wrapper
        
        Args:
            config_paths: (dict) Dictionary containing the paths to the secrets and alert-configs in the "secrets" and "alert-configs" keys
            api_delay: (float) Seconds to delay between calls for the Ebird API
        """

        self.config_manager = ConfigManager(config_paths)
        self.ebird_api = EbirdApiWrapper(self.config_manager.get_ebird_apikey())
        self.life_lists = {}
        self.api_delay = api_delay
        self.alerts = {}


    def get_life_lists(self):
        """Go through all of the users in the alert configs and get their life lists"""

        for user in self.config_manager.alert_configs:
            # Scrape Ebird page to get the life list
            print(f"Getting life list for {user}...")
            with EbirdWebScraper(user,self.config_manager.get_user_credentials(user)) as scraper:
                life_list =  scraper.get_life_list()

            # Call the Ebird api to get the more details using the species code from the life list
            detailed_life_list = []
            species_codes = ",".join(life_list)
            ebird_taxonomy_resp = self.ebird_api.get_bird_taxonomy(species_codes)

            if ebird_taxonomy_resp.status_code == 200:
                detailed_life_list = ebird_taxonomy_resp.json()
            else:
                print(f"Unable to get taxonomy for species: {species_codes}, Status Code: {ebird_taxonomy_resp.status_code} ({ebird_taxonomy_resp.reason})")
            self.life_lists[user] = detailed_life_list


    def compare_checklist(self, user, checklist):
        """
        Compare a ebird checklist w/ the life list of a user and return all the birds
        seen in the checklist but not the user's life list

        Args:
            user: (string) Ebird user whose life list you're comparing the checklist to
            checklist: (Ebird checklist) Ebird checklist to compare again

        Returns:
            List of birds seen in the checklist but not the user's life list along with their observation details
        """

        life_list_species_codes = [species["speciesCode"] for species in self.life_lists[user]]
        new_species = []
        detailed_new_species = []
        observation_map = {}

        # Get all the new birds in the checklist
        for observation in checklist["obs"]:
            if observation["speciesCode"] not in life_list_species_codes:
                observation_map[observation["speciesCode"]] = observation
                new_species.append(observation["speciesCode"])

        # Call the Ebird api to get more details on all the new birds
        species_codes = ",".join(new_species)
        ebird_taxonomy_resp = self.ebird_api.get_bird_taxonomy(species_codes)
        if ebird_taxonomy_resp.status_code == 200:
            detailed_new_species = ebird_taxonomy_resp.json()
        else:
            print(f"Unable to get taxonomy for species: {species_codes}, Status Code: {ebird_taxonomy_resp.status_code} ({ebird_taxonomy_resp.reason})")
        
        # Add the additional observation information to the detailed species list
        for new_species in detailed_new_species:
            for key, val in observation_map[new_species["speciesCode"]]:
                if key not in new_species:
                    new_species[key] = val

        return detailed_new_species

            
