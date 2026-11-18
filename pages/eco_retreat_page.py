
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class EcoRetreatPage(BasePage):

    # Page locators taken from the supplied HTML
    PAGE_CONTAINER = (
        By.CSS_SELECTOR,
        "app-eco-retreat-list"
    )

    HERO_SECTION = (
        By.CSS_SELECTOR,
        ".page-hero"
    )

    HERO_HEADING = (
        By.CSS_SELECTOR,
        ".page-hero-heading"
    )

    COLLECTION_SECTION = (
        By.ID,
        "ecoRetreatCollection"
    )

    COLLECTION_HEADING = (
        By.CSS_SELECTOR,
        ".eco-section-title"
    )

    DESTINATION_CARDS = (
        By.CSS_SELECTOR,
        ".eco-card"
    )

    DESTINATION_NAMES = (
        By.CSS_SELECTOR,
        ".eco-card-name"
    )

    DISTRICT_NAMES = (
        By.CSS_SELECTOR,
        ".badge-district"
    )

    OPENING_DATES = (
        By.CSS_SELECTOR,
        ".eco-opening-text"
    )

    PRICES = (
        By.CSS_SELECTOR,
        ".price-val"
    )

    TENT_COUNTS = (
        By.CSS_SELECTOR,
        ".tents-num"
    )

    BOOK_NOW_LINKS = (
        By.CSS_SELECTOR,
        "a.eco-book-btn"
    )

    def wait_for_list_page(self):
        self.wait.until(
            EC.url_contains("/tourism/eco-retreat-list")
        )

        self.wait_for_visibility(self.PAGE_CONTAINER)

    def get_hero_heading(self):
        return self.get_text(self.HERO_HEADING)

    def get_collection_heading(self):
        return self.get_text(self.COLLECTION_HEADING)

    def get_destination_cards(self):
        return self.find_elements(self.DESTINATION_CARDS)

    def get_destination_names(self):
        elements = self.find_elements(self.DESTINATION_NAMES)
        return [element.text.strip() for element in elements]

    # def click_book_now(self, index=0):
    #     links = self.find_elements(self.BOOK_NOW_LINKS)
    #     link = links[index]
    #
    #     # Scroll the selected Book Now button into view
    #     self.driver.execute_script(
    #         "arguments[0].scrollIntoView({block: 'center'});",
    #         link
    #     )
    #
    #     # Wait until the button is clickable, then perform normal click
    #     self.wait.until(
    #         EC.element_to_be_clickable(link)
    #     ).click()
    def click_book_now(self, index=0):
        links = self.find_elements(self.BOOK_NOW_LINKS)
        link = links[index]

        # Scroll the button into the visible browser area
        self.driver.execute_script("""
            window.scrollTo({
                top: arguments[0].getBoundingClientRect().top
                     + window.pageYOffset
                     - (window.innerHeight / 2),
                behavior: 'instant'
            });
        """, link)

        # Wait until the button is inside the viewport
        self.wait.until(
            lambda d: d.execute_script("""
                const rect = arguments[0].getBoundingClientRect();
                return rect.top >= 0 &&
                       rect.bottom <= window.innerHeight;
            """, link)
        )

        # Perform normal Selenium click
        self.wait_for_clickable(self.BOOK_NOW_LINKS).click()

    def get_book_now_url(self, index=0):
        links = self.find_elements(self.BOOK_NOW_LINKS)
        return links[index].get_attribute("href")
