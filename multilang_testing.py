from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_button_exist(browser):
    browser.get(link)
    get_button = len(browser.find_elements_by_css_selector('.btn-add-to-basket'))
    time.sleep(10)
    assert get_button > 0, "button is absent"