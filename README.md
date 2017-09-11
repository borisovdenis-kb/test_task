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

| URL                          | CREDITORG | PARTNER    | SUPERUSER |
|:-----------------------------|:---------:|:----------:|:---------:|
| /creditorg/claims/           |    YES    |     NO     |    YES    |
| /creditorg/claims/{id}/      |    YES    |     NO     |    YES    |
| /creditorg/claims/           |    NO     |     YES    |    YES    |
| /creditorg/claims/{id}/send/ |    NO     |     YES    |    YES    |
| /creditorg/claims/{id}/      |    NO     |     NO     |    YES    |
| /creditorg/claims/{id}/      |    NO     |     NO     |    YES    |
| /creditorg/offers/           |    YES    |     NO     |    YES    |
| /creditorg/offers/{id}/      |    YES    |     NO     |    YES    |
| /creditorg/offers/           |    YES    |     NO     |    YES    |
| /creditorg/offers/{id}/      |    YES    |     NO     |    YES    |
| /creditorg/offers/{id}/      |    NO     |     NO     |    YES    |
| /creditorg/worksheets/       |    NO     |     YES    |    YES    |
| /creditorg/worksheets{id}/   |    NO     |     YES    |    YES    |
| /creditorg/worksheets/       |    NO     |     YES    |    YES    |
| /creditorg/worksheets/{id}/  |    NO     |     NO     |    YES    |
| /creditorg/worksheets/{id}/  |    NO     |     NO     |    YES    |

