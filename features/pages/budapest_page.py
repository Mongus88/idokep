from playwright.sync_api import expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from pages.base_page import BasePage


class BudapestPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.what_to_wear = self.page.locator("span.what-to-wear")
        self.day_elements = self.page.locator(".ik.dailyForecastCol")

        self.rainy_days_results = []

    def recommend_clothes(self):
        self.what_to_wear.wait_for(state="visible")
        return self.what_to_wear.inner_text()

    def rainy_days(self, days=4, skip_today=True):
        self.rainy_days_results = []

        start = 1 if skip_today else 0
        end = days + start

        for i in range(start, end):
            day_element = self.day_elements.nth(i)
            day_name = day_element.locator(".ik.dfColHeader").inner_text()
            day_number = day_name.split("\n")[0].strip()
            rain_container = day_element.locator(".ik.rainlevel-container")

            try:
                rain_container.wait_for(state="visible", timeout=2000)
                will_rain = "Igen"
            except PlaywrightTimeoutError:
                will_rain = "Nem"

            self.rainy_days_results.append({"Dátum": day_number, "Fog esni az eső?": will_rain})
