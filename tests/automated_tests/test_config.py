from Application.config import Config



def test_Creation():
    instance = Config()
    assert instance.OPENAI_API_KEY != None
    assert instance.TELEGRAM_API_KEY != None
    assert instance.WEBHOOK_URL != None
    assert instance.BOOKING_API_KEY != None