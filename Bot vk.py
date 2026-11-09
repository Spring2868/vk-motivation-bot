import os
from dotenv import load_dotenv
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
import schedule
import time
import threading


load_dotenv() # Загружает данные из файла .env
TOKEN = os.getenv('VK_TOKEN') # Читает токен в переменную безопасности

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


quotes = [ "«Лучший способ предсказать будущее — создать его.» — Питер Друкер",
    "«Ошибки — это доказательство того, что ты пытался.»",
    "«Сложные дороги часто приводят к прекрасным местам.»"
]

lifehacks = ["Правило 2 минут: если дело занимает меньше двух минут — сделайте его прямо сейчас.",
    "Чтобы сфокусироваться, используйте метод Помодоро: 25 минут работы, 5 минут отдыха."
]

stories = ["История Сэма: Он завалил 12 собеседований подряд, но на 13-й раз создал проект, который позже выкупил Google.",
    "История Джоан Роулинг: Её рукопись о Гарри Поттере отвергли 12 издательств."
]

users = set()


def send_message(user_id, text, keyboard=None):
    params = {
    'user_id': user_id,
    'message': text,
    'random_id': random.randint(1, 1000000)
    }
    if keyboard:
        params['keyboard'] = keyboard.get_keyboard()
    vk.messages.send(**params)


def create_keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Цитата дня', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Лайфхак', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Истории успеха', color=VkKeyboardColor.SECONDARY)
    return keyboard


def daily_broadcast():
    if not users:
        return

morning_message = f"Доброе утро! Время утренней мотивации:\n\n{random.choice(quotes)}"
for user_id in users:
        try:
            send_message(user_id, morning_message)
        except Exception as e:
            print(f"Не удалось отправить пользователю {user_id}: {e}")

def run_scheduler():
    schedule.every().day.at("09:00").do(daily_broadcast)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Запуск будильника в фоне
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

print("Бот ВКонтакте запущен и готов к работе без всяких прокси!")

# --- ГЛАВНЫЙ ЦИКЛ ОЖИДАНИЯ СООБЩЕНИЙ ---
for event in longpoll.listen():
    # Проверяем, что пришло именно НОВОЕ ТЕКСТОВОЕ сообщение от ПОЛЬЗОВАТЕЛЯ
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        text = event.text
        users.add(user_id) # Запоминаем человека для утренней рассылки
        
        # Логика ответов
        if text.lower() in ['привет', 'старт', 'начать']:
            send_message(user_id, "Привет! Я твой личный мотиватор.", create_keyboard())
            
        elif text == 'Цитата дня':
            send_message(user_id, random.choice(quotes))
            
        elif text == 'Лайфхак':
            send_message(user_id, random.choice(lifehacks))
            
        elif text == 'Истории успеха':
            send_message(user_id, random.choice(stories))
            
        else:
            send_message(user_id, "Используй кнопки меню, чтобы получить контент!", create_keyboard())

