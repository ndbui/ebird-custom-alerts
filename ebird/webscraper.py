from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from typing import Optional, Type, Self, List
from types import TracebackType


class EbirdWebScraper:
    """Ebird web scraper using Selenium"""

    def __init__(self: Self, username: str, password: str, wait: int = 10) -> None:
        """Initialize the scrapper driver

        Args:
            username (str): Ebird username
            password (str): Ebird user password
            wait (int, optional): Selenium wait time for html elements. Defaults to 10.
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(wait)
        self.host_url = "https://ebird.org/"
        self.username = username
        self.password = password

    def __enter__(self: Self) -> Self:
        """Sign in to Ebird when the scraper is entered"""
        self.signin()
        return self

    def __exit__(
        self: Self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        exc_traceback: Optional[TracebackType],
    ) -> None:
        """Close out the driver on exit. Print out exceptions if they are thrown"""
        if exc_type is not None:
            print(f"Exception Type: {exc_type}")
        if exc_value is not None:
            print(f"Exception Value: {exc_value}")
        if exc_traceback is not None:
            print(f"Exception Traceback: {exc_traceback}")
        self.driver.quit()

    def signin(self: Self):
        """Sign into Ebird using the credentials passed in the init"""
        print("Signing in...")
        url = self.host_url + "home?forceLogin=true"
        self.driver.get(url)

        username_element = self.driver.find_element(By.XPATH, "//input[@id='input-user-name']")
        username_element.send_keys(self.username)

        password_element = self.driver.find_element(By.XPATH, "//input[@id='input-password']")
        password_element.send_keys(self.password)

        signin_element = self.driver.find_element(By.XPATH, "//input[@id='form-submit' and @value='Sign in']")
        signin_element.click()

    def get_life_list(self: Self, region: str = "world") -> List[str]:
        """Scrape the list of seen birds in Ebird filtered by the given region

        Args:
            region (str, optional): Ebird region code used to filter which life list is scraped. Defaults to "world".

        Returns:
            List[str]: list of Ebird bird identifiers
        """

        url = self.host_url + "lifelist/" + region
        self.driver.get(url)

        retval = []
        results = self.driver.find_elements(By.ID, "results")
        species_elements = results[0].find_elements(By.CLASS_NAME, "Observation-species")
        for species_element in species_elements:
            a_tags = species_element.find_elements(By.TAG_NAME, "a")
            if len(a_tags) > 0:
                species_id = a_tags[0].get_attribute("data-species-code")
                retval.append(species_id)

        return retval
