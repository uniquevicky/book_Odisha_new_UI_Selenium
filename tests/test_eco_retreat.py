
import pytest
import allure

from pages.landing_page import LandingPage
from pages.eco_retreat_page import EcoRetreatPage


@allure.feature("Eco Retreat")
class TestEcoRetreat:

    @allure.story("Eco Retreat Navigation")
    @allure.title("Verify navigation to Eco Retreat list page")
    @pytest.mark.smoke
    def test_eco_retreat_list_page_navigation(self, driver):

        landing_page = LandingPage(driver)
        eco_retreat_page = EcoRetreatPage(driver)

        with allure.step("Open Book Odisha application"):
            landing_page.open_landing_page()

        with allure.step("Close promotional popup"):
            landing_page.close_popup()

        with allure.step("Click Eco Retreat tab"):
            landing_page.click_search_tab("Eco Retreat")

        with allure.step("Wait for Eco Retreat list page"):
            eco_retreat_page.wait_for_list_page()

        with allure.step("Verify Eco Retreat page heading"):
            assert eco_retreat_page.get_hero_heading() == \
                "Experience Luxury in Nature"

    @allure.story("Eco Retreat List Page")
    @allure.title("Verify destination cards and external Book Now navigation")
    @pytest.mark.smoke
    def test_eco_retreat_cards_and_external_navigation(self, driver):
        landing_page = LandingPage(driver)
        eco_retreat_page = EcoRetreatPage(driver)

        landing_page.open_landing_page()
        landing_page.close_popup()
        landing_page.click_search_tab("Eco Retreat")

        eco_retreat_page.wait_for_list_page()

        # Count destination cards
        cards = eco_retreat_page.get_destination_cards()
        print(f"\nTotal Eco Retreat Cards: {len(cards)}")

        # Print destination names
        destination_names = eco_retreat_page.get_destination_names()

        for index, name in enumerate(destination_names, start=1):
            print(f"{index}. {name}")

        assert len(cards) == 8, "Unexpected number of Eco Retreat cards"

        # Capture current browser tab and expected external URL
        original_window = driver.current_window_handle
        expected_url = eco_retreat_page.get_book_now_url(0)

        # Click Book Now of the first destination
        eco_retreat_page.click_book_now(0)

        # Verify new browser tab opens
        eco_retreat_page.wait.until(
            lambda d: len(d.window_handles) == 2
        )

        new_windows = [
            window for window in driver.window_handles
            if window != original_window
        ]

        assert len(new_windows) == 1

        driver.switch_to.window(new_windows[0])

        assert driver.current_url.startswith(expected_url)

        print(f"\nExternal booking URL opened: {driver.current_url}")
