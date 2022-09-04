from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AppUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default=None)
    surname = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)


class Meaning(models.Model):
    meaning = models.CharField(max_length=50)

    def str(self):
        return str(self.meaning)


class Context(models.Model):
    context = models.CharField(max_length=50)

    def str(self):
        return str(self.context)


class Behaviour(models.Model):
    behaviour = models.CharField(max_length=50)

    def str(self):
        return str(self.behaviour)


class Gesture(models.Model):
    # stavi user attr
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gesture = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    meaning = models.ManyToManyField(Meaning)  # meaning of gesture
    context = models.ManyToManyField(Context, blank=True)  # optional context
    behaviour = models.ManyToManyField(Behaviour, blank=True)  # optional behaviour
    male = models.BooleanField()
    female = models.BooleanField()
    adult = models.BooleanField()
    child = models.BooleanField()
    # read = models.BooleanField(default=False) nema da imame read, samo kvizovi

    def str(self):
        return str(self.meaning)


# class ContextGesture(models.Model):
#     gesture = models.CharField(max_length=50)
#     in_love = models.BooleanField()
#     at_work = models.BooleanField()
#     image = models.ImageField(upload_to="images/")
#     feeling = models.CharField(max_length=50)
#     male = models.BooleanField()
#     female = models.BooleanField()
#     adult = models.BooleanField()
#     child = models.BooleanField()
#     read = models.BooleanField(default=False)


# class Behaviour(models.Model):
#     behaviour = models.CharField(max_length=50)
#     image = models.ImageField(upload_to="images/")
#     male = models.BooleanField()
#     female = models.BooleanField()
#     adult = models.BooleanField()
#     child = models.BooleanField()
#     read = models.BooleanField(default=False)


# class TestResults(models.Model):
#     # mislam deka nema potreba da se stavaat vo baza, na front end e dovolno, samo poenite ni se dovolni, kje se proveruva dali se tochni na frontend
#     points = models.IntegerField()
#     taken = models.BooleanField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

    # da se pristapi "taken", ako e true, da se smenat poenite
    # da se izrachunaat poenite na samiot frontend, i da ne se rachunaat duplo, da se prenesat na backend preku submit
    # da se dade prashanje dali saka retake, da se proveri prethoden score i da se apdejtiraat poenite


# ova nema ni da ni treba na kraj izgleda, kje treba samo da staime user attr u gesture model
# class Statistics(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     lectures = models.FloatField()
#     quizzes = models.FloatField()
#     # potrebni se matematiki za presmetuvanje progress. dobieni poeni od mozhni poeni za testovi, prochitani gestures od vkupen broj na gesture

