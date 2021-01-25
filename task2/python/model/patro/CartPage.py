from selenium.webdriver.common.by import By

from task2.python.model.BaseClass import BasePage


class PageCartLocators:
    ITEM_IN_CART = (By.CLASS_NAME, "js-cart-item")


class CartPage(BasePage):
    def get_items_count(self) -> int:
        return self.find_elements(PageCartLocators.ITEM_IN_CART)