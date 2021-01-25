from selenium.webdriver.common.by import By

from task2.python.model.patro.CartPage import CartPage
from task2.python.model.patro.CartPopUp import CartPopUp
from task2.python.model.patro.CategoriesPage import CategoriesPage
from task2.python.model.patro.MainPage import MainPage
from task2.python.model.patro.MobilePhonesPage import MobilePhonesPage


def test_mobile_phones(browser):
    # creating page objects
    main_page = MainPage(browser)
    categories_page = CategoriesPage(browser)
    mobile_phones_page = MobilePhonesPage(browser)
    cart_popup = CartPopUp(browser)
    cart_page = CartPage(browser)

    #test
    main_page.go_to_site()
    main_page.click_on_mobile_phones()
    categories_page.click_on_mobiles()
    mobile_phones_page.order_from_expensive()
    mobile_phones_page.add_phone_to_basket_first()
    cart_popup.click_on_back_to_shopping_button()
    mobile_phones_page.add_second_phone_to_cart()
    cart_popup.click_on_go_to_cart_button()
    items_in_cart = cart_page.get_items_count()

    #assertion
    assert len(items_in_cart) == 2
