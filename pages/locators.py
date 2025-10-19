from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASSWORD = (By.NAME, "registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_PRODUCT_HAS_BEEN_ADDED = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    ALERT_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ALERT_PRICE_PRODUCT_HAS_BEEN_ADDED = (By.CSS_SELECTOR, "#messages > div.alert.alert-info.fade.in > div")
    ALERT_PRICE_PRODUCT = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.fade.in > div > p:nth-child(1) > strong")
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_BASKET_FORM = (By.CSS_SELECTOR, "#basket_formset > div")


