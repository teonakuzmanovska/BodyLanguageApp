# Generated by Django 4.1 on 2022-08-27 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BodyLanguage', '0014_alter_meaning_meaning'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bodypartgesture',
            name='feeling',
        ),
    ]
