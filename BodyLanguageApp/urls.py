"""BodyLanguageApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from BodyLanguage.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('contact/', contact, name="contact"),
    path('help/', helphtml, name="help"),
    path('tips/', tips, name="tips"),
    path('articles/', articles, name="articles"),
    path('categories/', categories, name="categories"),
    path('quizzes/', quizzes, name="quizzes"),
    path('progress/', progress, name="progress"),
    path('body_parts/', body_parts, name="body_parts"),
    path('emotions/', emotions, name="emotions"),
    path('context/', context, name="context"),
    path('bp_face/', bp_face, name="bp_face")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
