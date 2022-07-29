import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

# def test_add_button(browser):
#     browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
#     button = browser.find_elements(By.CSS_SELECTOR, ".btn-primary")
#     print("\nbrowser.find_elements(By.CSS_SELECTOR, '.btn-primary') = ", button)
#     print("\nlen(browser.find_elements(By.CSS_SELECTOR, '.btn-primary'))=", len(button))
#     print("\nButton text: ", button.text)

#     ### Assert я, конечно, добавил, раз так указано в задании, но смысла в нем никакого нет.
#     ### В случае отсутствия кнопки тест и так упадёт с исключением.
#     ### Писать код через find_elements, что бы потом тест упал на assert из-за нулевой длины - идиотия и пустая трата времени и ресурсов машины.

#     assert button.text is not None

def test_guest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	# link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
	page = MainPage(browser, link)
	page.open()
	page.go_to_login_page()
	login_page = LoginPage(browser, browser.current_url)
	login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	# link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
	page = MainPage(browser, link)
	page.open()
	page.should_be_login_link()



	