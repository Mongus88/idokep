from pages.base_page import BasePage


class HunHeatPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.heat_map_box = self.page.locator("#terkep-box")

    def one_day_heat_map(self):
        self.heat_map_box.wait_for(state="visible")
        return self.heat_map_box
