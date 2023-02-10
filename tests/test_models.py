from django.test import TestCase
from BodyLanguage.models import *


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("test", "test@test.com", "Test123_")
        self.meaning = Meaning.objects.create(meaning='sadness')
        self.context = Context.objects.create(context='in_love')
        self.behaviour = Behaviour.objects.create(behaviour='lying')
        self.gesture = Gesture.objects.create(user=self.user, gesture='eye_gaze', category='face', male=True, female=True, adult=True, child=False)
        self.gesture.meaning.add(self.meaning)
        self.gesture.context.add(self.context)
        self.gesture.behaviour.add(self.behaviour)
        self.question = Question.objects.create(question='q1', op1='1', op2='2', op3='3', op4='4', ans='option1', category='face')
        self.results = Results.objects.create(category='face', points='5', user=self.user)

    def test_meaning(self):
        self.assertEquals(Meaning.str(self.meaning), 'sadness')

    def test_context(self):
        self.assertEquals(Context.str(self.context), 'in_love')

    def test_behaviour(self):
        self.assertEquals(Behaviour.str(self.behaviour), 'lying')

    def test_question(self):
        self.assertEquals(Question.str(self.question), 'q1')

    def test_results(self):
        self.assertEquals(Results.str(self.results), 'face')

    def test_gesture(self):
        self.assertEquals(Gesture.str(self.meaning), 'sadness')
