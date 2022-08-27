# Generated by Django 4.1 on 2022-08-27 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Behaviour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('behaviour', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('male', models.BooleanField()),
                ('female', models.BooleanField()),
                ('adult', models.BooleanField()),
                ('child', models.BooleanField()),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContextGesture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gesture', models.CharField(max_length=50)),
                ('in_love', models.BooleanField()),
                ('at_work', models.BooleanField()),
                ('image', models.ImageField(upload_to='images/')),
                ('feeling', models.CharField(max_length=50)),
                ('male', models.BooleanField()),
                ('female', models.BooleanField()),
                ('adult', models.BooleanField()),
                ('child', models.BooleanField()),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meaning', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestResults',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('points', models.IntegerField()),
                ('taken', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lectures', models.FloatField()),
                ('quizzes', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BodyPartGesture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gesture', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('male', models.BooleanField()),
                ('female', models.BooleanField()),
                ('adult', models.BooleanField()),
                ('child', models.BooleanField()),
                ('read', models.BooleanField(default=False)),
                ('meaning', models.ManyToManyField(to='BodyLanguage.meaning')),
            ],
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('surname', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
