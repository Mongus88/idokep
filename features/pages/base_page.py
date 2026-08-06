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

    def open_page(self, city):
        self.page.goto(f'{self.base_url()}/idojaras/{city}')
        expect(self.page).to_have_url(f'{self.base_url()}/idojaras/{city}')

    def navigate_to_map(self, menu_name, menu_button):
        menu_link = self.page.get_by_role("link", name=menu_name, exact=True)
        menu_link.wait_for(state="visible", timeout=5000)
        menu_link.hover()

        dropdown_button = self.page.get_by_role("link", name=menu_button, exact=True)
        dropdown_button.wait_for(state="visible", timeout=5000)
        dropdown_button.click()