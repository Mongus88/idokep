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

    temp_page = context.browser_context.new_page()
    temp_page.goto(f"{BasePage.base_url()}/idojaras/Budapest", wait_until="domcontentloaded")
    try:
        temp_page.locator("#accept-btn").click(timeout=5000)
    except Exception:
        pass

    try:
        temp_page.get_by_role("button", name="Confirm").click(timeout=5000)
    except Exception:
        pass

        temp_page.close()


def before_scenario(context, scenario):
    context.page = context.browser_context.new_page()

    context.base_page = BasePage(context.page)
    context.precipitation_page = PrecipitationPage(context.page)
    context.hun_heat_page = HunHeatPage(context.page)
    context.budapest_page = BudapestPage(context.page)


def after_scenario(context, scenario):
    context.page.close()


def after_all(context):
    os.makedirs("traces", exist_ok=True)
    context.browser_context.tracing.stop(path="traces/trace.zip")

    context.browser_context.close()
    context.browser.close()
    context.playwright.stop()