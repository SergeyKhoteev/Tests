import pytest
from .pages.main_page import MainPage

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
	page = MainPage(browser, link)
	page.open()
	page.should_be_login_link()
	
	