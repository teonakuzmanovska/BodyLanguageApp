from django.shortcuts import render, redirect

# Create your views here.
from BodyLanguage.forms import UserRegistrationForm
from BodyLanguage.models import *
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


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

    if request.user.is_authenticated:
        return render(request, "quizzes.html")
    else:
        return redirect("/login/")


def progress(request):
    # stavi user attr u gesture
    # lectures = Gesture.objects.filter(read=True).count()
    # context={"lectures": lectures}
    if request.user.is_authenticated:
        return render(request, "progress.html")
    else:
        return redirect("/login/")


def body_parts(request):
    eyes = Gesture.objects.filter(category="eyes").all()
    context = {"eyes": eyes}  # , "form": form_data
    return render(request, "body_parts.html", context=context)


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


def context(request):
    return render(request, "context.html")

# zemi go toa pole i smeni, api-to da e povikano vo template


