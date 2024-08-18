import requests
from typing import Self, Dict, Any


class EbirdApiWrapper:
    """Wrapper for the Ebird API 2.0"""

    def __init__(self: Self, api_key: str, host: str = "api.ebird.org", context_root: str = "v2"):
        """Initialize the wrapper with the API key that will be used to call the Ebird API

        Args:
            self (Self): _description_
            api_key (str): API key that will be used to call the Ebird API
            host (str, optional): Host for the Ebird api. Defaults to "api.ebird.org".
            context_root (str, optional):Context root for the Ebird api. Defaults to "v2".
        """

        self.api_key = api_key
        self.host = host
        self.context_root = context_root

    def generate_request_headers(self: Self) -> Dict[str, Any]:
        """Helper function to generate request headers for each of the EBird API call

        Returns:
            Dict[str, Any]: Header used for Ebird API calls
        """
        return {"x-ebirdapitoken": self.api_key}

    def get_bird_taxonomy(self: Self, species_code: str) -> requests.Response:
        """Retrieve bird taxonomy from the Ebird API using a specified species code

        Args:
            species_code (str): Species code of the bird you want to get the taxonomy for

        Returns:
            requests.Response: Response containing the Ebird taxonomy
        """

        url = f"https://{self.host}/{self.context_root}/ref/taxonomy/ebird?fmt=json&species={species_code}"
        headers = self.generate_request_headers()
        return requests.get(url, headers=headers)

    def get_checklist(self: Self, checklist_id: str) -> requests.Response:
        """Get Checklist information from Ebird

        Args:
            checklist_id (str): Id of the checklist you want to get more information about

        Returns:
            requests.Response: Response containing Ebird checklist information including all observations
                made in the checklist
        """

        url = f"https://{self.host}/{self.context_root}/product/checklist/view/{checklist_id}?fmt=json"
        headers = self.generate_request_headers()
        return requests.get(url, headers=headers)

    def get_recent_checklists(self: Self, region_code: str, max_results: int = 20) -> requests.Response:
        """Get the recent checklists made at a location

        Args:
            region_code (str): The country, subnational1, subnational2 or location code.
            max_results (int, optional): How many results to return. Defaults to 20.

        Returns:
            requests.Response: Response containing a list of recent checklists
        """

        url = f"https://{self.host}/{self.context_root}/product/lists/{region_code}?fmt=json&maxResults={max_results}"
        headers = self.generate_request_headers()
        return requests.get(url, headers=headers)
