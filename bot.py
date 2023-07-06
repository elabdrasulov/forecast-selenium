import json
import time 
import pathlib
from telebot import types, TeleBot
from decouple import config

from main import get_source_code
from parse import get_soup, get_page_data

token = config('TOKEN')
bot = TeleBot(token)

main_url = 'https://weather.com/'



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'enter city')
    
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    city = message.text
    bot.send_message(message.chat.id, f'Parsing data for {city}')
    get_source_code(url=main_url, city=city)
    time.sleep(1)
    forecast = pathlib.Path('forecast.html').read_text()
    get_page_data(get_soup(forecast))
    
    if data := get_data_from_json():
        formatted_data = format_data(data)
        bot.send_message(message.chat.id, formatted_data)
    else:
        bot.send_message(message.chat.id, 'Data not found for the specified city')

def get_data_from_json():
    try:
        with open('forecast.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception:
        return None

def format_data(data):
    location = data.get('location')
    degree = data.get('degree')
    condition = data.get('condition')
    return f"Location: {location}\nDegree: {degree}\nCondition: {condition}"
    
bot.polling()


