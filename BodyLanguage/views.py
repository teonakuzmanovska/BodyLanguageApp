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
    return render(request, "progress.html")


def body_parts(request):
    return render(request, "body_parts.html")


def emotions(request):
    return render(request, "emotions.html")


def context(request):
    return render(request, "context.html")


def bp_face(request):
    # za ova ich ne sum sigurna
    # if request.method == "post":
    #     form_data = Statistics(data=request.POST, files=request.FILES)
    #     if form_data.is_valid():
    #         statistics = form_data.save(commit=False)
    #         statistics.user = request.user
    #         statistics.lectures = form_data.cleaned_data['lectures']
    #         statistics.save()
    #         return redirect("bp_face")

    queryset = BodyPartGesture.objects.filter(category="eyes").all()
    context = {"bp_face": queryset}  # , "form": form_data
    return render(request, "bp_face.html", context=context)


