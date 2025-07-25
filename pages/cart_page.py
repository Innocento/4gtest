from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")

    def is_item_in_cart(self):
        return len(self.driver.find_elements(*self.CART_ITEM)) > 0
