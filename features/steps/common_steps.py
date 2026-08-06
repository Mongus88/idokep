from behave import given
from playwright.sync_api import expect


@given('open the main page of idokep.hu')
def open_main_page(context):
    context.base_page.open_page("Budapest")
