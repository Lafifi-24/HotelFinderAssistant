from flask import Flask,request
import os
import json
import re

from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import requests


OPENAI_API_key=os.getenv('OPENAI_API_key')
TELEGRAM_API_key=os.getenv('TELEGRAM_API_key')
llm = ChatOpenAI(openai_api_key = OPENAI_API_key)
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a part from hotel assistant system. Your task is to contact customers and build json for the second part from the system by gathering specific information\
            Please gather this details from the customer:\
            Check-in and Check-out Dates:\
            Number of Persons: including both adults and children.\
            Number of Rooms: Indicate how many rooms you'll need.\
            Children Details: If there are any children in the group, please provide their ages.\
            Budget: Kindly share your budget for the stay, indicating the currency.\
            Location: Please specify the city and country where you'd like to book the hotel.\
            Hotel Class: If you have a preference, mention the hotel class, such as 2-star or 5-star.\
            Based on the information collected, a JSON object will be created with the following keys:\
            'checkin'  YYYY-MM-DD format.\
            'checkout' YYYY-MM-DD format.\
            'group_adults' number \
            'no_rooms'\
            'group_children'\
            'age'\
            'price'\
            'city'\
            'country'\
            'class'\
            For any information not provided, the JSON will have 'none' as the value.\
            Kindly note that unrelated questions will be avoided, and each question will be asked only once.\
            Your last message should be the only JSON object reflecting the collected information"
                
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{human_message}"),
    ]
)



    
@app.route("/",methods=["POST","GET"])
def index():
    if(request.method == "POST"):
        data = request.get_json()
        message = data["message"]["text"]
        user = data["message"]["from"]["first_name"]
        chatid = data["message"]["chat"]["id"]
        if chatid not in global_memory.keys():
            memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
            global_memory[chatid] = LLMChain(
                        llm=llm,
                        prompt=prompt,
                        memory=memory
                    )
        # Notice that we just pass in the `question` variables - `chat_history` gets populated by memory
        url_to_send_the_message = "https://api.telegram.org/bot{}/sendMessage".format(TELEGRAM_API_key)
        message = global_memory[chatid]({"human_message": message})['text']
        json_part = message[message.find('{'): message.find('}')+1]
        if len(json_part) > 0:
            params = json.loads(str(json_part))
            resp = requests.get(url_to_send_the_message,params={"text":"it takes time",
                    "chat_id":chatid})
            print('Start')
            try : 
                hotels = navigate(params)
            except :
                hotels = ['navigation error']
            print('Done')
                
            
            payload = {
                "text":str(hotels),
                "chat_id":chatid
                }

            resp = requests.get(url_to_send_the_message,params=payload)
            return 'Done'

        payload = {
            "text":message,
            "chat_id":chatid
            }
    
    resp = requests.get(url_to_send_the_message,params=payload)
    return "Done"

    
    
if __name__ == "__main__":
    app.run(debug=True)