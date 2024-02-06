# The name of project: last_operations

Логика работы 
Проект представляет собой новую функцию для личного кабинета клиента банка. При нажатии клавиши Enter пользователю
выводятся последние 5 успешных операций клиента. Программа считывает и собирает данные с отдельной библиотеки формата
json, сортирует их по дате в порядке убывания, шифрует номер счета (карты) отправителя и номер счета (карты) получателя,
и далее выводит все на пользовательский экран, где сверху - самые последние успешные транзакции. На экран выводятся: 
- дата совершения транзакции;
- назначение платежа;
- Номер счета отправителя или имя карты + номер счета отправителя
- Счет получателя 
- Баланс счета клиента.

Функции и методы проекта:
- get_operations - считывает данные с библиотеки json и кладет их в отдельный список python.
- get_sorted_operations - запускает цикл по каждой транзакции в списке, отсеивает отмененные транзакции, а также 
транзакции без даты. Далее сортирует оставшиеся транзакции по дате в порядке убывания и осталвяет последние 5.
- check_sender - Проверяет, есть ли отправитель у транзакции в списке. Если его нет, возвращает "Unknown", если 
есть, проверяет первое слово отправителя, если оно равно слову "Счет", то вызывается следующая функция encode_account, 
которая зашифрует номер счета, а если первое слово - имя карты - вызывается функция encode_card, которая зашифрует номер
карты. 
- print_date - принимает дату, сверяет ее с существующей, приводит к визуально понятному виду и возвращает ее. Либо
возвращает ошибку формата даты, если поступит неправильное значение. 

Проект состоит из двух веток Git. В ветке main лежит стабильная версия проекта, а в ветке develop велась разработка. 
Разработка новых функций проекта должна вестись в локально созданных других ветках, добавление новых функций должно
осуществляться через ветку develop. 
Разработка велась в виртуальном окружении venv. Список установленных для окружения пакетов и их версий:

- certifi==2024.2.2
- charset-normalizer==3.3.2
- colorama==0.4.6
- coverage==7.4.1
- idna==3.6
- iniconfig==2.0.0
- packaging==23.2
- pluggy==1.4.0
- pytest==8.0.0
- requests==2.31.0
- urllib3==2.2.0
- Python==3.12.0
