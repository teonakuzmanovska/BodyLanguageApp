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

    def test_tips_button_redirects_to_tips(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse('tips')
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '💡').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )

    def test_articles_button_redirects_to_articles(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse('articles')
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '🌐').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )

    def test_categories_button_redirects_to_categories(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse('categories')
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '📖').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )

    def test_quizzes_button_redirects_to_login(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse('login')
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '📝').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )

    def test_progress_button_redirects_to_login(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse('login')
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '📈').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )
