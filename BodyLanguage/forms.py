# from django.forms import forms, ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from BodyLanguage.models import *


# class ReadForm(ModelForm):
#
#     # i za ova ne sum bash sigurna, najchesto ne raboti
#     # dopolnitelno da se smeni attr 'read' na soodvetniot gesture
#     def __init__(self, *args, **kwargs):
#         super(ReadForm, self).__init__(*args, **kwargs)
#         for field in self.visible_fields():
#             print(field)
#             field.field.widget.attrs["class"] = "form-control"
#
#     class Meta:
#         model = Gesture
#         exclude = ("user",)

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

