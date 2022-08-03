from .base_page import BasePage
from .locators import LoginPageLocators as LoginPageLocators

import time


class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		assert 'login' in self.browser.current_url, 'login not in link'

	def should_be_login_form(self):
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login_form is not presented'

	def should_be_register_form(self):
		assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register_form is not presented'

	def register_new_user(self):
		email, password = self.generate_email_and_password()
		email_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
		email_form.send_keys(email)
		password_form1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD1)
		password_form1.send_keys(password)
		password_form2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD2)
		password_form2.send_keys(password)
		button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)
		button.click()

	def generate_email_and_password(self):
		email = str(time.time()) + "@fakemail.org"
		password = str(time.time()) + "@fakemail.org"
		return email, password

	def should_be_login_success_message(self):
		assert self.is_element_present(*LoginPageLocators.LOGIN_SUCCESS_MESSAGE), 'No success message. Authorization failed.'