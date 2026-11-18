
import pytest
import allure

from pages.landing_page import LandingPage
from pages.hotel_page import HotelPage


class TestHotel:

    @allure.story("Hotel Search Section")
    @allure.title("Verify Hotel search section default selection")
    @pytest.mark.smoke
    def test_hotel_search_default_selection(self, driver):

        landing_page = LandingPage(driver)
        hotel_page = HotelPage(driver)

        landing_page.open_landing_page()
        landing_page.close_popup()

        assert hotel_page.is_hotel_tab_active(), \
            "Hotel tab is not selected by default"

        assert hotel_page.is_hotel_search_displayed(), \
            "Hotel search section is not displayed"

        assert hotel_page.is_location_displayed(), \
            "Location dropdown is not displayed"

        assert hotel_page.is_date_picker_displayed(), \
            "Date picker is not displayed"

        assert hotel_page.is_guests_rooms_displayed(), \
            "Guests and Rooms element is not displayed"

        assert hotel_page.is_search_button_displayed(), \
            "Search button is not displayed"

        assert hotel_page.is_location_enabled(), \
            "Location dropdown is disabled"

        assert hotel_page.is_date_picker_enabled(), \
            "Date picker is disabled"

        assert hotel_page.is_search_button_enabled(), \
            "Search button is disabled"

        print("\nHotel search section is displayed correctly.")
        print("Hotel tab is selected by default.")

    @allure.story("Hotel Location")
    @allure.title("Verify available hotel locations")
    @pytest.mark.smoke
    def test_hotel_location_options(self, driver):
        landing_page = LandingPage(driver)
        hotel_page = HotelPage(driver)

        landing_page.open_landing_page()
        landing_page.close_popup()

        locations = hotel_page.get_location_options()

        print(f"\nTotal available locations: {len(locations)}")

        for index, location in enumerate(locations, start=1):
            print(f"{index}. {location}")

        assert len(locations) == 14, \
            f"Expected 14 locations, but found {len(locations)}"

    @allure.story("Hotel Date Picker")
    @allure.title("Inspect hotel date picker and available dates")
    @pytest.mark.smoke
    def test_hotel_date_picker_inspection(self, driver):
        landing_page = LandingPage(driver)
        hotel_page = HotelPage(driver)
        landing_page.open_landing_page()
        landing_page.close_popup()
        hotel_page.open_date_picker()
        months = hotel_page.get_calendar_months()
        print("\nDisplayed calendar months:", months)
        assert len(months) == 2, \
            f"Expected two calendar months, found {len(months)}"
        hotel_page.get_calendar_day_status()

    @allure.story("Hotel Date Picker")
    @allure.title("Verify past dates disabled and future dates enabled")
    @pytest.mark.smoke
    def test_hotel_past_and_future_dates(self, driver):
        landing_page = LandingPage(driver)
        hotel_page = HotelPage(driver)

        landing_page.open_landing_page()
        landing_page.close_popup()

        hotel_page.open_date_picker()

        past_dates = hotel_page.get_past_dates()
        available_dates = hotel_page.get_available_dates()

        print("\nDisabled past dates:", past_dates)
        print("\nAvailable dates:", available_dates)

        assert past_dates, "No disabled past dates found"
        assert available_dates, "No available future dates found"

        print("\nPast and future date availability verified.")

    @allure.story("Hotel Date Picker")
    @allure.title("Verify check-in and check-out date selection")
    @pytest.mark.smoke
    def test_hotel_checkin_checkout_selection(self, driver):
        landing_page = LandingPage(driver)
        hotel_page = HotelPage(driver)

        landing_page.open_landing_page()
        landing_page.close_popup()
        hotel_page.select_hotel_dates(
            "26 Nov 2026",
            "27 Nov 2026"
        )

        selected_dates = driver.find_element(
            *hotel_page.DATE_PICKER
        ).get_attribute("value")
        print("\nSelected hotel dates:", selected_dates)
        assert selected_dates == "26 Nov 2026 - 27 Nov 2026"



