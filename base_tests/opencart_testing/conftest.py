import pytest
from os import path, getcwd, makedirs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChrOpts
from selenium.webdriver.firefox.options import Options as FFOpts


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='chrome', type=str)
    parser.addoption("--url", action="store", default='10.211.55.12', type=str)


@pytest.fixture()
def get_url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def get_driver(request):
    browser = request.config.getoption('--browser')
    results_dir = path.join(getcwd(), 'results')

    if not path.exists(results_dir):
        makedirs(results_dir)

    log_path = path.join(results_dir, 'driver.log')
    drivers_dir = path.join(getcwd(), 'drivers')

    driver = None
    driver_name = dict(
        firefox='geckodriver',
        chrome='chromedriver'
    )[browser]
    driver_path = path.join(drivers_dir, driver_name)

    if browser == 'firefox':
        options = FFOpts()
        options.headless = True
        driver = webdriver.Firefox(executable_path=driver_path, service_log_path=log_path, options=options)
    elif browser == 'chrome':
        options = ChrOpts()
        options.add_argument("headless")
        driver = webdriver.Chrome(executable_path=driver_path, service_log_path=log_path, options=options)
    driver.maximize_window()

    def close_driver():
        driver.quit()

    request.addfinalizer(close_driver)
    return driver
