import telebot
from telebot import types
import Catalog1
import Catalog2

# Вставь сюда свой токен бота
TOKEN = '7798015471:AAFOxQFIwuu4YoTZtY9Ke6d7NC0NGmxFuWI'
bot = telebot.TeleBot(TOKEN)

# Данные консультанта
CONSULTANT_USERNAME = '@ar_tem_Lee'
CONSULTANT_NAME = 'Артем ЛИ'

# Сайт магазина
STORE_URL = 'https://yourclothstore.com'

def send_main_menu(chat_id, username):
    # Используем HTML разметку
    welcome_text = f"👋 Приветствую @{username} в нашем магазине \"Cloth Store!\" 🛍️\n\nВыберите функцию ниже 👇"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👗 Каталог Одежды")
    btn2 = types.KeyboardButton("👟 Каталог Обуви")
    btn3 = types.KeyboardButton("💬 Связаться с консультантом")
    btn4 = types.KeyboardButton("🌐 Перейти на наш сайт")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)

    # Отправляем сообщение с HTML-разметкой
    bot.send_message(chat_id, welcome_text, reply_markup=markup, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    send_main_menu(message.chat.id, message.from_user.username)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    text = message.text
    username = message.from_user.username

    if text == "👗 Каталог Одежды":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back_btn = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add(back_btn)
        catalog_text = Catalog1.get_catalog()
        bot.send_message(message.chat.id, f"📄 <b>Каталог одежды:</b>\n{catalog_text}", parse_mode='HTML', reply_markup=markup)

    elif text == "👟 Каталог Обуви":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back_btn = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add(back_btn)
        catalog_text = Catalog2.get_catalog()
        bot.send_message(message.chat.id, f"📄 <b>Каталог обуви:</b>\n{catalog_text}", parse_mode='HTML', reply_markup=markup)

    elif text == "💬 Связаться с консультантом":
        consultant_info = f"📞 Наш консультант:\n👤 Имя: <b>{CONSULTANT_NAME}</b>\n🔗 Telegram: {CONSULTANT_USERNAME}"
        bot.send_message(message.chat.id, consultant_info, parse_mode='HTML')

    elif text == "🌐 Перейти на наш сайт":
        bot.send_message(message.chat.id, f"🛒 Посетите наш сайт: <a href='{STORE_URL}'>Нажмите здесь</a>", parse_mode='HTML', disable_web_page_preview=True)

    elif text == "🔙 Вернуться в главное меню":
        send_main_menu(message.chat.id, username)

    else:
        bot.send_message(message.chat.id, "❓ Пожалуйста, выберите одну из опций ниже.")

# Запуск бота
bot.polling(none_stop=True)