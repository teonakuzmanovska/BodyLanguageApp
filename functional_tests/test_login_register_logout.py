from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


class TestLoginRegisterLogout(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver.exe")
        self.username = 'test'
        self.password = 'Test123_'
        self.email = 'test@test.com'

    def test_login_register_logout(self):
        self.browser.get(self.live_server_url)
        # User clicks on login
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Log in').click()
        # User clicks on register
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Register here').click()
        self.browser.find_element(By.ID, 'id_username').send_keys(self.username)
        self.browser.find_element(By.ID, 'id_first_name').send_keys(self.username)
        self.browser.find_element(By.ID, 'id_last_name').send_keys(self.username)
        self.browser.find_element(By.ID, 'id_email').send_keys(self.email)
        self.browser.find_element(By.ID, 'id_password1').send_keys(self.password)
        self.browser.find_element(By.ID, 'id_password2').send_keys(self.password)
        time.sleep(20)
        self.browser.find_element(By.ID, 'register').click()
        # User is redirected to login
        self.browser.find_element(By.ID, 'id_username').send_keys(self.username)
        self.browser.find_element(By.ID, 'id_password').send_keys(self.password)
        # User clicks on login
        time.sleep(20)
        self.browser.find_element(By.ID, 'login').click()
        logout_url = self.live_server_url + reverse('login')
        # User clicks on logout
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Log out').click()
        self.assertEquals(
            self.browser.current_url,
            logout_url
        )

    def test_invalid_login(self):
        self.browser.get(self.live_server_url)
        # User clicks on login
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Log in').click()
        # User is redirected to login
        self.browser.find_element(By.ID, 'id_username').send_keys(self.username)
        self.browser.find_element(By.ID, 'id_password').send_keys(self.password)
        # User clicks on login
        time.sleep(20)
        self.browser.find_element(By.ID, 'login').click()
        # The Log out button should not be visible because the user hasn't logged in
        self.assertTrue(
            self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Log in')
        )

    def test_invalid_register(self):
        self.browser.get(self.live_server_url)
        # User clicks on login
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Log in').click()
        # User clicks on register
        self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Register here').click()
        self.browser.find_element(By.ID, 'id_username').send_keys(self.username)
        self.browser.find_element(By.ID, 'id_first_name').send_keys(self.username)
        self.browser.find_element(By.ID, 'id_last_name').send_keys(self.username)
        self.browser.find_element(By.ID, 'id_email').send_keys(self.email)
        self.browser.find_element(By.ID, 'id_password1').send_keys(self.password)
        self.browser.find_element(By.ID, 'id_password2').send_keys('test123_')
        time.sleep(20)
        self.browser.find_element(By.ID, 'register').click()
        # The user should be on register page still
        register_url = self.live_server_url + reverse('register')
        self.assertEquals(
            self.browser.current_url,
            register_url
        )

