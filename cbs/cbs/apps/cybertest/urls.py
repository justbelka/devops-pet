from django.urls import path
from . import views

app_name = 'cybertest'

urlpatterns = [
    path('', views.Main.as_view(), name='main'),  # домашняя страница
    path('about', views.About.as_view(), name='about'),  # страница "о нас"
    path('test/<str:name>/', views.TestDetail.as_view(), name='test_page'),  # обзорная страница теста
    path('test/<str:test_name>/questions/', views.questions, name='questions'),  # страница вопросов теста
    path('test/<str:test_name>/questions/<int:question_number>/', views.question, name='question'),  # страница вопроса
    path('test/<str:test_name>/questions/<int:question_number>/check/', views.check, name='check'),  # проверка
    path('test/<str:name>/complete/', views.Complete.as_view(), name='complete'),
    path('signup', views.signup, name='signup'),  # регистрация
    path('login', views.Login.as_view(), name='login'),  # авторизация
    path('logout', views.logout, name='logout'),  # выход из пользователя
    path('profile', views.profile, name='profile'),  # страница профиля
]
