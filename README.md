# **Template Telegram Bot**

Template Telegram Bot - готовый шаблон для телеграм бота на python.

### Установка:
1. Клонировать репозиторый и зайти в папку c ботом

```
git clone https://github.com/Gamafoot/TemplateTelegramBot.git

cd TemplateTelegramBot
```

2. Создать виртуальное окружение `python3 -m venv venv`

3. Активировать виртуальное окружение:

```
Windows: & .\venv\Scripts\Activate.ps1
Mac/Linux: . ./venv/bin/activate
```

4. Установите библиотеку `aiogram` для работы с шаблоном `pip install aiogram`

5. В файле `config.py` назначте токен бота:

```python
TOKEN = 'ваш токен'
```

6. Запустите бота `python3 run.py`