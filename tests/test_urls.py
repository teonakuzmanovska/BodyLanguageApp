from django.contrib.auth.views import LogoutView, LoginView
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from BodyLanguage.views import index, contact, helphtml, tips, articles, categories, quizzes, progress, body_parts, emotions, register


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact)

    def test_help_url_is_resolved(self):
        url = reverse('help')
        print(resolve(url))
        self.assertEquals(resolve(url).func, helphtml)

    def test_tips_url_is_resolved(self):
        url = reverse('tips')
        print(resolve(url))
        self.assertEquals(resolve(url).func, tips)

    def test_articles_url_is_resolved(self):
        url = reverse('articles')
        print(resolve(url))
        self.assertEquals(resolve(url).func, articles)

    def test_categories_url_is_resolved(self):
        url = reverse('categories')
        print(resolve(url))
        self.assertEquals(resolve(url).func, categories)

    def test_quizzes_url_is_resolved(self):
        url = reverse('quizzes')
        print(resolve(url))
        self.assertEquals(resolve(url).func, quizzes)

    def test_progress_url_is_resolved(self):
        url = reverse('progress')
        print(resolve(url))
        self.assertEquals(resolve(url).func, progress)

    def test_body_parts_is_resolved(self):
        url = reverse('body_parts')
        print(resolve(url))
        self.assertEquals(resolve(url).func, body_parts)

    def test_emotions_url_is_resolved(self):
        url = reverse('emotions')
        print(resolve(url))
        self.assertEquals(resolve(url).func, emotions)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LogoutView)
