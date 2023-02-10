from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestIndexPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver.exe")

    def tearDown(self):
        self.browser.close()

    def test_start(self):
        self.browser.get(self.live_server_url)

        # The user requests the page for the first time
        time.sleep(20)

    def test_home_button_redirects_to_home(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse('index')
        self.browser.find_element(By.LINK_TEXT, 'Home').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )

    def test_contact_button_redirects_to_contact(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse('contact')
        self.browser.find_element(By.LINK_TEXT, 'Contact').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )

    def test_help_button_redirects_to_help(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse('help')
        self.browser.find_element(By.LINK_TEXT, 'Help').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )

    # ova kopche e prepokrieno od log in kopcheto posho ne sme logirani
    # def test_logout_button_redirects_to_logout(self):
    #     self.browser.get(self.live_server_url)
    #     add_url = self.live_server_url + reverse('logout')
    #     self.browser.find_element(By.LINK_TEXT, 'Log out').click()
    #     self.assertEquals(
    #         self.browser.current_url,
    #         add_url
    #     )

    def test_login_button_redirects_to_login(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse('login')
        self.browser.find_element(By.LINK_TEXT, 'Log in').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )

