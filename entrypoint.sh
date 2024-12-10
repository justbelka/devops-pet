#!/bin/bash
sleep 10
echo "Выполнение миграций..."
python /app/manage.py migrate --noinput

echo "Создание нового суперпользователя..."
echo "from django.contrib.auth.models import User;
import os;
username = os.environ.get('DJ_SUPERUSER');
email = os.environ.get('DJ_SUPERMAIL');
password = os.environ.get('DJ_SUPERPASS');
if username and email and password and not User.objects.filter(username=username).exists():\
      User.objects.create_superuser(username, email, password)" | python /app/manage.py shell

echo "Создание базовой модели теста cybertest..."
echo "from cybertest.models import Test, Question, Answer;
if not Test.objects.filter(name='cybersecurity').exists():
      test = Test.objects.create(name='cybersecurity', questions_count=10);

      q1 = Question.objects.create(test=test, text='Начнём с простого. Какой из представленных паролей является наиболее безопасным?', points=10, description='Чем сложнее и непонятнее пароль, тем меньше шанс, что его взломают. Можешь продолжать');
      Answer.objects.create(question=q1, text='123456', is_right=False);
      Answer.objects.create(question=q1, text='дракон', is_right=False);
      Answer.objects.create(question=q1, text='Bi%DuIn!So57Lo', is_right=True);
      Answer.objects.create(question=q1, text='iLoVeYou', is_right=False);
      Answer.objects.create(question=q1, text='D00R8377', is_right=False);
      Answer.objects.create(question=q1, text='1q2w3e4r', is_right=False);
      
      q2 = Question.objects.create(test=test, text='Что из перечисленного является самой большой угрозой безопасности организации?', points=10, description='Этот вопрос больше теоретический. Тем не менее самой большой угрозой безопасности являются люди внутри организации, ведь человеческий фактор никто не отменял, а легче всего влиять именно на людей внутри компании');
      Answer.objects.create(question=q2, text='Люди внутри организации', is_right=True);
      Answer.objects.create(question=q2, text='Люди за пределами организации', is_right=False);
      
      q3 = Question.objects.create(test=test, text='Как в кругах кибербезопасности называется "атака на человека"?', points=10, description='Атака на человека или социальная инженерия - это совокупность психологических и социологических приёмов, методов и технологий, которые позволяют получить конфиденциальную информацию. Таким образом, хакеры стали не только мошенниками, но и профессиональными психологами. Можешь продолжать');
      Answer.objects.create(question=q3, text='Социальная инженерия', is_right=True);
      Answer.objects.create(question=q3, text='Фишинг', is_right=False);
      Answer.objects.create(question=q3, text='Скимминг', is_right=False);
      Answer.objects.create(question=q3, text='Скам', is_right=False);
      
      q4 = Question.objects.create(test=test, text='Какие криптографические механизмы использует протокол "https"?', points=10, description='Правильный ответ - SSL/TLS. Использование таких механизмов позволяет добиться результатов, когда запрос от клиента может быть прочтён только на стороне сервера и никак не может быть перехвачен третьей стороной где-то посередине. Можешь продолжать');
      Answer.objects.create(question=q4, text='SSH / KFC', is_right=False);
      Answer.objects.create(question=q4, text='SSH / TLS', is_right=False);
      Answer.objects.create(question=q4, text='TLS / SMS', is_right=False);
      Answer.objects.create(question=q4, text='SSL / TLS', is_right=True);
      Answer.objects.create(question=q4, text='KMS / GPS', is_right=False);
      
      q5 = Question.objects.create(test=test, text='Это база :) Представь себе ситуацию: вчера у тебя был корпоратив. С утра на электронную почту пришло письмо вот с таким содержанием: "Привет! Классно вчера потусили, я тут прикрепил видео где ты назвал начальника дебилом. Ржака полная" также прикреплён архив. Что ты сделаешь?', points=10, description='Думаю здесь мои комментарии излишни. Можешь продолжать');
      Answer.objects.create(question=q5, text='Скачаю архив и посмотрю видео', is_right=False);
      Answer.objects.create(question=q5, text='Проигнорирую, так как это может быть попыткой заражения', is_right=True);
      Answer.objects.create(question=q5, text='Напишу заявление об уходе', is_right=False);
      Answer.objects.create(question=q5, text='Пойду извинюсь перед начальником', is_right=False);
      
      q6 = Question.objects.create(test=test, text='Анализ исходящего трафика от гаджетов в квартире раскрыл привычки ее обитателей: когда дети ложатся спать и что они смотрят по телевизору, когда родители на работе', points=10, description='Такой эксперимент провела журналистка издания Gizmodo. На два месяца она превратила свою квартиру в умный дом. Все устройства — кофеварки, зубные щетки, пылесосы и так далее — передавали данные компаниям-производителям несколько раз в день, а, например, телевизор передавал данные о привычках семьи сторонним компаниям. Можешь продолжать');
      Answer.objects.create(question=q6, text='Правда', is_right=True);
      Answer.objects.create(question=q6, text='Ложь', is_right=False);
      
      q7 = Question.objects.create(test=test, text='Серийный киллер анонимно купил оружие в интернете при помощи биткоинов. Позже это стало доказательством его вины в суде', points=10, description='Биткоин не анонимен, как принято считать. Реестр со всеми транзакциями публичен: зная адрес вашего кошелька, можно увидеть все ваши переводы. Можешь продолжать');
      Answer.objects.create(question=q7, text='Правда', is_right=True);
      Answer.objects.create(question=q7, text='Ложь', is_right=False);
      
      q8 = Question.objects.create(test=test, text='Парень разговаривал со своим другом о поломке наушников по телефону. Зайдя в Facebook он увидел рекламу наушников, значит ли это, что Facebook подслушивает своих пользователей?', points=10, description='Facebook неоднократно подозревали в прослушке разговоров для таргетирования рекламы (технически это возможно, у приложения есть доступ к микрофону смартфона). Компании даже пришлось выпустить официальное опровержение. Независимые проверки подтвердили — приложение Facebook не анализирует разговоры пользователей. Можешь продолжать');
      Answer.objects.create(question=q8, text='Да', is_right=False);
      Answer.objects.create(question=q8, text='Нет', is_right=True);
      
      q9 = Question.objects.create(test=test, text='Некий пользователь Z опасаясь взлома защитил свою почту двухфакторной авторизацией через SMS. Но его все равно взломали', points=10, description='Хакеры и спецслужбы могут перехватить SMS с помощью уязвимости в SS7 — системе служебных протоколов, с помощью которых телеком-операторы управляют телефонными сетями. Получив доступ к SMS пользователя, можно войти в его почту, сбросив пароль. Можешь продолжать');
      Answer.objects.create(question=q9, text='Такое возможно', is_right=True);
      Answer.objects.create(question=q9, text='Такое невозможно', is_right=False);
      
      q10 = Question.objects.create(test=test, text='Пользователь J купил тостер, а злоумышленники с его помощью накручивали лайки в социальных сетях', points=10, description='Канадцы столкнулись с нетипичным ботнетом Linux/Moose, который состоит из зараженных устройств интернета вещей и используется для накруток лайков и фолловеров в соцсетях. Подобные ботнеты используются для DDoS-атак, рассылки спама или открутки баннеров. А в данном случае злоумышленники зарабатывали на раскрутке инстаграм-аккаунтов. Можешь продолжать');
      Answer.objects.create(question=q10, text='Такое возможно', is_right=True);
      Answer.objects.create(question=q10, text='Такое невозможно', is_right=False);
" | python /app/manage.py shell

echo "Запуск сервера..."
exec "$@"
