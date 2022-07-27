import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption("--language", action="store", default='en')

@pytest.fixture(scope="function")
def browser(request):
	lang = request.config.getoption("language")
	if lang is None:
		raise pytest.UsageError("--language option is empty")
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': lang})
	browser = webdriver.Chrome(options=options)
	yield browser
	browser.quit()
	