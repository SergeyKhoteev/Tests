from selenium.webdriver.common.by import By


class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn.btn-default')
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	REGISTER_FORM_EMAIL = (By.NAME, "registration-email")
	REGISTER_FORM_PASSWORD1 = (By.NAME, "registration-password1")
	REGISTER_FORM_PASSWORD2 = (By.NAME, "registration-password2")
	REGISTER_FORM_BUTTON = (By.NAME, "registration_submit")
	LOGIN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner.wicon')

class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
	PRODUCT_NAME = (By.CSS_SELECTOR, 'div.content h1')
	PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.row p.price_color')
	MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
	MESSAGE_NAME = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
	MESSAGE_PRICE = (By.CSS_SELECTOR, '#messages div:nth-child(3) strong')

class BasketPageLocators():
	BASKET_CONTENT = (By.CSS_SELECTOR, '#content_inner form')
	EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p:only-child')
	BASKET_NAME = (By.CSS_SELECTOR, '.basket-items h3')
	BASKET_PRICE = (By.CSS_SELECTOR, '.basket-items .col-sm-1 p.price_color')