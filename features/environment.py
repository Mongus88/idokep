import os

from playwright.sync_api import sync_playwright

from pages.base_page import BasePage
from pages.budapest_page import BudapestPage
from pages.hun_heat_page import HunHeatPage
from pages.precipitation_page import PrecipitationPage


def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True, slow_mo=500)
    context.browser_context = context.browser.new_context(viewport={"width": 1920, "height": 1080})

    context.browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)


def before_scenario(context, scenario):
    context.page = context.browser_context.new_page()

    context.page.add_locator_handler(
        context.page.locator("#accept-btn"),
        lambda overlay: overlay.click()
    )

    context.page.add_locator_handler(
        context.page.get_by_role("button", name="Confirm"),
        lambda overlay: overlay.click()
    )

    context.base_page = BasePage(context.page)
    context.precipitation_page = PrecipitationPage(context.page)
    context.hun_heat_page = HunHeatPage(context.page)
    context.budapest_page = BudapestPage(context.page)


def after_scenario(context, scenario):
    context.page.close()


def after_all(context):
    os.makedirs("traces", exist_ok=True)

    if hasattr(context, "browser_context"):
        context.browser_context.tracing.stop(path="traces/trace.zip")
        context.browser_context.close()

    if hasattr(context, "browser"):
        context.browser.close()

    if hasattr(context, "playwright"):
        context.playwright.stop()