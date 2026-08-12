from behave import given, when, then

from utils.file_writer import save_csv


@when('see if it rains in the next four days')
def see_rains_in_next_four_days(context):
    context.budapest_page.rainy_days(days=4, skip_today=False)


@then('save the results to a csv file')
def save_csv_file(context):
    save_csv(context.budapest_page.rainy_days_results, "raine_forecast")