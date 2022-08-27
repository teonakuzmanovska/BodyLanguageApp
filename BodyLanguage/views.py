from django.shortcuts import render

# Create your views here.
from BodyLanguage.models import *


def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def helphtml(request):
    return render(request, "help.html")


def tips(request):
    return render(request, "tips.html")


def articles(request):
    return render(request, "articles.html")


def categories(request):
    return render(request, "categories.html")


def quizzes(request):
    return render(request, "quizzes.html")


def progress(request):
    return render(request, "progress.html")


def body_parts(request):
    return render(request, "body_parts.html")


def emotions(request):
    return render(request, "emotions.html")


def context(request):
    return render(request, "context.html")


def bp_face(request):
    queryset = BodyPartGesture.objects.filter(category="eyes").all()
    context = {"bp_face": queryset}
    return render(request, "bp_face.html", context=context)

