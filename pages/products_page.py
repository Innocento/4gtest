from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    PRODUCT_ADD_BUTTON = (By.CLASS_NAME, "btn_inventory")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_first_product_to_cart(self):
        self.driver.find_elements(*self.PRODUCT_ADD_BUTTON)[0].click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
