from .locators import BasketPageLocators as BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):

	def should_be_empty_basket(self):
		assert self.is_not_element_present(*BasePageLocators.BASKET_CONTENT), 'Product in the basket'

	def should_be_empty_basket_message(self):
		assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), 'No message with empty basket'
