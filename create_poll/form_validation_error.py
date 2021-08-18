from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# We expect to see FORM ERROR! if:
# 1. form is empty
# 2. poll question input has only one word
# 3. poll question input has 2 words or more and no option
# 4. no poll question and one option
# 5. option one and two, no question


class CreatePollForm(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:4200/"
        self.driver.get(self.url)

    @staticmethod
    def wait_for_error_form_to_display():
        # todo: find a better wait for animation
        time.sleep(1)

    def test_create_poll_with_empty_input(self):
        self.driver.find_element_by_id("createPoll").click()
        self.wait_for_error_form_to_display()
        actual = self.driver.find_element_by_id("alert-box-title").text
        self.assertEqual("FORM ERROR!", actual)

    def test_poll_question_input_one_word(self):
        self.driver.find_element_by_id("pollQuestion").send_keys("Hello")
        self.driver.find_element_by_id("createPoll").click()
        self.wait_for_error_form_to_display()
        actual = self.driver.find_element_by_id("alert-box-title").text
        self.assertEqual("FORM ERROR!", actual)

    def test_poll_question_two_words_no_options(self):
        self.driver.find_element_by_id("pollQuestion").send_keys("Do you have a question?")
        self.driver.find_element_by_id("createPoll").click()
        self.wait_for_error_form_to_display()
        actual = self.driver.find_element_by_id("alert-box-title").text
        self.assertEqual("FORM ERROR!", actual)

    def test_option_one_no_poll_question(self):
        self.driver.find_element_by_id("option-1").send_keys("Yes")
        self.driver.find_element_by_id("createPoll").click()
        self.wait_for_error_form_to_display()
        actual = self.driver.find_element_by_id("alert-box-title").text
        self.assertEqual("FORM ERROR!", actual)

    def test_option_one_two_no_question(self):
        self.driver.find_element_by_id("option-1").send_keys("option one")
        self.driver.find_element_by_id("option-2").send_keys("option-two")
        self.driver.find_element_by_id("createPoll").click()
        self.wait_for_error_form_to_display()
        actual = self.driver.find_element_by_id("alert-box-title").text
        self.assertEqual("FORM ERROR!", actual)

    def tearDown(self) -> None:
        self.driver.close()
