# Introduction
This project is a chatbot assistant on Telegram using OpenAI API and langchain. It collects information from users to suggest hotels based on their preferences.
## Application schema
There are two versions. In the first one, I used a Flask server. In the second one, I deployed the bot using AWS Lambda, AWS ECR, and AWS DynamoDB.
### First version
![Alt text](./schema/flaskserver.drawio%20(1).png?raw=true)
### Second version
![Alt text](./schema/lambda.drawio.png?raw=true)
## Demonstration
In the video, you will notice the chatbot starting by welcoming the user with their Telegram username.Then it begins to ask about user preferences, such as city, check-in, and checkout... . Once it has collected the required information, the system will utilize the Booking API to present hotel options.



https://github.com/Lafifi-24/HotelFinderAssistant/assets/71573277/adef7c81-2e54-4343-b10c-45b962490893




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
After installing requirments and fill and execute api_keys.sh, you can try to excute this tests from tests folder.

    - automated tests:
        contains tests created using pytest to ensure each component from the application works as expected 
        To run it : `python -W ignore -m pytest tests/automated_tests/`

    - manual tests : it has two files 
        - test_chatbot_manager : is a test for the bots perfomence with different scenarios, it helps to improve the prompt for Bots 
        to run it : `python -W ignore tests/manual_tests/test_chatbot_manager.py`
        - test_telegram_bot : is a test for TelegramBot class if it has the ability to interact with user side 
        to use it : 
            - first : execute `python tests/manual_tests/test_telegram_bot.py`
            - second :  use telegram account to communicate with your bot

