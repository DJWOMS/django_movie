<p align="center">
    <a href="https://djangochannel.com" target="_blank" rel="noopener noreferrer">
        <img width="100" src="logo.png" title="djangoschool">
    </a>
</p>

<h2 align="center">Django Movie</h2>

[Сайт](https://djwoms.ru)

[Канал YouTube](https://www.youtube.com/channel/UC_hPYclmFCIENpMUHpPY8FQ?view_as=subscriber)

Кинобиблиотека на Django 3.

Проект написан в рамках обучающего курса по Django 3 на [youtube](https://youtube.com/playlist?list=PLF-NY6ldwAWrb6nQcPL21XX_-AmivFAYq).

- Категории
- Жанры
- Фильмы
- Кадры из фильма
- Режиссеры\Актеры
- Звезды рейтинга
- Отзывы
- Фильтры

# Django Movie

## Описание
Django Movie — это полнофункциональная кинобиблиотека, реализованная на Django 3.0. Проект создан в рамках обучающего курса и демонстрирует современные подходы к разработке веб-приложений на Django.

## Основные функции
- Категории и жанры фильмов
- Управление фильмами, актёрами и режиссёрами
- Кадры из фильмов
- Рейтинги (звёзды) и отзывы пользователей
- Фильтрация и поиск фильмов
- Мультиязычность (русский/английский)
- CKEditor для редактирования контента
- Подписка по email (модуль обратной связи)
- Интеграция с reCAPTCHA v3
- Аутентификация через django-allauth (в т.ч. через VK)
- Адаптивный интерфейс

## Стек
- Django 3.0.3
- django-allauth
- django-ckeditor
- django-modeltranslation
- django-recaptcha3
- Pillow
- requests, requests-oauthlib
- и др. (см. `requirements.txt`)

## Установка
1. **Создайте виртуальное окружение:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # или venv\Scripts\activate для Windows
    ```

2. **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Выполните миграции:**
    ```bash
    python manage.py migrate
    ```

4. **Создайте суперпользователя:**
    ```bash
    python manage.py createsuperuser
    ```

## Запуск
```bash
python manage.py runserver
```

## Структура проекта
- `django_movie/` — основной конфиг и настройки проекта
- `movies/` — приложение для управления фильмами, жанрами, актёрами, отзывами и рейтингами
- `contact/` — приложение для email-подписки и обратной связи
- `templates/` — шаблоны сайта
- `static/` — статические файлы (CSS, JS, изображения)
- `media/` — загружаемые пользователями файлы (постеры, кадры и т.д.)
- `config/` — конфигурация для деплоя (gunicorn, supervisor)
- `logs/` — логи приложения

## Переменные окружения
- `SECRET_KEY` — секретный ключ Django
- `DEBUG` — режим отладки (True/False)
- `ALLOWED_HOSTS` — список разрешенных хостов

## Запуск тестов
```bash
python manage.py test
```

## Важные нюансы
- Проект поддерживает мультиязычность (русский, английский). Файлы переводов хранятся в папке `locale/`.
- Для деплоя используются gunicorn и supervisor. Примеры конфигураций находятся в папке `config/`.
- CI/CD настроен через Travis CI. Конфигурация находится в файле `.travis.yml`.

