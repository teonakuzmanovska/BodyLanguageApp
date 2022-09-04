from django.shortcuts import render, redirect

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
    # stavi user attr u gesture
    lectures = Gesture.objects.filter(read=True).count()
    context={"lectures": lectures}
    return render(request, "progress.html", context=context)


def body_parts(request):
    return render(request, "body_parts.html")


# def emotions(request):
#     return render(request, "emotions.html")


def context(request):
    return render(request, "context.html")


def bp_face(request):
    eyes = Gesture.objects.filter(category="eyes").all()
    context = {"bp_face": eyes}  # , "form": form_data
    return render(request, "bp_face.html", context=context)


def emotions(request):
    happiness = Gesture.objects.filter(meaning__meaning="happiness").all()
    sadness = Gesture.objects.filter(meaning__meaning="sadness").all()
    shame = Gesture.objects.filter(meaning__meaning="shame").all()
    guilt = Gesture.objects.filter(meaning__meaning="quilt").all()
    disgust = Gesture.objects.filter(meaning__meaning="disgust").all()
    anger = Gesture.objects.filter(meaning__meaning="anger").all()
    fear = Gesture.objects.filter(meaning__meaning="fear").all()

    context = {"happiness": happiness, "sadness": sadness, "shame": shame, "guilt": guilt, "disgust": disgust, "anger": anger, "fear": fear}
    return render(request, "emotions.html", context=context)

# zemi go toa pole i smeni, api-to da e povikano vo template


