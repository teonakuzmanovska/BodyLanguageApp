from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def tips(request):
    return render(request, "tips.html")


def contact(request):
    return render(request, "contact.html")


def helphtml(request):
    return render(request, "help.html")