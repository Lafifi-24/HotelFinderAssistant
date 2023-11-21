### Run the app
you can use two ways to run this app:
- first one is to use the version based on falsk server by :

    - Fill api_keys.sh with your APIs tokens
    - Build docker image `docker build --no-cache -f Dockerfile.flask -t BookingMate .`
    - Run the docker image `docker run -p  5000:5000 BookingMate`
    - Congrats! 
- second one is to use lambda version:
    - Fill api_keys.sh with your APIs tokens
    - Build docker image `docker build --build-arg OPENAI_API_key=$OPENAI_API_key TELEGRAM_API_key=$TELEGRAM_API_key BOOKING_API_key=$BOOKING_API_key --no-cache -f Dockerfile.lambda -t BookingMate .`
    - follow instructions in deployment part from aws documentation https://docs.aws.amazon.com/lambda/latest/dg/python-image.html
    - Create lambda function using docker image , follow instruction from step 4 : https://medium.com/the-resultid-blog/setting-up-a-lambda-function-with-a-docker-image-d29f3611e0c6#:~:text=Setting%20Up%20a%20Lambda%20Function%20With%20a%20Docker,...%206%20Step%206%3A%20Let%E2%80%99s%20test%20it%20out%E2%80%A6
    - https://api.telegram.org/bot<Bot_token>/setWebhook?url=<API_GateWay_link>



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

