import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as exp_option

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    lang = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        """Эта часть используется для запуска тестов на удаленном сервере
        comp_options = webdriver.ChromeOptions()
        comp_options.add_argument('--ignore-certificate-errors')
        capabilities = comp_options.to_capabilities()
        comp_options.add_argument(f'--lang={lang}')
        browser = webdriver.Remote(command_executor='http://ip/wd/hub', desired_capabilities=capabilities)
        """
        options = exp_option()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        """Эта часть используется для запуска тестов на удаленном сервере
        comp_options = webdriver.FirefoxOptions()
        comp_options.add_argument('--ignore-certificate-errors')
        capabilities = comp_options.to_capabilities()
        browser = webdriver.Remote(command_executor='http://ip/wd/hub', desired_capabilities=capabilities)
        """
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", lang)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()