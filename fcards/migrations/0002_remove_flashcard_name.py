# Generated by Django 3.1.3 on 2021-07-21 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='name',
        ),
    ]
