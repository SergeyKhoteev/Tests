import pytest
import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
# 								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
# 								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
# 								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
# 								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
# 								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
# 								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
# 								  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
# 								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
# 								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser):
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_to_basket()
	product_page.product_should_be_added()
	product_page.verify_name()
	product_page.verify_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_to_basket()
	product_page.success_message_is_not_present()

def test_guest_cant_see_success_message(browser): 
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.success_message_is_not_present()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.add_to_basket()
	product_page.success_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.go_to_basket_page()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_be_empty_basket()
	basket_page.should_be_empty_basket_message()

class TestUserAddToBasketFromProductPage():

	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.should_be_login_link()
		product_page.go_to_login_page()
		login_page = LoginPage(browser, browser.current_url)
		login_page.should_be_login_page()
		email = str(time.time()) + "@fakemail.org"
		password = str(time.time()) + "@fakemail.org"
		login_page.register_new_user(email, password)
		login_page.should_be_login_success_message()
	
	def test_guest_cant_see_success_message(self, browser): 
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.should_be_authorized_user()
		product_page.success_message_is_not_present()

	def test_guest_can_add_product_to_basket(self, browser):
		product_page = ProductPage(browser, link)
		product_page.open()
		product_page.should_be_authorized_user()
		product_page.add_to_basket()
		product_page.product_should_be_added()
		product_page.verify_name()
		product_page.verify_price()
