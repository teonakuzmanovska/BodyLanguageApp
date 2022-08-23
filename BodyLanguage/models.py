from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AppUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default=None)
    surname = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)


class BodyPartGesture(models.Model):
    gesture = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    feeling = models.CharField(max_length=50)
    male = models.BooleanField()
    female = models.BooleanField()
    adult = models.BooleanField()
    child = models.BooleanField()


class Emotion(models.Model):
    emotion = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    male = models.BooleanField()
    female = models.BooleanField()
    adult = models.BooleanField()
    child = models.BooleanField()


class ContextGesture(models.Model):
    gesture = models.CharField(max_length=50)
    in_love = models.BooleanField()
    at_work = models.BooleanField()
    image = models.ImageField(upload_to="images/")
    feeling = models.CharField(max_length=50)
    male = models.BooleanField()
    female = models.BooleanField()
    adult = models.BooleanField()
    child = models.BooleanField()


class Behaviour(models.Model):
    behaviour = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    male = models.BooleanField()
    female = models.BooleanField()
    adult = models.BooleanField()
    child = models.BooleanField()


class Read(models.Model):
    read = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    body_part_gesture = models.ForeignKey(BodyPartGesture, on_delete=models.CASCADE, default=False)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, default=False)
    context_gesture = models.ForeignKey(ContextGesture, on_delete=models.CASCADE, default=False)
    behaviour = models.ForeignKey(Behaviour, on_delete=models.CASCADE, default=False)


class TestResults(models.Model):
    # mislam deka nema potreba da se stavaat vo baza, na front end e dovolno, samo poenite ni se dovolni, kje se proveruva dali se tochni na frontend
    id = models.IntegerField(primary_key=True)
    points = models.IntegerField()
    taken = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # da se pristapi "taken", ako e true, da se smenat poenite
    # da se izrachunaat poenite na samiot frontend, i da ne se rachunaat duplo, da se prenesat na backend preku submit
    # da se dade prashanje dali saka retake, da se proveri prethoden score i da se apdejtiraat poenite


class Statistics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lectures = models.FloatField()
    quizzes = models.FloatField()
    # potrebni se matematiki za presmetuvanje progress. dobieni poeni od mozhni poeni za testovi, prochitani gestures od vkupen broj na gesture
