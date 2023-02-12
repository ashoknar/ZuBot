import os
from run_inference import get_reply
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    reply_message = get_reply(message.text)
    reply_message = reply_message.replace("[me]", "")
    bot.send_message(message.chat.id, reply_message)


print("bot polling")
bot.infinity_polling()
