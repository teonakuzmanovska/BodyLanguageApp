from django.test import TestCase
from BodyLanguage.forms import UserRegistrationForm


class TestUserRegistrationForm(TestCase):
    def test_user_registration_form_valid_data(self):
        form = UserRegistrationForm(data={
            'username': 'test',
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@test.com',
            'password1': 'Test123_',
            'password2': 'Test123_'
        })

        self.assertTrue(form.is_valid())

    def test_user_registration_form_invalid_data(self):
        form = UserRegistrationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)
