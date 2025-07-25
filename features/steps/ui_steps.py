from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@given("I open the SauceDemo login page")
def step_impl(context):

    context.driver = (webdriver.Chrome(ChromeDriverManager().install()))
    context.login_page = LoginPage(context.driver)
    context.products_page = ProductsPage(context.driver)
    context.cart_page = CartPage(context.driver)
    context.login_page.open()

@when("I login with valid credentials")
def step_impl(context):
    context.login_page.login("standard_user", "secret_sauce")

@when("I login with invalid credentials")
def step_impl(context):
    context.login_page.login("invalid_user", "invalid_pass")

@when("I add a product to the cart")
def step_impl(context):
    context.products_page.add_first_product_to_cart()

@when("I go to the cart")
def step_impl(context):
    context.products_page.go_to_cart()

@then("I should see the product in the cart")
def step_impl(context):
    assert context.cart_page.is_item_in_cart()
    context.driver.quit()

@then("I should see a login error message")
def step_impl(context):
    assert "Epic sadface" in context.login_page.get_error_message()
    context.driver.quit()
