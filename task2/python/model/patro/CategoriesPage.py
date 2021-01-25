from selenium.webdriver.common.by import By

from task2.python.model.BaseClass import BasePage


class CategoriesPageSelectors:
    MOBILE_PHONES = (By.CSS_SELECTOR, "li.list-categories__item:nth-child(2)")
    MOBILE_PHONE_NEXT = (By.PARTIAL_LINK_TEXT, "Mobilní telefony")


class CategoriesPage(BasePage):
    def click_on_mobile_phones(self):
        self.find_element(CategoriesPageSelectors.MOBILE_PHONES).click()

    def click_on_mobiles(self):
        self.find_element(CategoriesPageSelectors.MOBILE_PHONE_NEXT).click()