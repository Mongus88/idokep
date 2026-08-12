from behave import given, when, then

from features.utils.file_writer import save_txt


@when('see what clothes it recommends today')
def see_recommended_clothes(context):
    context.clothing_advice = context.budapest_page.recommend_clothes()


@then('save the results to a text file')
def save_text_to_file(context):
    save_txt(context.clothing_advice, "clothing_advice")
