from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urlparse
import re


class CreateAPOll(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:4200/"
        self.driver.get(self.url)

    def test_create_a_poll_with_two_options(self):
        self.driver.find_element_by_id("pollQuestion").send_keys("Is this the first test to create a poll?")
        self.driver.find_element_by_id("option-1").send_keys("Yes")
        self.driver.find_element_by_id("option-2").send_keys("Maybe")
        self.driver.find_element_by_id("createPoll").click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "success-container")))

        actual = self.driver.find_element_by_id("success-header").text
        self.assertEqual("You have created a new poll!", actual)

    def test_create_a_poll_with_three_options(self):
        self.driver.find_element_by_id("pollQuestion").send_keys("Is this the second poll test?")
        self.driver.find_element_by_id("option-1").send_keys("Yes")
        self.driver.find_element_by_id("option-2").send_keys("No")
        self.driver.find_element_by_id("option-3").send_keys("Maybe")
        self.driver.find_element_by_id("createPoll").click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "success-container")))

        cur_url = self.driver.current_url
        path = urlparse(cur_url).path
        if re.match('\/success\/([a-zA-Z0-9])+$', path):
            result = True
        else:
            result = False

        self.assertEqual(True, result)

    def test_created_poll_by_its_poll_url(self):
        self.driver.find_element_by_id("pollQuestion").send_keys("Is poll url ready?")
        self.driver.find_element_by_id("option-1").send_keys("Yes, it is")
        self.driver.find_element_by_id("option-2").send_keys("No")
        self.driver.find_element_by_id("createPoll").click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "success-container")))

        poll_url = self.driver.find_element_by_id("poll-url").text
        poll_id = urlparse(poll_url).path.split('/')[-1]

        success_url = self.driver.current_url
        success_id = urlparse(success_url).path.split('/')[-1]
        self.assertEqual(poll_id, success_id)




