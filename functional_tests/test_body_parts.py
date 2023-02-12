from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from BodyLanguage.models import *


class TestBodyPartsPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver.exe")

    def tearDown(self):
        self.browser.close()

    def test_start(self):
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
        # The user sees content on body parts page
        self.assertEquals(
            self.browser.find_element(By.TAG_NAME, 'h3').text,
            'Gestures by body parts'
        )

    # FAIL
    # def test_body_parts_gestures_are_rendered(self):
    #     self.browser.get(self.live_server_url)
    #     # The user clicks on the categories button
    #     self.browser.find_element(By.PARTIAL_LINK_TEXT, '📖').click()
    #
    #     # The user clicks on the body parts button
    #     self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Body parts').click()
    #
    #     self.user = User.objects.create_user("test", "test@test.com", "Test123_")
    #     self.meaning = Meaning.objects.create(meaning='sadness')
    #     self.context = Context.objects.create(context='in_love')
    #     self.behaviour = Behaviour.objects.create(behaviour='lying')
    #     self.gesture = Gesture.objects.create(user=self.user, gesture='eye_gaze', category='face', male=True,
    #                                      female=True, adult=True, child=False)
    #     self.gesture.meaning.add(self.meaning)
    #     self.gesture.context.add(self.context)
    #     self.gesture.behaviour.add(self.behaviour)
    #     self.gesture.save()
    #
    #     # self.assertTrue(
    #     #     self.browser.find_element(By.CLASS_NAME, 'card my-4 mx-auto'),
    #     # )
    #
    #     time.sleep(20)
