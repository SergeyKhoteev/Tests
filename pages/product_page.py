from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):

	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			alert_text = alert.text
			print(f"Your code: {alert_text}")
			alert.accept()
			return True
		except NoAlertPresentException:
			print("No second alert presented")
			return True

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
