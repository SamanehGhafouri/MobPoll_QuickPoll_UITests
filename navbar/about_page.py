from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.keys import Keys
import unittest


class AboutPage(unittest.TestCase):

    def setUp(self) -> None:
        self.about_driver = webdriver.Chrome()
        self.about_url = "http://localhost:4200/about"
        self.about_driver.get(self.about_url)
        self.main_url = "http://localhost:4200/"

    def test_nav_to_create_poll(self):

        self.about_driver.find_element_by_xpath("/html/body/app-root/app-nav-bar/nav/ul/li[1]/a").click()
        actual = self.about_driver.current_url
        expected = self.main_url
        self.assertEqual(expected, actual)

    def test_nav_to_learn_more(self):

        self.about_driver.find_element_by_xpath("/html/body/app-root/app-nav-bar/nav/ul/li[4]/a").click()
        actual = self.about_driver.current_url
        expected = f"{self.main_url}" + "learn_more"
        self.assertEqual(expected, actual)

    def test_nav_to_public_poll(self):

        self.about_driver.find_element_by_xpath("/html/body/app-root/app-nav-bar/nav/ul/li[5]/a").click()
        actual = self.about_driver.current_url
        expected = f"{self.main_url}" + "public_polls"
        self.assertEqual(expected, actual)

    def test_about_page_help_header(self):

        self.about_driver.find_element_by_xpath("/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()
        actual = self.about_driver.find_element_by_xpath("/html/body/ngb-modal-window/div/div/app-about-help/app-help/div/label[1]").text
        expected = "HELP: ABOUT"
        self.assertEqual(expected, actual)

    def test_about_page_help_header_color(self):
        self.about_driver.find_element_by_xpath(
            "/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()
        color = self.about_driver.find_element_by_xpath(
            "/html/body/ngb-modal-window/div/div/app-about-help/app-help/div/label[1]").value_of_css_property("color")
        actual = Color.from_string(color).hex
        expected = "#3fa9f5"
        self.assertEqual(expected, actual)

    def test_about_page_help_header_font(self):
        self.about_driver.find_element_by_xpath(
            "/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()
        actual = self.about_driver.find_element_by_xpath(
            "/html/body/ngb-modal-window/div/div/app-about-help/app-help/div/label[1]").value_of_css_property("font-family")
        expected = "days-font"
        self.assertEqual(expected, actual)

    def test_about_page_help_paragraph_text(self):

        self.about_driver.find_element_by_xpath("/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()
        actual = self.about_driver.find_element_by_xpath(
            "/html/body/ngb-modal-window/div/div/app-about-help/app-help/div/label[2]/p").text
        expected = "Find us on Facebook by visiting the links on this page."
        self.assertEqual(expected, actual)

    def test_about_page_help_paragraph_text_color(self):
        self.about_driver.find_element_by_xpath(
            "/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()
        color = self.about_driver.find_element_by_xpath(
            "/html/body/ngb-modal-window/div/div/app-about-help/app-help/div/label[2]/p").value_of_css_property("color")
        actual = Color.from_string(color).hex
        expected = "#ff9e13"
        self.assertEqual(expected, actual)

    def test_about_page_help_submit_button(self):
        self.about_driver.find_element_by_xpath(
            "/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()
        actual = self.about_driver.find_element_by_class_name("alert-box-button").text
        expected = "CLOSE"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()