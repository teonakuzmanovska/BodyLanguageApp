from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AppUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


  # read, test results i statistics se vrzani so user-ot, trebaat foreign keys
class Read(models.Model):
    read = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BodyPartGesture(models.Model):
    gesture = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    feeling = models.CharField(max_length=50)
    male = models.BooleanField()
    female = models.BooleanField()
    adult = models.BooleanField()
    child = models.BooleanField()
    read = models.ForeignKey(Read, on_delete=models.CASCADE)


class Emotion(models.Model):
    emotion = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    male = models.BooleanField()
    female = models.BooleanField()
    adult = models.BooleanField()
    child = models.BooleanField()
    read = models.BooleanField()


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
    read = models.ForeignKey(Read, on_delete=models.CASCADE)


class Behaviour(models.Model):
    behaviour = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    male = models.BooleanField()
    female = models.BooleanField()
    adult = models.BooleanField()
    child = models.BooleanField()
    read = models.ForeignKey(Read, on_delete=models.CASCADE)


class TestResults(models.Model):
    # mislam deka nema potreba da se stavaat vo baza, na front end e dovolno, samo poenite ni se dovolni, kje se proveruva dali se tochni na frontend
    id = models.IntegerField()
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
