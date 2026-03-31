![placeholder](https://github.com/DanielBash/alice-bot/blob/main/.github/github-banner.png?raw=true)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Stars](https://img.shields.io/github/stars/DanielBash/alice-bot)
[![.github/workflows/python-tests.yaml](https://github.com/DanielBash/alice-bot/actions/workflows/python-tests.yaml/badge.svg)](https://github.com/DanielBash/profile/actions/workflows/python-tests.yaml)
[![update-docker-image](https://github.com/DanielBash/alice-bot/actions/workflows/docker-deploy.yaml/badge.svg)](https://github.com/DanielBash/profile/actions/workflows/docker-deploy.yaml)

# Бот яндекс-алиса

> Это бот для яндекс-алисы

Он размещен здесь [here](https://hell-0.ru)!

## Локальная установка
### Вариант 1: Виртуаьлное окружение
1) Скачайте репозиторий
```bash
git clone https://github.com/DanielBash/alice-bot.git
cd alice-bot
```

2) Установите зависимости
```bash
pip install -r requirements.txt
```

3) Опционально измените .env для собсдвенной надстройки
```bash
echo "SECRET_KEY=secure-secret-key" > .env
```

4) Запустите скирпт <br/>

**Вариант 1.1**: Запустите скрипт для отладки
```bash
python main.py
```

**Вариант 1.2**: Запустите скрипт для продакшена
```bash
gunicorn --config gunicorn_config.py main:app
```

### Вариант 2: Docker-контейнер
1) Загрузите последнюю версию докер образа с сервера:
```bash
docker pull danielbashl/alice-bot:latest
```

2)  Запустите контейнер:
```bash
docker run -d -p 5000:8000 danielbashl/alice-bot:latest
```
