
from selenium.webdriver.common.by import By

from config.config import BASE_URL
from pages.base_page import BasePage


class LandingPage(BasePage):
    URL = BASE_URL
    PAGE_POPUP=(By.XPATH,"//img[@alt='Special Announcement']")
    POPUP_CLOSE = (By.CSS_SELECTOR,"#welcomepopupmodal button.btn-close-overlay")
    HERO_SECTION = (By.CSS_SELECTOR,".hero-section-fullscreen")
    HERO_TITLE = (By.CSS_SELECTOR,".hero-main-title")
    HERO_SUBTITLE = (By.CSS_SELECTOR,".hero-main-subtitle")

    # ==============================
    # Booking Search Section
    # ==============================

    SEARCH_CONTAINER = (By.CSS_SELECTOR,".search-container")
    SEARCH_TABS = (By.CSS_SELECTOR,"#searchTabGroup .search-tab")
    LOCATION_DROPDOWN = (By.ID,"hotel-loc")
    DATE_PICKER = (By.ID,"hotel-date")
    SEARCH_BUTTON = (By.CSS_SELECTOR,".btn-search-pill")
    # ==============================
    # Interactive Services
    # ==============================
    SERVICES_SECTION = ( By.CSS_SELECTOR,".section-interactive-services")
    SERVICE_CARDS = (By.CSS_SELECTOR,".service-bento")
    # ==============================
    # Featured Experiences
    # ==============================
    FEATURED_CARDS = (By.CSS_SELECTOR,".exp-card")
    # ==============================
    # Recommended Stays
    # ==============================
    RECOMMENDED_CARDS = (By.CSS_SELECTOR,".premium-card")
    # ==============================
    # Footer
    # ============================
    FOOTER = (By.CSS_SELECTOR,".structured-footer")

    # ==============================
    # Page Actions
    # ==============================

    def open_landing_page(self):
        self.navigate_to(self.URL)
    def get_popup_image(self):
        return self.find_element(self.PAGE_POPUP).get_attribute("src")

    def close_popup(self):
        # Wait until popup close button is clickable
        self.wait_for_clickable(self.POPUP_CLOSE).click()

        # Wait until popup image disappears
        self.wait_for_invisibility(self.PAGE_POPUP)
    def get_hero_title(self):
        return self.get_text(self.HERO_TITLE)
    def get_hero_subtitle(self):
        return self.get_text(self.HERO_SUBTITLE)
    def get_search_tabs(self):
        return self.find_elements(self.SEARCH_TABS)
    def get_service_cards(self):
        return self.find_elements(self.SERVICE_CARDS)
    def get_featured_cards(self):
        return self.find_elements(self.FEATURED_CARDS)
    def get_recommended_cards(self):
        return self.find_elements(self.RECOMMENDED_CARDS)
    def click_search_tab(self, tab_name):

        tabs = self.find_elements(self.SEARCH_TABS)

        for tab in tabs:
            if tab.text.strip().casefold() == tab_name.casefold():
                tab.click()
                return

        raise AssertionError(
            f"Search tab '{tab_name}' was not found"
        )
