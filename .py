import os
import telebot

bot=telebot.TeleBot("API Key Here")

@bot.message_handler(commands=["start"])
def send welcome(message):
  bot.reply_to(message,"Hello")
  
@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message, "hi")

bot.polling()  
