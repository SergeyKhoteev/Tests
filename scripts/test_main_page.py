import pytest
from selenium.webdriver.common.by import By

def test_add_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    print("\nButton text: ", button.text)

    ### Assert я, конечно, добавил, раз так указано в задании, но смысла в нем никакого нет.
    ### В случае отсутствия кнопки тест и так упадёт с исключением.
    ### Писать код через find_elements, что бы потом тест упал на assert из-за нулевой длины - идиотия и пустая трата времени и ресурсов машины.

    assert button.text is not None

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()