# Generated by Django 3.0.2 on 2022-04-14 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cybertest', '0006_auto_20220408_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testmarks', to=settings.AUTH_USER_MODEL, verbose_name='Студент')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testmarks', to='cybertest.Question', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Отметка об оконачнии',
                'verbose_name_plural': 'Отметки об окончании',
            },
        ),
    ]
