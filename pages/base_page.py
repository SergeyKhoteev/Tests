from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage():

	def __init__(self, browser, url):
		self.browser = browser
		self.url = url

	def open(self):
		self.browser.get(self.url)

	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'login_link is not presented'

	def go_to_login_page(self):
		self.should_be_login_link()
		login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		login_link.click()

	def should_be_basket_link(self):
		assert self.is_element_present(*BasePageLocators.BASKET_LINK), 'basket_link is not presented'

	def go_to_basket_page(self):
		basket_button = self.browser.find_element(*BasePageLocators.BASKET_LINK)
		basket_button.click()

	def should_be_authorized_user(self):
	    assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
	    																" probably unauthorised user"

	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except NoSuchElementException:
			return False

		return True

	def is_not_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True

		return False

	def is_disappeared(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException).\
				until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False

		return True

