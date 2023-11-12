import os
import json
import re

from flask import Flask,request
from telebot.types import InputFile

from config import Config
from navigator import Navigator , BookingApiClient
from chatbot_manager import ChatbotManager
from telegram_bot import TelegramBot

app = Flask(__name__)

telegram_bot = TelegramBot(bot_token=Config.TELEGRAM_API_KEY,webhook_url=Config.WEBHOOK_URL)
bots_manager = ChatbotManager(openai_api_key=Config.OPENAI_API_KEY)
json_builder = bots_manager.get_json_builder()


booking_api_client = BookingApiClient(api_token=Config.BOOKING_API_KEY)
navigator = Navigator(booking_api_client)

    
@app.route("/",methods=["POST","GET"])
def webhook():
    
    text, chat_id, user_name, is_callback_query = telegram_bot.get_info_from_response(request.stream.read())
    
    
    chat_session, is_new_session = bots_manager.get_or_create_session(chat_id)
    if is_new_session:
        telegram_bot.send_message(chat_id, "A new session is starting now.")
        chat_session.add_in_bot_memory("Hello {}, I am your hotel finder assistant. How can I help you?".format(user_name))
        telegram_bot.send_message(chat_id, "Hello {}, I am your hotel finder assistant. How can I help you?".format(user_name))
    else:
        if is_callback_query:
            pass
        else:
            response = chat_session.demand_response(text)
            if '##' in response:
                json_builder_response = str(json_builder(response[response.find('##'):]))
                Json = json.loads(json_builder_response[json_builder_response.find('{'):json_builder_response.find('}')+1])
                hotels = navigator.get_hotels(Json)
                for hotel in hotels:
                    telegram_bot.send_photo(chat_id, hotel.photo_url, "*Name :* **{}**\n\n*Class :* {}\n*Price :* {}{}\n*Rating :* {} by {} person\n ".format(hotel.name, hotel.propertyClass, hotel.price, hotel.currency, hotel.reviewScore, hotel.reviewCount))
                
            else:
                telegram_bot.send_message(chat_id, chat_session.demand_response(text))
        
    
    return 'ok', 200

    
    
if __name__ == "__main__":
    app.run(debug=True)