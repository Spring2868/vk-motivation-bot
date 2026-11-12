# VK Motivation Bot

Чат-бот для сообщества ВКонтакте на python, предназначенный для автоматической отправки мотивационных цитат, советов и интерактивного взаимодействия с пользователями через клавиатуру сообщества.

## Основной функционал
* **Автоматические ответы:** реакция на текстовые команды и нажатия кнопок в личных сообщениях сообщества.
* **Интерактивная клавиатура (VK Keyboard):** удобное меню выбора категорий сообщений для пользователя.
* **Безопасность конфигурации:** токен доступа и чувствительные данные вынесены из публичного кода (настроен `.gitignore`).

## Стек технологий
* **Язык:** python
* **Библиотеки:** `vk_api` (работа с Long Poll API ВКонтакте)

## Демонстрация работы

<img width="676" height="539" alt="image" src="https://github.com/user-attachments/assets/b61dcbf7-5fff-41f8-8d02-d48da43f9a73" />

<img width="693" height="410" alt="image" src="https://github.com/user-attachments/assets/520bfcdd-98e6-487d-9dae-afc32df625c7" />

<img width="667" height="582" alt="image" src="https://github.com/user-attachments/assets/755ef5fa-a106-40bb-b0a9-a3611833636f" />







## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com
   cd vk-motivation-bot
   ```

2. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Укажите токен вашего сообщества ВКонтакте и запустите скрипт:
   ```bash
   python "Bot vk.py"
   ```
