import os
from pyngrok import ngrok

# Configuring Environment Variables

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_key')
    TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_key')
    WEBHOOK_URL = ngrok.connect(5000).public_url
    BOOKING_API_KEY = os.getenv('BOOKING_API_key')