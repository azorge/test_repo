"""
1. Установить opencart (инструкция есть в дз)
2. Написать фикстуру для запуска трех разных браузеров (ie, firefox, chrome) в
полноэкранном режиме с опцией headless. Выбор браузера должен осуществляться
путем передачи аргумента командной строки pytest.
По завершению работы тестов должно осуществляться закрытие браузера.
3. Добавить опцию командной строки, которая указывает базовый URL opencart.
4. Написать тест, который открывает основную страницу opencart
(http://<ip_or_fqdn>/opencart/) и проверяет,
что мы находимся именно на странице приложения opencart.
"""

# drivers_path = "/Users/alexeyvitsenko/Documents/edu/test_repo/base_tests/" \
#                "opencart_testing/drivers/"

# def test_main_store_chrome():
#     chrome_options = ChrOpts()
#     chrome_options.add_argument("headless")
#     driver = webdriver.Chrome(
#         executable_path=os.path.join(drivers_path, 'chromedriver'),
#         options=chrome_options,
#     )
#     driver.fullscreen_window()
#     driver.get('http://10.211.55.12/opencart')
#     assert driver.title == 'Your Store'
#     driver.close()
#
#
# def test_main_store_firefox():
#     options = FFOpts()
#     options.headless = True
#     driver = webdriver.Firefox(
#         executable_path=os.path.join(drivers_path, 'geckodriver'),
#         options=options,
#     )
#     driver.maximize_window()
#     driver.get('http://10.211.55.12/opencart')
#     assert driver.title == 'Your Store'
#     driver.close()


def test_is_opencart(get_driver, get_url):
    driver = get_driver
    driver.get('http://{}/opencart'.format(get_url))
    assert driver.title == 'Your Store'
