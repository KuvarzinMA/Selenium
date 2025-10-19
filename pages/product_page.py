from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_add_to_basket_button()
        self.click_add_to_basket()

    def should_be_product_url(self):
        assert "?promo=newYear" in self.browser.current_url, "Product link is incorrect"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def click_add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def product_name_text(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price_text(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_alert_inner_product_has_been_added(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_PRODUCT_HAS_BEEN_ADDED), "Alert that the product has been added is not presented"

    def should_be_name_product_in_alert(self):
        product_name = self.product_name_text()
        assert product_name == self.browser.find_element(*ProductPageLocators.ALERT_NAME_PRODUCT).text, "Product name is incorrect"

    def should_be_alert_inner_product_price(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_PRICE_PRODUCT_HAS_BEEN_ADDED), "Alert that the product price has been added is not presented"

    def should_be_price_product_in_alert(self):
        product_price = self.product_price_text()
        assert product_price == self.browser.find_element(*ProductPageLocators.ALERT_PRICE_PRODUCT).text, "Product price is incorrect"




