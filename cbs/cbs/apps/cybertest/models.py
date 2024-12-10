from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название теста')
    questions_count = models.IntegerField(verbose_name='Количество вопросов')
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def get_absolute_points(self):
        questions = Question.objects.filter(test=self.id)
        summa = 0
        for question in questions:
            summa += question.points
        return int(summa)

    def __str__(self):
        return self.name


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест')
    text = models.TextField(verbose_name='Текст вопроса')
    points = models.FloatField(default=1, verbose_name='Количество очков за правильный ответ')
    description = models.TextField(verbose_name='Описание вопроса', blank=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_right = models.BooleanField()

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'    

    def __str__(self):
        return self.text

class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест')
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Студент", related_name='results')
    current_question = models.IntegerField(verbose_name='Текущий вопрос', default=1)
    date_of_passage = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата прохождения")
    points = models.IntegerField(default=0)
    Rating =models.FloatField(verbose_name="Проценты", default=0)
    completed = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def get_absolute_result(self):
        return int((self.points / self.test.get_absolute_points()) * 100)

class Mark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Студент", related_name='marks')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос', related_name='marks')
    mark = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Отметка'
        verbose_name_plural = 'Отметки'

class TestMark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Студент", related_name='testmarks')
    test = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Тест', related_name='testmarks')
    completed = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Отметка об оконачнии'
        verbose_name_plural = 'Отметки об окончании'
