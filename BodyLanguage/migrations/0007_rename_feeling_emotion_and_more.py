# Generated by Django 4.1 on 2022-08-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BodyLanguage', '0006_feeling_delete_emotion_alter_bodypartgesture_feeling'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feeling',
            new_name='Emotion',
        ),
        migrations.RenameField(
            model_name='emotion',
            old_name='feeling',
            new_name='emotion',
        ),
        migrations.AlterField(
            model_name='bodypartgesture',
            name='feeling',
            field=models.CharField(max_length=50),
        ),
    ]
