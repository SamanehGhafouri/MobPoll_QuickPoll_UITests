from selenium import webdriver
import unittest

# We expect to see FORM ERROR! if:
# 1. form is empty
# 2. poll question input has only one word
# 3. poll question input has 2 words or more and no option


class CreatePollForm(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:4200/"
        self.driver.get(self.url)

    def test_create_poll_with_empty_input(self):

        self.driver.find_element_by_id("createPoll").click()
        actual = self.driver.find_element_by_class_name("title").text
        expected = "FORM ERROR!"
        self.assertEqual(expected, actual)

    def test_poll_question_input_one_word(self):
        self.driver.find_element_by_id("pollQuestion").send_keys("Hello")
        self.driver.find_element_by_id("createPoll").click()
        actual = self.driver.find_element_by_class_name("title").text
        expected = "FORM ERROR!"
        self.assertEqual(expected, actual)

    def test_poll_question_two_words_no_options(self):
        self.driver.find_element_by_id("pollQuestion").send_keys("Do you have a question?")
        self.driver.find_element_by_id("createPoll").click()
        actual = self.driver.find_element_by_class_name("title").text
        expected = "FORM ERROR!"
        self.assertEqual(expected, actual)

