from telebot import types, TeleBot

class TelegramBot:
    
    def __init__(self, bot_token, webhook_url=None):
        self.bot = TeleBot(token = bot_token)
        if webhook_url!=None: 
            self.bot.set_webhook(url=webhook_url)
        
    
    def get_info_from_response(self, json_response):
        '''
        This method is used to extract information from the json response sent by telegram.
        
        Parameters:
            json_response (str): json response sent by telegram.
            
        Returns:
            (str): text of the message sent by the user.
            (int): chat id of the user.
            (str): first name of the user.
            (bool): True if the message is a callback query, False otherwise.
        '''
        
        update = types.Update.de_json(json_response)
        
        if update.message:
            message = update.message
            return message.text, message.from_user.id, message.from_user.first_name, False
        elif update.callback_query:
            callback_query = update.callback_query
            return callback_query.data, callback_query.message.chat.id, callback_query.message.from_user.first_name, True
        
    def send_message(self, chat_id, message, markup=None):
        '''
        This method is used to send a message to a user.
        
        Parameters:
            chatid (int): chat id of the user.
            message (str): message to be sent.
            markup (types.InlineKeyboardMarkup): markup to be sent with the message.
        '''
        
        
        self.bot.send_message(chat_id, message, reply_markup=markup)
        
    def send_photo(self, chat_id, photo_url, caption, markup=None):
        '''
        This method is used to send a photo to a user.
        
        Parameters:
            chatid (int): chat id of the user.
            photo (str): path to the photo to be sent.
            caption (str): caption to be sent with the photo.
        '''
        
        self.bot.send_photo(chat_id, photo=photo_url, caption=caption, parse_mode='Markdown', reply_markup=markup)
        
    
    
    

    
        
        
        
    