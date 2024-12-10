# Generated by Django 3.0.2 on 2022-04-08 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cybertest', '0005_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание вопроса'),
        ),
        migrations.AlterField(
            model_name='result',
            name='Rating',
            field=models.FloatField(default=0, verbose_name='Проценты'),
        ),
    ]
