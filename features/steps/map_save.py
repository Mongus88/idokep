from behave import given, when, step, then

from utils.file_writer import save_screenshot


@when('go to precipitation map page')
def go_to_precipitation_map_page(context):
    context.base_page.navigate_to_map("Térképek", "Csapadék")


@step('see the precipitation map for the last 24 hours')
def see_24h_precipitation_map(context):
    context.current_map = context.precipitation_page.one_day_precipitation_map()


@then('save the image of the precipitation map')
def save_precipitation_map(context):
    save_screenshot(context.current_map, "csapadek")


@when('go to heat map page')
def go_to_heat_map_page(context):
    context.base_page.navigate_to_map("Hőtérkép", "Magyarország")


@step('view the current heat map')
def see_current_heat_map_page(context):
    context.current_map = context.hun_heat_page.one_day_heat_map()


@then('save the image of the heat map')
def save_heat_map(context):
    save_screenshot(context.current_map, "hoterkep")
