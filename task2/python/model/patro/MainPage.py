from selenium.webdriver.common.by import By
from task2.python.model.BaseClass import BasePage


class MainPageLocators:
    MOBILE_PHONES = (By.CSS_SELECTOR, "li.main-menu__item:nth-child(3)")


class MainPage(BasePage):

    def click_on_mobile_phones(self):
        self.find_element(MainPageLocators.MOBILE_PHONES).click()