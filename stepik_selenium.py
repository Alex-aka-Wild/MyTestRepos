from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as dc
from selenium.webdriver.support.ui import Select
import time
import os
import math

def func(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Remote(command_executor='http://<ip_addr_remote_server>:4444/wd/hub',desired_capabilities=dc.CHROME)
link = 'http://suninjuly.github.io/redirect_accept.html'
driver.get(link)




btn = driver.find_element_by_css_selector('button[type="Submit"]')
btn.click()
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)
x_element = driver.find_element_by_css_selector('span[id="input_value"]').text

y = func(x_element)

driver.find_element_by_css_selector('input[id="answer"]').send_keys(y)
btn = driver.find_element_by_css_selector('button[type="Submit"]')
btn.click()

time.sleep(30)

driver.quit()
