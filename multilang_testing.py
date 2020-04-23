import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_button_exist(browser):
    browser.get(link)
    get_button = len(browser.find_elements_by_css_selector('.btn-add-to-basket'))
    time.sleep(10)
    assert get_button > 0, "button is absent"
