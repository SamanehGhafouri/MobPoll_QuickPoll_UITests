from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


class LearnMore(unittest.TestCase):

    def setUp(self):
        self.learn_more_driver = webdriver.Chrome()
        learn_more_url = "http://localhost:4200/learn_more"
        self.learn_more_driver.get(learn_more_url)
        self.main_url = "http://localhost:4200/"

    def test_learn_more_header(self):
        actual = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[1]/div/div[2]/label").text
        expected = "Learn More".upper()
        self.assertEqual(expected, actual)

    def test_learn_more_header_color(self):
        color = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[1]/div/div[2]/label")\
            .value_of_css_property("color")
        actual = Color.from_string(color).hex
        expected = "#3fa9f5"
        self.assertEqual(expected, actual)

    def test_learn_more_header_font(self):
        actual = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[1]/div/div[2]/label")\
            .value_of_css_property("font-family")
        expected = "days-font"
        self.assertEqual(expected, actual)

    def test_make_voting_count_link_text(self):
        actual = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[1]").text
        expected = "Make Voting Count"
        self.assertEqual(expected, actual)

    def test_make_voting_count_link_text_font(self):
        actual = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[1]")\
            .value_of_css_property("font-family")
        expected = "Verdana"
        self.assertEqual(expected, actual)

    def test_make_voting_count_link_text_color(self):
        color = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[1]")\
            .value_of_css_property("color")
        actual = Color.from_string(color).hex
        expected = "#ff9e13"
        self.assertEqual(expected, actual)

    def test_make_voting_count_link(self):
        self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[1]").click()
        actual = self.learn_more_driver.current_url
        expected = "https://www.facebook.com/MakeVotingCount"
        self.assertEqual(expected, actual)

    def test_MobPoll_link_text(self):
        actual = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[2]").text
        expected = "MobPoll"
        self.assertEqual(expected, actual)

    def test_MobPoll_link_text_font(self):
        actual = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[2]").value_of_css_property("font-family")
        expected = "Verdana"
        self.assertEqual(expected, actual)

    def test_MobPoll_link_text_color(self):
        color = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[2]")\
            .value_of_css_property("color")
        actual = Color.from_string(color).hex
        expected = "#ff9e13"
        self.assertEqual(expected, actual)

    def test_MobPoll_link(self):
        self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[2]").click()
        actual = self.learn_more_driver.current_url
        expected = "https://www.facebook.com/MobPoll"
        self.assertEqual(expected, actual)

    def test_The_center_for_election_link_text(self):
        actual = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[3]").text
        expected = "The Center for Election Science"
        self.assertEqual(expected, actual)

    def test_The_center_for_election_link_text_font(self):
        actual = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[3]")\
            .value_of_css_property("font-family")
        expected = "Verdana"
        self.assertEqual(expected, actual)

    def test_The_center_for_election_link_text_color(self):
        color = self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[3]")\
            .value_of_css_property("color")
        actual = Color.from_string(color).hex
        expected = "#ff9e13"
        self.assertEqual(expected, actual)

    def test_The_center_for_election_link(self):
        self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/div/div/app-more/app-contatiner/div/div[2]/label[2]/a[3]").click()
        actual = self.learn_more_driver.current_url
        expected = "https://electionscience.org/"
        self.assertEqual(expected, actual)

    def test_learn_more_help_header(self):
        self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()

        success_wait = WebDriverWait(self.learn_more_driver, 1800)
        success_wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/ngb-modal-window/div/div/app-learn-more-help/app-help/div/label[2]/p")))
        actual = self.learn_more_driver\
            .find_element_by_xpath("/html/body/ngb-modal-window/div/div/app-learn-more-help/app-help/div/label[1]").text
        expected = "Help: Learn More".upper()
        self.assertEqual(expected, actual)

    def test_learn_more_help_header_font(self):
        self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()
        actual = self.learn_more_driver.find_element_by_xpath(
            "/html/body/ngb-modal-window/div/div/app-learn-more-help/app-help/div/label[1]")\
            .value_of_css_property("font-family")
        expected = "days-font"
        self.assertEqual(expected, actual)

    def test_learn_more_help_header_color(self):
        self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()
        color = self.learn_more_driver.find_element_by_xpath(
            "/html/body/ngb-modal-window/div/div/app-learn-more-help/app-help/div/label[1]")\
            .value_of_css_property("color")
        actual = Color.from_string(color).hex
        expected = "#3fa9f5"
        self.assertEqual(expected, actual)

    def test_learn_more_help_body_text_color(self):
        self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()
        color = self.learn_more_driver.find_element_by_xpath(
            "/html/body/ngb-modal-window/div/div/app-learn-more-help/app-help/div/label[2]/p")\
            .value_of_css_property("color")
        actual = Color.from_string(color).hex
        expected = "#ff9e13"
        self.assertEqual(expected, actual)

    def test_learn_more_help_body_text_font(self):
        self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()
        actual = self.learn_more_driver.find_element_by_xpath(
            "/html/body/ngb-modal-window/div/div/app-learn-more-help/app-help/div/label[2]/p")\
            .value_of_css_property("font-family")
        expected = "days-font"
        self.assertEqual(expected, actual)

    def test_learn_more_help_body_text(self):
        self.learn_more_driver.find_element_by_xpath(
            "/html/body/app-root/app-nav-bar/nav/ul/li[2]/app-help-button/a").click()
        success_wait = WebDriverWait(self.learn_more_driver, 1800)
        success_wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/ngb-modal-window/div/div/app-learn-more-help/app-help/div/label[2]/p")))
        actual = self.learn_more_driver\
            .find_element_by_xpath("/html/body/ngb-modal-window/div/div/app-learn-more-help/app-help/div/label[2]/p").text
        expected = "Learn more about approval voting by visiting the links on this page."
        self.assertEqual(expected, actual)

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

