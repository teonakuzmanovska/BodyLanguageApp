from django.forms import forms, ModelForm

from BodyLanguage.models import *


class ReadForm(ModelForm):

    # i za ova ne sum bash sigurna, najchesto ne raboti
    # dopolnitelno da se smeni attr 'read' na soodvetniot gesture
    def __init__(self, *args, **kwargs):
        super(ReadForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Gesture
        exclude = ("user",)
