# from django.forms import forms
#
# from BodyLanguage.models import *
#
#
# class StatisticsForm(forms.ModelForm):
#     # i za ova ne sum bash sigurna, najchesto ne raboti
#     def __init__(self, *args, **kwargs):
#         super(StatisticsForm, self).__init__(*args, **kwargs)
#         for field in self.visible_fields():
#             print(field)
#             field.field.widget.attrs["class"] = "form-control"
#
#     class Meta:
#         model = Statistics
#         exclude = ("user",)
