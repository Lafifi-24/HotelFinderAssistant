### Run the app
- First step create your telegram Bot
- Second Create the backend:
    - falsk server :

        - Fill api_keys.sh with your APIs tokens
        - Build docker image `docker build --no-cache -f Dockerfile.flask -t BookingMate .`
        - Run the docker image `docker run -p  5000:5000 BookingMate`
        - Congrats! 
    - aws lambda serverless:
        - Build docker image `docker build --no-cache -f Dockerfile.lambda -t BookingMate .`
        - follow instructions in deployment part from [aws documentation](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html) 
        - Create lambda function using docker image 
        - Add AmazonDynamoDBFullAccess policy to the role.
        - Add Environment variables from api_keys with your tokens
        - Change Memory=1024 MB and Timeout = 1 min 
        - Open this link in your browser `https://api.telegram.org/bot<Bot_token>/setWebhook?url=<API_GateWay_link>`, be sur that you get the message "webhook was set"



### Tests
After installing requirments and fill and execute api_keys.sh, you can try to excute this tests from tests folder.\

    - automated tests:\
        contains tests created using pytest to ensure each component from the application works as expected \
        To run it : `python -W ignore -m pytest tests/automated_tests/`

    - manual tests :\
    it has two files :
        - test_chatbot_manager : is a test for the bots perfomence with different scenarios, it helps to improve the prompt for Bots \
        to run it : `python -W ignore tests/manual_tests/test_chatbot_manager.py`
        - test_telegram_bot : is a test for TelegramBot class if it has the ability to interact with user side \
        to use it : 
            - first : execute `python tests/manual_tests/test_telegram_bot.py`
            - second :  use telegram account to communicate with your bot

