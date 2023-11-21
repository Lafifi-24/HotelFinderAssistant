import os


# Configuring Environment Variables

class Config:
    def __init__(self, ngrok=False):
        
        self.OPENAI_API_KEY = os.getenv('OPENAI_API_key')
        self.TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_key')
        
        self.BOOKING_API_KEY = os.getenv('BOOKING_API_key')
        if ngrok:
            from pyngrok import ngrok
            self.WEBHOOK_URL = ngrok.connect(5000).public_url