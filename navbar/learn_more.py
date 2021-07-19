from selenium import webdriver
from selenium.webdriver.support.color import Color
import unittest


class LearnMore(unittest.TestCase):

    def setUp(self):
        self.learn_more_driver = webdriver.Chrome()
        learn_more_url = "http://localhost:4200/learn_more"
        self.learn_more_driver.get(learn_more_url)
        self.main_url = "http://localhost:4200/"

    def test_nav_to_create_poll(self):
        self.learn_more_driver.find_element_by_xpath("/html/body/app-root/app-nav-bar/nav/ul/li[1]/a").click()
        actual = self.learn_more_driver.current_url
        expected = self.main_url
        self.assertEqual(expected, actual)

    def test_nav_to_about(self):
        self.learn_more_driver.find_element_by_xpath("/html/body/app-root/app-nav-bar/nav/ul/li[3]/a").click()
        actual = self.learn_more_driver.current_url
        expected = self.main_url + "about"
        self.assertEqual(expected, actual)

    def test_nav_to_public_polls(self):
        self.learn_more_driver.find_element_by_xpath("/html/body/app-root/app-nav-bar/nav/ul/li[5]/a").click()
        actual = self.learn_more_driver.current_url
        expected = self.main_url + "public_polls"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

