from telebot import TeleBot

bot = TeleBot('7613331831:AAEokH9p4BA-3QYVOOe6wjA2ABuHSWXOgwM')

@bot.message_handler(commands=['start'])
def botic(message):
    bot.send_message(message.chat.id, 'привет')
    
@bot.message_handler(commands=['реши уравнение'])
def start(message):
    bot.send_message(message.chat.id,'https://mathsolver.microsoft.com/ru/algebra-calculator')
    
@bot.message_handler(commands=['реши задачу'])
def problem(message):
    bot.send_message(message.chat.id, 'https://chatinfo.ru/reshit-zadachu-online')
    
@bot.message_handler(commands=['начерти график'])
def grafic(message):
    bot.send_message(message.chat.id, 'https://www.mathway.com/ru/graph')
    
bot.infinity_polling()