
import json

from telebot import types

from Application.config import Config
from Application.navigator import Navigator , BookingApiClient
from Application.chatbot_manager import ChatbotManager
from Application.telegram_bot import TelegramBot
from Application.memory import Memory

config = Config(ngrok=False)
memory = Memory(memory_type="DynamoDB")
telegram_bot = TelegramBot(bot_token=config.TELEGRAM_API_KEY)
bots_manager = ChatbotManager(openai_api_key=config.OPENAI_API_KEY)
json_builder = bots_manager.get_json_builder()


booking_api_client = BookingApiClient(api_token=config.BOOKING_API_KEY)
navigator = Navigator(booking_api_client)
client_preferences_storage = {}

def handler(event, context):
    text, chat_id, user_name, is_callback_query = telegram_bot.get_info_from_response(json.loads(event['body']))
    chat_history = memory.load_history_from_dynamodb(str(chat_id))
    chat_session, is_new_session = bots_manager.get_or_create_session(chat_id, chat_history=chat_history)
    if is_new_session:
        telegram_bot.send_message(chat_id, "A new session is starting now.")
        chat_session.add_in_bot_memory("Hello {}, I am your hotel finder assistant. How can I help you?".format(user_name))
        telegram_bot.send_message(chat_id, "Hello {}, I am your hotel finder assistant. How can I help you?".format(user_name))
    else:
        if is_callback_query:
            hotel_id = text.split('/')[1]
            if chat_id in client_preferences_storage:
                Json = client_preferences_storage[chat_id]
                url = navigator.get_hotel_url(hotel_id, Json['checkin_date'], Json['checkout_date'], Json['currency'])
                url_with_params = navigator.build_url_with_params(url, Json)
                telegram_bot.send_message(chat_id, "Here is the link to book the hotel: {}".format(url_with_params))
                
            else :
                telegram_bot.send_message(chat_id, "Sorry, I can't find the hotel you are looking for.")
                
            
  
        else:
            response = chat_session.demand_response(text)
            if '##' in response.strip():
                chat_session.add_in_bot_memory("I will now proceed with searching for suitable hotels based on your preferences. Please give me a moment.")
                telegram_bot.send_message(chat_id, "I will now proceed with searching for suitable hotels based on your preferences. Please give me a moment.")
                json_builder_response = json_builder({"summary":response[response.find('#'):]})['text']
                Json = json.loads(json_builder_response[json_builder_response.find('{'):json_builder_response.find('}')+1])
                hotels = navigator.get_hotels(Json)
                
                for i, hotel in enumerate(hotels):
                    if i > 7:
                        break
                    client_preferences_storage[chat_id] = Json
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    button = types.InlineKeyboardButton("Get the URL", callback_data='{}/{}'.format(chat_id,hotel.id))
                    markup.add(button)
                    telegram_bot.send_photo(chat_id, 
                                            hotel.photoUrl, 
                                            "Hotel Name: **{}**\nClass: {} Stars\nPrice: {} {}\nRating: {} (Rated by {} people)".format(hotel.name, hotel.propertyClass, hotel.price, hotel.currency, hotel.reviewScore, hotel.reviewCount),
                                             markup=markup)
                    
                chat_session.add_in_bot_memory("these are a 7 suitable hotels ordered {}, you can change to popularity or review score or price".format(Json['order_by']))
                telegram_bot.send_message(chat_id, "these are a 7 suitable hotels ordered {}, you can change to popularity or review score or price".format(Json['order_by']))
                
            else:
                telegram_bot.send_message(chat_id, chat_session.demand_response(text))
                
    memory.save_history_to_dynamodb(chat_session.chatbot, str(chat_id)) 
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
        }