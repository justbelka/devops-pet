# Generated by Django 3.0.2 on 2022-04-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cybertest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='current_question',
            field=models.IntegerField(default=1, verbose_name='Текущий вопрос'),
        ),
    ]