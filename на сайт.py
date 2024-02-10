from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os


load_dotenv()

PROXY_URL = 'http://178.49.22.23'
bot = Bot(token=os.environ.get('TOKEN'), proxy=PROXY_URL)
dp = Dispatcher(bot)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую! Я - Тестовый бот!\nКоманда /help - открывает меню действий')
    
@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Рабочие команды:\n/start - перезапустить бот \n/help - команды бота\n/YT - оффициальная ссылка на YouTube\n/TT - оффициальная ссылка на TikTok')
    
@bot.message_handler(commands=['YT'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='YouTube', url='https://m.youtube.com/')
    kb.add(btn1)
    bot.send_message(message.chat.id, 'Оффициальная ссылка на YouTube!', reply_markup=kb)
    
@bot.message_handler(commands=['TT'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    btn2 = types.InlineKeyboardButton(text='TikTok', url='https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.tiktok.com/ru-RU/&ved=2ahUKEwj_x_nJmpmEAxVdAxAIHfUaBXwQFnoECAYQAQ&usg=AOvVaw28dSVjhQ3xv1dyaXxqs8u2')
    kb.add(btn2)
    bot.send_message(message.chat.id, 'Оффициальная ссылка на TikTok!', reply_markup=kb)
    
@bot.message_handler(func= lambda message: True)
def start(message):
    bot.reply_to(message, 'Я еще не научился общаться с живыми людьми. Воспользуйтесь командой /help для ознакомлениями с командами!')
    
bot.polling()
