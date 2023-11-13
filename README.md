- you can run this application in your local follow this instruction\
    - excute `python -W ignore -m flask --app flaskserver/main.py run` 
- Tests folder
    - automated tests:\
        contains tests created using pytest to ensure each companant from the application works as expected \
        
        To run it : `python -W ignore -m pytest tests/automated_tests/`
    - manual tests :\
    it has two files :
        - test_chatbot_manager : is a test for the bots perfomence with different scenarion, it helps to improve the prompt for Bots \
        to run it : `python -W ignore tests/manually_tests/test_chatbot_manager.py`
        - test_telegram_bot : is a test for TelegramBot class if it has the ability to interact with user side \
        to use it : 
            - first : excute `python tests/manually_tests/test_telegram_bot.py`
            - second :  use telegram account to communicate with your bot

