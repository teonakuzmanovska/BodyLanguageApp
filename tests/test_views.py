from django.test import TestCase, Client
from django.urls import reverse
from BodyLanguage.models import User, Results
from BodyLanguage.views import percentage, sumPoints, hasObjects


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user("test", "test@test.com", "Test123_")
        self.random_results = Results.objects.create(category="random", points=3, user=self.user)
        self.body_parts_results = Results.objects.create(category="body_parts", points=1, user=self.user)
        self.emotions_results = Results.objects.create(category="emotions", points=2, user=self.user)
        self.contexts_points = Results.objects.create(category="contexts", points=1, user=self.user)
        self.behaviours_points = Results.objects.create(category="behaviours", points=1, user=self.user)
        self.points = [self.random_results, self.body_parts_results, self.emotions_results, self.contexts_points, self.behaviours_points]

    def test_index_GET(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_POST_adds_new_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'Test123_'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user.username, 'test')

    def test_register_GET_render_form(self):
        response = self.client.get(reverse('register'))
        self.assertIn('form', response.context)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_contact_GET(self):
        response = self.client.get(reverse('contact'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_help_GET(self):
        response = self.client.get(reverse('help'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'help.html')

    def test_tips_GET(self):
        response = self.client.get(reverse('tips'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips.html')

    def test_articles_GET(self):
        response = self.client.get(reverse('articles'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles.html')

    def test_categories_GET(self):
        response = self.client.get(reverse('categories'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories.html')

    def test_quizzes_GET_unauthenticated_user(self):
        response = self.client.get(reverse('quizzes'))
        self.assertEquals(response.status_code, 302)

    def test_quizzes_GET_render_questions(self):
        response = self.client.get(reverse('quizzes'))
        # The user is logged in
        if response.context is not None:
            self.assertIn('random', response.context)
            self.assertIn('body_parts', response.context)
            self.assertIn('emotions', response.context)
            self.assertIn('contexts', response.context)
            self.assertIn('behaviours', response.context)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'quizzes.html')

    def test_quizzes_POST_add_results(self):
        response = self.client.post(reverse('progress'), {
            'category': 'random',
            'points': 3,
            'user': self.user
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user.username, 'test')

    def test_progress_GET_unauthenticated_user(self):
        response = self.client.get(reverse('progress'))
        self.assertEquals(response.status_code, 302)

    def test_progress_GET_render_progress(self):
        response = self.client.get(reverse('progress'))
        # The user is logged in
        if response.context is not None:
            self.assertIn('score', response.context)
            self.assertIn('random', response.context)
            self.assertIn('body_parts', response.context)
            self.assertIn('emotions', response.context)
            self.assertIn('contexts', response.context)
            self.assertIn('behaviours', response.context)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'progress.html')

    def test_body_parts_GET(self):
        response = self.client.get(reverse('body_parts'))

        self.assertIn('face', response.context)
        self.assertIn('arms', response.context)
        self.assertIn('legs', response.context)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'body_parts.html')

    def test_emotions_GET(self):
        response = self.client.get(reverse('emotions'))

        self.assertIn('happiness', response.context)
        self.assertIn('sadness', response.context)
        self.assertIn('shame', response.context)
        self.assertIn('guilt', response.context)
        self.assertIn('disgust', response.context)
        self.assertIn('anger', response.context)
        self.assertIn('fear', response.context)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'emotions.html')

    def test_context_GET(self):
        response = self.client.get(reverse('context'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'context.html')

    # functions
    def test_percentage(self):
        userPoints = 62
        allPoints = 100

        self.assertEquals(percentage(userPoints, allPoints), (userPoints / allPoints) * 100)

    def test_percentage_no_points(self):
        self.assertEquals(percentage("abc", 100), 0)

    def test_sumPoints(self):
        sum = 0
        for point in self.points:
            sum += point.points

        self.assertEquals(sumPoints(self.points), sum)

    def test_hasObjects_false(self):
        self.assertEquals(hasObjects(brObjekti=0, poeni=self.points), 0)

    def test_hasObjects_true(self):
        self.assertEquals(hasObjects(brObjekti=3, poeni=self.points), sumPoints(points=self.points))


