# -*- coding: utf-8 -*-
import redis
import os
import telebot
import math
import random
import threading
from telebot import types
from emoji import emojize
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
groups=[]
stopp=0
admins=[441399484, 512006137]

from telethon import TelegramClient, events, sync
api_id=os.environ['api_id']
api_hash=os.environ['api_hash']
client=TelegramClient('sname', api_id, api_hash, '+79254704968')
client.start()

def spamon(message, group):
    global stopp
    while stopp!=1:
        msg=bot.send_message(group, message)
        try:
            bot.pin_chat_message(msg.chat.id, msg.message_id)
        except:
            pass
    
    bot.send_message(group, 'Спам остановлен ебать')
    
@bot.message_handler(commands=['stop'])
def stopppp(m):
    if m.from_user.id in admins:
        global stopp
        stopp=1
        bot.send_message(m.chat.id, 'Остановил спам во всех чатах ебать')
        
@bot.message_handler(commands=['start'])
def stopppp(m):
    if m.from_user.id in admins:
        global stopp
        stopp=0
        bot.send_message(m.chat.id, 'Разрешил спам во всех чатах ебать')
    
@bot.message_handler(commands=['spam'])
def spam(m):
    try:
        msg=m.text.split('/spam')[1]
        spamon(msg, m.chat.id)
    except:
        bot.send_message(m.chat.id, 'Ты долбоеб ебаный')
    
    
@client.message_handler(content_types=['text'])
def tttttc(m):
    client.send_message('@Loshadkin', m.from_user.first_name)



def poll():
    
        bot.polling(none_stop=True)

        
poll()



