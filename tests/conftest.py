import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope='class')
def setUp(request):
    global driver
    browser = request.config.getoption("--browser")
    print(browser)
    if browser == 'chrome':
        print("Running test on chrome")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == 'firefox':
        print("Running test on firefox")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'IE':
        driver = webdriver.Ie(executable_path=IEDriverManager().install())
    else:
        print("Running else case")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://letskodeit.teachable.com/p/practice")
    request.cls.driver = driver

    yield driver
    #driver.close()
