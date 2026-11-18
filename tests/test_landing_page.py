
import pytest
import allure

from pages.landing_page import LandingPage


@allure.feature("Landing Page")
class TestLandingPage:

    @allure.story("Landing Page UI Verification")
    @allure.title("Verify Book Odisha landing page")
    @pytest.mark.smoke
    def test_landing_page_verification(self, driver):
        landing_page = LandingPage(driver)
        with allure.step("Open Book Odisha application"):
            landing_page.open_landing_page()
        with allure.step("Close promotional popup"):
            landing_page.close_popup()
        with allure.step("Verify landing page URL"):
            assert "booktestnewui.estpl.net:8889" in landing_page.get_current_url()
        with allure.step("Verify hero section"):
            assert landing_page.is_element_displayed(landing_page.HERO_SECTION)
        with allure.step("Verify hero heading"):
            assert landing_page.get_hero_title() == "Discover the Soul of Odisha"
        with allure.step("Verify booking search tabs"):
            tabs = landing_page.get_search_tabs()
            assert len(tabs) == 8
        with allure.step("Verify interactive services"):
            services = landing_page.get_service_cards()
            assert len(services) == 4
        with allure.step("Verify footer"):
            assert landing_page.is_element_displayed(landing_page.FOOTER)

    @allure.story("Landing Page UI Verification")
    @allure.title("Verify featured experiences section")
    @pytest.mark.smoke
    def test_featured_experiences_displayed(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open_landing_page()
        landing_page.close_popup()
        with allure.step("Verify featured experience cards"):
            cards = landing_page.get_featured_cards()
            assert len(cards) > 0, \
                "No featured experience cards are displayed"

    @allure.story("Landing Page UI Verification")
    @allure.title("Verify recommended stays section")
    @pytest.mark.smoke
    def test_recommended_stays_displayed(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open_landing_page()
        landing_page.close_popup()
        with allure.step("Verify recommended stay cards"):
            cards = landing_page.get_recommended_cards()
            assert len(cards) > 0, \
                "No recommended stay cards are displayed"

    @allure.story("Landing Page UI Verification")
    @allure.title("Verify landing page footer")
    @pytest.mark.smoke
    def test_landing_page_footer_displayed(self, driver):
        landing_page = LandingPage(driver)
        landing_page.open_landing_page()
        landing_page.close_popup()
        with allure.step("Verify footer is displayed"):
            assert landing_page.is_element_displayed(
                landing_page.FOOTER
            ), "Landing page footer is not displayed"

    def test_close_promotional_popup(self, driver):
        landing_page = LandingPage(driver)

        landing_page.open_landing_page()
        landing_page.close_popup()

        assert not landing_page.is_element_displayed(
            landing_page.PAGE_POPUP
        )





