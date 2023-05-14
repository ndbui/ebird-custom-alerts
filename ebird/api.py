import requests

class EbirdApiWrapper():
    """Wrapper for the Ebird API 2.0"""

    def __init__(self, api_key, host="api.ebird.org", context_root="v2"):
        """
        Initialize the wrapper with the API key that will be used to call the Ebird API

        Args:
            api_key: (string) API key that will be used to call the Ebird API
            host: (string) Host for the ebird api (default: "api.ebird.org")
            context_root: (string) Context root for the ebird api (default: "v2")
        """
        self.api_key = api_key
        self.host = host
        self.context_root = context_root

    def generate_request_headers(self):
        """Helper function to generate request headers for each of the EBird API calls"""
        return {
            "x-ebirdapitoken": self.api_key
        }

    def get_bird_taxonomy(self, species_code):
        """
        Retrieve bird taxonomy from the Ebird API using a specified species code

        Args:
            species_code: (string) Species code of the bird you want to get the taxonomy for

        Returns:
            Ebird bird taxonomy
        """
        url = f"https://{self.host}/{self.context_root}/ref/taxonomy/ebird?fmt=json&species={species_code}"
        headers = self.generate_request_headers()
        return requests.get(url, headers=headers)



    def get_checklist(self, checklist_id):
        """
        Get Checklist information from Ebird

        Args:
            checklist_id: (string) Id of the checklist you want to get more information about

        Returns:
            Ebird checklist information including all of the observations made in the checklist
        """
        url = f"https://{self.host}/{self.context_root}/product/checklist/view/{checklist_id}?fmt=json"
        headers = self.generate_request_headers()
        return requests.get(url, headers=headers)

    def get_recent_checklists(self, region_code, max_results=20):
        """
        Get the recent checklists made at a location

        Args:
            region_code: (string) The country, subnational1, subnational2 or location code.
            max_results: (int) How many results to return (default: 20)

        Returns:
            List of recent checklists
        """
        url = f"https://{self.host}/{self.context_root}/product/lists/{region_code}?fmt=json&maxResults={max_results}"
        headers = self.generate_request_headers()
        return requests.get(url, headers=headers)