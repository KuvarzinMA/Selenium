from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators, BasketPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
from faker import Faker

url_list = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

def test_guest_can_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_url()
    product_page.should_be_add_to_basket_button()
# Хочу оставить параметризацию как пример работы с ней. Не снижайте за неё бал, пожалуйста
@pytest.mark.need_review
@pytest.mark.parametrize('link', url_list)
def test_guest_can_add_product_to_basket(browser,link):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_add_to_basket_button()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_alert_inner_product_has_been_added()
    page.should_be_name_product_in_alert()
    page.should_be_alert_inner_product_price()
    page.should_be_price_product_in_alert()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.check_element_not_present(*ProductPageLocators.MESSAGE_SUCCESS)

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.check_element_not_present(*ProductPageLocators.MESSAGE_SUCCESS)

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.check_element_disappeared(*ProductPageLocators.MESSAGE_SUCCESS)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    assert page.is_disappeared(*BasketPageLocators.PRODUCT_BASKET_FORM) == True, "Product is in basket"

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        fake = Faker()
        random_email = fake.email()
        random_password = fake.password(length=9, special_chars=True, digits=True, upper_case=True, lower_case=True)
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(random_email, random_password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"
        page = ProductPage(browser, link)
        page.open()
        page.check_element_not_present(*ProductPageLocators.MESSAGE_SUCCESS)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_add_to_basket_button()
        page.click_add_to_basket()
        page.should_be_alert_inner_product_has_been_added()
        page.should_be_name_product_in_alert()
        page.should_be_alert_inner_product_price()
        page.should_be_price_product_in_alert()

