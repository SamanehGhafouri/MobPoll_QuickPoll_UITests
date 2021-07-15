from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import requests


# driver = webdriver.Chrome()
# url = "http://localhost:4200/"
# driver.get(url)


class NavbarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:4200/"
        self.driver.get(self.url)

    def test_status_code(self):
        response = requests.get(self.url)
        actual = response.status_code
        expected = 200
        self.assertEqual(expected, actual)

    def test_title(self):
        actual_title = self.driver.title
        expected = "MobpollInAngular"
        self.assertEqual(expected, actual_title)

    def test_navigate_to_create_poll(self):
        self.driver.find_element_by_xpath('/html/body/app-root/app-nav-bar/nav/ul/li[1]/a').click()
        actual = self.driver.current_url
        expected = f"{self.url}"
        self.assertEqual(expected, actual)

    def test_navigate_to_about(self):
        self.driver.find_element_by_xpath('/html/body/app-root/app-nav-bar/nav/ul/li[3]/a').click()
        actual = self.driver.current_url
        expected = f"{self.url}" + "about"
        self.assertEqual(expected, actual)

    def test_navigate_to_more(self):
        self.driver.find_element_by_xpath('/html/body/app-root/app-nav-bar/nav/ul/li[4]/a').click()
        actual = self.driver.current_url
        expected = f"{self.url}" + "learn_more"
        self.assertEqual(expected, actual)

    def test_navigate_to_public_polls(self):
        self.driver.find_element_by_xpath('/html/body/app-root/app-nav-bar/nav/ul/li[5]/a').click()
        actual = self.driver.current_url
        expected = f"{self.url}" + "public_polls"
        self.assertEqual(expected, actual)

    def test_create_poll_help_header(self):
        self.driver.find_element_by_xpath('/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a').click()
        actual = self.driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/app-create-poll-help/app-help/div/label[1]').text
        expected = "HELP: CREATE A POLL"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

