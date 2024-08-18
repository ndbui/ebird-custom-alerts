import ebird.webscraper as ebirdscraper


def test_scraper_init():
    """Test that the ebird web scraper initializes correctly"""
    scraper = ebirdscraper.EbirdWebScraper("testu", "testp")
    assert scraper.username == "testu"
    assert scraper.password == "testp"
