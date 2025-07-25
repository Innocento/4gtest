from behave import given, then
import requests

@given('I query countries using "{currency}" currency')
def step_impl(context, currency):
    context.response = requests.get(f"https://restcountries.com/v3.1/currency/{currency}")

@then("the response should have status 200")
def step_impl(context):
    assert context.response.status_code == 200

@then("I should get at least one country")
def step_impl(context):
    countries = context.response.json()
    assert len(countries) > 0
    assert "name" in countries[0]

@then("the response should have status 404")
def step_impl(context):
    assert context.response.status_code == 404
