import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path='D:/Selenium/Drivers/chromedriver.exe')
    return driver


def pytest_configure(config):
    config._metadata['Project Name'] = "nop Commerce"
    config._metadata['Module Name'] = "Customers"
    config._metadata['Tester'] = "Pavan"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
