from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestCategoriesPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver.exe")

    def tearDown(self):
        self.browser.close()

    def test_start(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '📖').click()

        self.assertEquals(
            self.browser.find_element(By.TAG_NAME, 'h3').text,
            'Learn gestures per:'
        )

        time.sleep(20)

    def test_body_parts_button_redirects_to_body_parts(self):
        self.browser.get(self.live_server_url)
        # The user clicks on the categories button
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '📖').click()

        body_url = self.live_server_url + reverse('body_parts')

        # The user clicks on the body parts button
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Body parts').click()
        self.assertEquals(
            self.browser.current_url,
            body_url
        )

    def test_emotions_button_redirects_to_emotions(self):
        self.browser.get(self.live_server_url)
        # The user clicks on the categories button
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '📖').click()

        body_url = self.live_server_url + reverse('emotions')

        # The user clicks on the body parts button
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Emotions').click()
        self.assertEquals(
            self.browser.current_url,
            body_url
        )

    def test_context_button_redirects_to_context(self):
        self.browser.get(self.live_server_url)
        # The user clicks on the categories button
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '📖').click()

        body_url = self.live_server_url + reverse('context')

        # The user clicks on the body parts button
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Context').click()
        self.assertEquals(
            self.browser.current_url,
            body_url
        )
