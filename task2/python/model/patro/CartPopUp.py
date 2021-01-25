from selenium.webdriver.common.by import By
from time import sleep
from task2.python.model.BaseClass import BasePage


class CartPopUpSelectors:
    BACK_TO_SHOPPING_BUTTON = (By.CSS_SELECTOR, "a.window-popup__actions__btn:nth-child(2)")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "a.window-popup__actions__btn:nth-child(1)")


class CartPopUp(BasePage):

    def click_on_back_to_shopping_button(self):
        sleep(2)
        self.find_element(CartPopUpSelectors.BACK_TO_SHOPPING_BUTTON).click()

    def click_on_go_to_cart_button(self):
        sleep(2)
        self.find_element(CartPopUpSelectors.GO_TO_CART_BUTTON).click()