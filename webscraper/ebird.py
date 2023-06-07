from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


class EbirdWebScraper():
    """Ebird web scraper using Selenium"""
    def __init__(self, username, password, wait=10):
        """
        Initialize the scrapper driver

        Parameters:
            wait: (int) Selenium wait time when trying to find elements in seconds
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(wait)
        self.host_url = "https://ebird.org/"
        self.username = username
        self.password = password


    def __enter__(self):
        """Sign in to ebird when the scraper is entered"""
        self.signin()
        return self
    

    def __exit__(self,  exc_type, exc_value, exc_traceback):
        """Close out the driver on exit"""
        self.driver.close()
        self.driver.quit()


    def signin(self):
        """
        Sign into ebird using the credentials in the func params

        Args:
            user: (string) Username to sign in with
            password: (string) Password to sign in with
        """
        print("Signing in...")
        url = self.host_url + "home?forceLogin=true"
        self.driver.get(url)

        username_element = self.driver.find_element(By.XPATH, "//input[@id='input-user-name']")
        username_element.send_keys(self.username)

        password_element = self.driver.find_element(By.XPATH, "//input[@id='input-password']")
        password_element.send_keys(self.password)

        signin_element = self.driver.find_element(By.XPATH, "//input[@id='form-submit' and @value='Sign in']")
        signin_element.click()

    

    def get_life_list(self, region="world"):
        """
        Scrape the list of seen birds in ebird filtered by the given region

        Args:
            region: (string) ebird region code used to filter which life list is scraped

        Returns:
            []string: list of ebird bird identifiers
        """
        url = self.host_url + "lifelist/" + region
        self.driver.get(url)

        retval = []
        species_elements = self.driver.find_elements(By.XPATH, "//div[@class='Observation-species']")
        for species_element in species_elements:
            a_tags = species_element.find_elements(By.TAG_NAME, "a")
            if len(a_tags) > 0:
                species_id = a_tags[0].get_attribute("data-species-code")
                retval.append(species_id)

        return retval
    
