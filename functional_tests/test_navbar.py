from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


class TestIndexPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver.exe")
        self.username = 'test'
        self.password = 'Test123_'
        self.email = 'test@test.com'

    def tearDown(self):
        self.browser.close()

    def test_start(self):
        self.browser.get(self.live_server_url)

        # The user requests the page for the first time
        time.sleep(20)

    def test_home_button_redirects_to_home(self):
        self.browser.get(self.live_server_url)
        home_url = self.live_server_url + reverse('index')
        # The user clicks on home button
        self.browser.find_element(By.LINK_TEXT, 'Home').click()
        self.assertEquals(
            self.browser.current_url,
            home_url
        )
        # The user sees content on home page
        self.assertEquals(
            self.browser.find_element(By.TAG_NAME, 'h3').text,
            'Body Language App'
        )

    def test_contact_button_redirects_to_contact(self):
        self.browser.get(self.live_server_url)
        contact_url = self.live_server_url + reverse('contact')
        # The user clicks on contact button
        self.browser.find_element(By.LINK_TEXT, 'Contact').click()
        self.assertEquals(
            self.browser.current_url,
            contact_url
        )
        # The user sees content on contact page
        self.assertEquals(
            self.browser.find_element(By.TAG_NAME, 'h3').text,
            'Contact us'
        )

    def test_help_button_redirects_to_help(self):
        self.browser.get(self.live_server_url)
        help_url = self.live_server_url + reverse('help')
        # The user sees content on help page
        self.browser.find_element(By.LINK_TEXT, 'Help').click()
        self.assertEquals(
            self.browser.current_url,
            help_url
        )
        # The user sees content on help page
        self.assertEquals(
            self.browser.find_element(By.TAG_NAME, 'h3').text,
            'User guide'
        )
