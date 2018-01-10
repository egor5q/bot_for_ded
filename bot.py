# -*- coding: utf-8 -*-
import redis
import os
import telebot
import math
import random
import threading
import info
import test
from telebot import types
from emoji import emojize
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
groups=[]
alreadyspam=0

def spamon(message):
 if alreadyspam==1:
  t=threading.Timer(1.5, spamon, args=[message])
  t.start()
  for id in groups:
    bot.send_message(id, message)
    
    

@bot.message_handler(commands=['spam'])
def spam(m):
  if m.from_user.id==185023717 or m.from_user.id==441399484:
   if alreadyspam==0:
    z=len(m.text)
    message=[(z-4):]
    global alreadyspam=1
    spamon(message)
    
@bot.message_handler(commands=['off'])
def off(m):
  if m.from_user.id==185023717 or m.from_user.id==441399484:
    global alreadyspam=0

@bot.message_handler(content_types=['text'])
def add(m):
  if m.chat.id not in groups:
    groups.append(m.chat.id)






if __name__ == '__main__':
  try:
    bot.send_message(185023717, 'Бот был перезагружен только что')
  except:
    pass
  bot.polling(none_stop=True)



