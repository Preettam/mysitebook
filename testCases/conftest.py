import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'Chrome' or browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)

    elif browser == 'Firefox' or browser == 'firefox':
        driver = webdriver.Firefox()

    elif browser == 'Edge' or browser == 'edge':
        driver = webdriver.Edge()

    else:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_option)
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_metadata(metadata):
    metadata["Project Name"] = "My Site Book"
    metadata["Environment"] = "QA Environment"
    metadata["Module"] = "Billing Page"
    metadata["Tester"] = "Preettam"
    metadata.pop("Plugins", None)
