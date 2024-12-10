from re import template
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
from .forms import SignUpForm
from .utils import *


class Main(RenderMixin, View):
    template = 'cybertest/index.html'

class About(RenderMixin, View):
    template = 'cybertest/about.html'

class TestDetail(ObjectDetailMixin, View):
    model = Test
    template = 'cybertest/test_page.html'


class Complete(View):
    def get(self, request, name):
        test = get_object_or_404(Test, name=name)
        return render(request, 'cybertest/sure/complete.html', context={'test': test})
    def post(self, request, name):
        test = get_object_or_404(Test, name=name)
        result = Result.objects.get_or_create(test=test, student=request.user)[0]
        result.completed = True
        result.save()
        return redirect(reverse("cybertest:profile"))

def question(request, test_name, question_number):
    question = get_object_or_404(Question, id=question_number)
    answers = Answer.objects.filter(question=question_number)
    context = {
        'question': question,
        'answers': answers
    }
    return render(request, 'cybertest/question.html', context=context)

def check(request, test_name, question_number):
    if request.method == 'POST':
        text = request.POST['flexRadioDefault']
        mark = Mark.objects.get(student=request.user.id, question=question_number)
        answer = Answer.objects.get(id=text)
        result = Result.objects.get_or_create(test=Test.objects.get(name=test_name), student=request.user)[0]
        question = Question.objects.get(id=question_number)
        points = question.points
        context = {'question': question, 'completed': result.completed}
        if answer.is_right and not mark.mark and not result.completed:
            mark.mark = True
            mark.save()
            result.points += points
            result.save()
            context['right'] = True
        else:
            mark.mark = True
            mark.save()
            context['right'] = False
        return render(request, 'cybertest/result.html', context=context)
        

def questions(request, test_name):
    test = get_object_or_404(Test, name=test_name)
    questions = Question.objects.filter(test=test.id)
    result = Result.objects.get_or_create(test=test, student=request.user)[0]
    new_questions = []
    for question in questions:
        try: mark = Mark.objects.get(student=request.user.id, question=question.id)
        except: mark = Mark.objects.create(student=request.user, question=question)
        new_questions.append([question, mark])
    context = {
        'questions': new_questions,
        'test': test,
        'completed': result.completed
    }
    return render(request, 'cybertest/questions.html', context=context)

# Users part

def profile(request):
    if request.user.is_authenticated:
        results = Result.objects.filter(student=request.user.id).order_by('-id')
        context = {'results': results}
    else:
        context = {}
    return render(request, 'cybertest/profile.html', context=context)

def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        context = {
            'form': form,
            'username': False,
            'password': False
        }
        return render(request, 'cybertest/signup.html', context=context)
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(reverse("cybertest:profile"))
        errors = form.errors.as_data()
        context = {'form': form}
        try: context['username'] = errors['username']
        except: context['username'] = False
        try: context['password'] = errors['password2']
        except: context['password'] = False
        return render(request, 'cybertest/signup.html', context=context)       

class Login(View):
    def get(self, request):
        context = {'error': False}
        return render(request, 'cybertest/login.html', context=context)
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect(reverse("cybertest:profile"))
        else:
            context = {'error': True}
            return render(request, 'cybertest/login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect(reverse("cybertest:main"))
