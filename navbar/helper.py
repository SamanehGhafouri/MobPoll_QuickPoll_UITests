from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.keys import Keys

import unittest
import requests

#
driver = webdriver.Chrome()
url = "http://localhost:4200/about"
driver.get(url)
driver.find_element_by_xpath(
            '/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a').click()
print(driver.find_element_by_xpath(
            '/html/body/ngb-modal-window/div/div/app-about-help/app-help/div/label[1]').text)
message = driver.find_element_by_xpath("/html/body/ngb-modal-window/div/div/app-about-help/app-help/div/label[1]")
color = message.value_of_css_property("color")
hex = Color.from_string(color).hex
print(hex)