from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestArticlesPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver.exe")

    def tearDown(self):
        self.browser.close()

    def test_start(self):
        self.browser.get(self.live_server_url)
        # The user clicks on articles button
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '🌐').click()
        # The user clicks on the first link
        self.browser.find_element(By.ID, 'article1').click()

        self.assertEquals(
            self.browser.current_url,
            'https://nacada.ksu.edu/Resources/Clearinghouse/View-Articles/Body-Language-Around-the-World.aspx'
        )
