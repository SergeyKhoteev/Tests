from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.content h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.row p.price_color')
    MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    MESSAGE_NAME = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    MESSAGE_PRICE = (By.CSS_SELECTOR, '#messages div:nth-child(3) strong')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn.btn-default')

class BasketPageLocators():
    BASKET_NAME = (By.CSS_SELECTOR, '.basket-items h3')
    BASKET_PRICE = (By.CSS_SELECTOR, '.basket-items .col-sm-1 p.price_color')