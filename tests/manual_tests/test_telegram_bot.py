
## this file is for testing the telegram bot, is not automatic test, you should run it and test the bot manually
## you should run the flask server first, then run this file
import os
import sys
sys.path.insert(0, os.getcwd())


from telebot import types
from flask import Flask, request



from Application.telegram_bot import TelegramBot
from Application.config import Config

app = Flask(__name__)
config = Config()

bot = TelegramBot(config.TELEGRAM_API_KEY, config.WEBHOOK_URL)

@app.route('/', methods=['POST'])
def webhook():
    text, chat_id, user_name, is_callback_query = bot.get_info_from_response(request.stream.read())
    
   
    
    if is_callback_query:
        if text == 'photo':
            bot.send_photo(chat_id, 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png', 'This is a python logo \n success')
        bot.send_message(chat_id, 'Hello, ' + user_name +' ,you clicked on button '+ text)
    else:
        
    
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("photo", callback_data='photo'.format(chat_id))
        item2 = types.InlineKeyboardButton("next", callback_data='next/{}'.format(user_name))
        markup.add(item1, item2)
        bot.send_message(chat_id, 'Hello, ' + user_name, markup=markup)
        
    
    return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

