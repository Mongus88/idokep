import os

from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()


class BasePage:
    def __init__(self, page):
        self.page = page

    @staticmethod
    def base_url():
        return os.getenv("BASE_URL")

    def dismiss_cookie_banners(self):

        possible_buttons = [
            self.page.get_by_role("button", name="Close success modal"),
            self.page.get_by_role("button", name="Confirm"),
            self.page.locator("#accept-btn"),
        ]

        for button in possible_buttons:
            try:
                if button.is_visible(timeout=1500):
                    button.click()
            except Exception:
                continue

    def open_page(self, city):
        self.page.goto(f'{self.base_url()}/idojaras/{city}')
        self.dismiss_cookie_banners()
        expect(self.page).to_have_url(f'{self.base_url()}/idojaras/{city}', timeout=5000)

    def navigate_to_map(self, menu_name, menu_button):
        menu_link = self.page.get_by_role("link", name=menu_name, exact=True)
        menu_link.wait_for(state="visible", timeout=5000)
        menu_link.hover()

        dropdown_button = self.page.get_by_role("link", name=menu_button, exact=True)
        dropdown_button.wait_for(state="visible", timeout=5000)
        dropdown_button.click()