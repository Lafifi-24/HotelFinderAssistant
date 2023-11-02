import os
from pyngrok import ngrok

# Configuring Environment Variables
class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
    Webhook_URL = ngrok.connect(5000).public_url