from pages.base_page import BasePage


class PrecipitationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.twenty_four_hours_precipitation = self.page.locator("#csap24a")

    def one_day_precipitation_map(self):
        self.twenty_four_hours_precipitation.wait_for(state="visible")
        return self.twenty_four_hours_precipitation
