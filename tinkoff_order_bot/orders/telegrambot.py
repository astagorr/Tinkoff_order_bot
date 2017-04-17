import telebot
import time
from telebot import types

BOT_TOKEN = "345392316:AAGmMZBBY8pvMM9KpeOJoeoNC-FNVvTvYQI"
DELAY = 10
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types = ["text"], commands = ['start'])
def start(message, order = 0):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text = answer, callback_data = answer) for answer in ["Да", "Нет"]])
    msg = bot.send_message(message.chat.id, "Заказ номер %d. Подтвердить?" % order, reply_markup = keyboard)

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Ваш запрос обработан")
    print(call)

if __name__ == '__main__':
     bot.polling(none_stop=True)
