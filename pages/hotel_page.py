
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
import calendar
from datetime import datetime


class HotelPage(BasePage):

    # Hotel Search Section
    SEARCH_CONTAINER = (By.CSS_SELECTOR, ".search-container")

    # Hotel Tab
    HOTEL_TAB = (
        By.XPATH,
        "//div[@id='searchTabGroup']//button[contains(@class,'search-tab') "
        "and contains(normalize-space(.),'Hotel')]"
    )

    # Search Elements
    LOCATION_DROPDOWN = (By.ID, "hotel-loc")
    DATE_PICKER = (By.ID, "hotel-date")
    GUESTS_ROOMS = (By.CSS_SELECTOR, ".search-display-custom")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn-search-pill")

    # Date Picker
    CALENDAR = ( By.CSS_SELECTOR,"ngx-daterangepicker-material .md-drppicker")
    CALENDAR_MONTHS = (By.CSS_SELECTOR,".md-drppicker .calendar .month")
    CALENDAR_DAYS = (By.CSS_SELECTOR,".md-drppicker .calendar td")

    def is_hotel_tab_active(self):
        hotel_tab = self.wait_for_visibility(self.HOTEL_TAB)
        return "active" in hotel_tab.get_attribute("class").split()

    def is_hotel_search_displayed(self):
        return self.is_element_displayed(self.SEARCH_CONTAINER)

    def is_location_displayed(self):
        return self.is_element_displayed(self.LOCATION_DROPDOWN)

    def is_date_picker_displayed(self):
        return self.is_element_displayed(self.DATE_PICKER)

    def is_guests_rooms_displayed(self):
        return self.is_element_displayed(self.GUESTS_ROOMS)

    def is_search_button_displayed(self):
        return self.is_element_displayed(self.SEARCH_BUTTON)

    def is_location_enabled(self):
        return self.is_element_enabled(self.LOCATION_DROPDOWN)

    def is_date_picker_enabled(self):
        return self.is_element_enabled(self.DATE_PICKER)

    def is_search_button_enabled(self):
        return self.is_element_enabled(self.SEARCH_BUTTON)

    def get_location_options(self):
        location_dropdown = self.wait_for_visibility(
            self.LOCATION_DROPDOWN)
        select = Select(location_dropdown)
        # Exclude the placeholder option
        locations = [
            option.text.strip()
            for option in select.options
            if option.get_attribute("value").strip() ]
        return locations

    def get_location_count(self):
        return len(self.get_location_options())

    def open_date_picker(self):

        # Locate the date input
        date_input = self.wait_for_clickable(self.DATE_PICKER)

        # Position the date input near the top of the viewport
        self.driver.execute_script("""
            const element = arguments[0];
            const pageY = element.getBoundingClientRect().top + window.scrollY;

            window.scrollTo({
                top: Math.max(0, pageY - 150),
                behavior: 'instant'
            });
        """, date_input)

        # Click the date input
        self.wait_for_clickable(self.DATE_PICKER).click()

        # Wait until the calendar is visible
        self.wait.until(
            lambda driver: driver.find_element(
                *self.CALENDAR
            ).is_displayed()
        )

    def get_calendar_months(self):
        months = self.driver.find_elements(*self.CALENDAR_MONTHS)
        return [
            month.text.strip()
            for month in months
            if month.is_displayed()]

    def get_calendar_day_status(self):
        calendars = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".md-drppicker .calendar")

        for calendar_index, calendar in enumerate(calendars, start=1):
            if not calendar.is_displayed():
                continue
            days = calendar.find_elements(By.CSS_SELECTOR, "tbody td")
            print(f"\nCalendar {calendar_index}")
            for day in days:
                day_number = day.text.strip()
                day_classes = day.get_attribute("class")
                if day_number:
                    print(f"Day: {day_number}, Class: {day_classes}")

    def get_past_dates(self):
        calendars = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".md-drppicker .calendar")
        past_dates = []
        for calendar in calendars:
            if not calendar.is_displayed():
                continue
            days = calendar.find_elements(
                By.CSS_SELECTOR,
                "tbody td.disabled")
            for day in days:
                if day.text.strip():
                    past_dates.append(day.text.strip())
        return past_dates

    def get_available_dates(self):
        calendars = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".md-drppicker .calendar")
        available_dates = []
        for calendar in calendars:
            if not calendar.is_displayed():
                continue
            days = calendar.find_elements(
                By.CSS_SELECTOR,
                "tbody td.available:not(.disabled)")
            for day in days:
                if day.text.strip():
                    available_dates.append(day.text.strip())
        return available_dates

    def select_hotel_dates(self, check_in, check_out):
        self.click_element(self.DATE_PICKER)

        # We will implement date selection after inspecting
        # the calendar's HTML and date-cell attributes.

    def select_calendar_day(self, day):
        locator = (
            By.XPATH,
            f"//td[contains(@class,'available') "
            f"and not(contains(@class,'off')) "
            f"and .//span[normalize-space()='{day}']]"
        )
        self.click_element(locator)

        date_element = self.wait_for_clickable(locator)

        # Bring the date cell into the visible center of the screen
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            date_element
        )

        # Wait again after scrolling, then perform a normal Selenium click
        self.wait_for_clickable(locator).click()

    def select_calendar_date(self, date_value):

        target_date = datetime.strptime(date_value, "%d %b %Y")

        month_name = calendar.month_abbr[target_date.month]
        year = str(target_date.year)
        day = str(target_date.day)

        locator = (
            By.XPATH,
            f"//div[contains(@class,'md-drppicker')]"
            f"//table[.//th[contains(@class,'month') "
            f"and contains(normalize-space(.),'{month_name}') "
            f"and contains(normalize-space(.),'{year}')]]"
            f"//td[contains(@class,'available') "
            f"and not(contains(@class,'off')) "
            f"and .//span[normalize-space()='{day}']]"
        )

        # Find the required date
        date_element = self.wait_for_clickable(locator)

        # Click using normal Selenium interaction
        date_element.click()

        # Temporarily do not click

        # Temporarily do not click

    def select_hotel_dates(self, check_in, check_out):

        self.open_date_picker()

        self.select_calendar_date(check_in)
        self.select_calendar_date(check_out)



