from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators
import time

class ProductPage(BasePage):

	def product_should_be_added(self):
		assert self.is_element_present(*ProductPageLocators.MESSAGE), 'Message not found'

	def add_to_basket(self):
		add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		add_button.click()
		self.solve_quiz_and_get_code()

	def verify_name(self):
		name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
		name = name.text
		basket_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME)
		basket_name = basket_name.text
		assert name == basket_name, 'Name differs'
		
	def verify_price(self):
		price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
		price = price.text
		basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE)
		basket_price = basket_price.text
		assert price == basket_price, 'Price differs'

	def success_message_is_not_present(self):
		assert self.is_not_element_present(*ProductPageLocators.MESSAGE), 'Message on the page'

	def success_message_disappeared(self):
		assert self.is_disappeared(*ProductPageLocators.MESSAGE)

	# def go_to_basket_page(self):
	# 	basket_button = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
	# 	basket_button.click()
	
	# def go_to_basket_return_name_and_price(self):
	# 	name, price = self.get_product_name_and_price_and_check()
	# 	self.go_to_basket_page()
	# 	return name, price

	# def verify_name_and_price_in_basket(self, name, price):
	# 	basket_name = self.browser.find_element(*BasketPageLocators.BASKET_NAME)
	# 	basket_name = basket_name.text
	# 	assert name == basket_name, 'Name differs'
	# 	basket_price = self.browser.find_element(*BasketPageLocators.BASKET_PRICE)
	# 	basket_price = basket_price.text
	# 	assert price == basket_price, 'Price differs'

	# def should_be_price_the_same(self):
	# 	self.browser.switch_to.alert
	# 	print(alert.text)


