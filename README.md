# test_task
### Для начала работы нужно выполнить следующие действия:
- Установить все необходимые для работы сервиса библиотеки. Для этого в корне проекта выполнить следующую команду.

  `pip install -r requirements.txt`

- Создать таблицы в базе данных. Данные для подключения к базе хранятся в .env. 
  Соответвенно настраивать подключение нужно именно в этом файле.

  `python manage.py makemigrations`
  `python manage.py migrate`
  
- После успешного создания таблиц нужно создать группы пользователей и наполнить их соответсвующими правами. 
  Для этого нужно выполнить скрипт **/extra/groups_creation.py**  

**После того как все шаги пройдены можно начать тестировать сервис.**

**Для этого нужно зайти на http://127.0.0.1:8000**

### Таблица прав пользователей.

| URL                          | METHOD | CREDITORG | PARTNER    | SUPERUSER |
|:-----------------------------|:------:|:---------:|:----------:|:---------:|
| /creditorg/claims/           |GET     |    YES    |     NO     |    YES    |
| /creditorg/claims/{id}/      |GET     |    YES    |     NO     |    YES    |
| /creditorg/claims/           |POST    |    NO     |     YES    |    YES    |
| /creditorg/claims/{id}/send/ |POST    |    NO     |     YES    |    YES    |
| /creditorg/claims/{id}/      |PUT     |    NO     |     NO     |    YES    |
| /creditorg/claims/{id}/      |DELETE  |    NO     |     NO     |    YES    |
| /creditorg/offers/           |GET     |    YES    |     NO     |    YES    |
| /creditorg/offers/{id}/      |GET     |    YES    |     NO     |    YES    |
| /creditorg/offers/           |POST    |    YES    |     NO     |    YES    |
| /creditorg/offers/{id}/      |PUT     |    YES    |     NO     |    YES    |
| /creditorg/offers/{id}/      |DELETE  |    NO     |     NO     |    YES    |
| /creditorg/worksheets/       |GET     |    NO     |     YES    |    YES    |
| /creditorg/worksheets{id}/   |GET     |    NO     |     YES    |    YES    |
| /creditorg/worksheets/       |POST    |    NO     |     YES    |    YES    |
| /creditorg/worksheets/{id}/  |PUT     |    NO     |     NO     |    YES    |
| /creditorg/worksheets/{id}/  |DELETE  |    NO     |     NO     |    YES    |

