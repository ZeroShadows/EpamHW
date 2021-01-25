from selenium.webdriver.common.by import By

from task2.python.model.BaseClass import BasePage


class MobilePhonesPageLocators:
    SORT_FROM_EXPENSIVE = (By.CSS_SELECTOR, "a.box-order-type__item:nth-child(4)")
    ADD_TO_CART_BUTTON_FIRST = (By.CSS_SELECTOR, "li.list-products__item:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2)")
    ADD_TO_CART_SECOND_PHONE = (By.CSS_SELECTOR, "li.list-products__item:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > form:nth-child(1) > button:nth-child(2)")

class MobilePhonesPage(BasePage):

    def order_from_expensive(self):
        self.find_element(MobilePhonesPageLocators.SORT_FROM_EXPENSIVE).click()

    def add_phone_to_basket_first(self):
        self.find_element(MobilePhonesPageLocators.ADD_TO_CART_BUTTON_FIRST).click()

    def add_second_phone_to_cart(self):
        self.find_element(MobilePhonesPageLocators.ADD_TO_CART_SECOND_PHONE).click()
