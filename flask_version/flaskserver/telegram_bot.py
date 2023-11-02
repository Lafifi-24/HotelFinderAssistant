import requests


class TelegramBot:
    def __init__(self, bot_token, webhook_url):
        self.bot_token = bot_token 
        self.webhook_url = webhook_url
        
    def set_webhook(self):
        answer = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}".format(self.bot_token,self.webhook_url))#ngrok http 5000
        if not answer.ok:
            raise Exception("Error setting webhook: {}".format(answer.text))

    def send_message(self,chatid, message):
        url = "https://api.telegram.org/bot{}/sendMessage".format(self.bot_token)
        payload = {
            "text":message,
            "chat_id":chatid
            }
        resp = requests.get(url,params=payload)
    