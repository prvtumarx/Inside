<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Электронный кошелек{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">Главная</a> | 
        <a href="/users/register/">Регистрация</a> |
        <a href="/users/login/">Вход</a>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
