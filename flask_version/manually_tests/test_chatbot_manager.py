#this file to check the performance of the bot

import os
import sys
sys.path.insert(0, os.getcwd())


from langchain.memory import ConversationBufferMemory

from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from flaskserver.config import Config
from flaskserver.chatbot_manager import ChatbotManager




class TestBot:
    def __init__(self, openai_api_key):
        self.llm = ChatOpenAI(openai_api_key = openai_api_key)
        
        self.scenario = {
            1:' You are using  a  hotel finder assistant,\
                Your task is to talk with the assistant and ask him to find a hotel for you.\
                you are looking for a hotel in marrakech for 2 adults and 1 child of 5 years old.\
                your budget about 2000 dirhams , checkin in 2023/11/13 for three days, hotel class is 4. \
                ',
            2:'Act as a human,You are a user for hotel finder assistant,\
                Your task is to talk with the assistant and ask him to find a hotel for you.\
                you are looking for a hotel in paris for 1 adults and 2 child of 5 and 3 years old.\
                your budget less than 800 dollar , checkin in 2023 november 13 for three days. \
                ',
            3:'Act as a human,You are a user for hotel finder assistant,\
                Your task is to talk with the assistant and ask him to find a hotel for you.\
                you are looking for a hotel in tanger for 1 adults, no children\
                your budget more than 200000 yin , checkin in 2023 november 13 for three days. \
                ',
        }
        
    def set_bot_with_scenario(self, senario_id):
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(self.scenario[senario_id]),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{human_message}")])
        memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
        self.bot = LLMChain(llm=self.llm, prompt=prompt, memory=memory,verbose=False)
    
    def demand_response(self, message):
        return self.bot({"human_message": message})['text']
    

config = Config()
manager = ChatbotManager(openai_api_key=config.OPENAI_API_KEY)

testbot = TestBot(openai_api_key=config.OPENAI_API_KEY)



    
    
def create_conversation(Assistant, Client, json_builder):
    assistant_message = Assistant.demand_response('hello')
    print('Start conversation')
    print('Assistant : ',assistant_message)
    i = 0
    while('##' not in assistant_message):
        
        if i > 10:
            break
        
        client_message = Client.demand_response(assistant_message)
        
        assistant_message = Assistant.demand_response(client_message)
        print('Client : ',client_message)
        print('Assistant : ',assistant_message)
        
    print('JSON :',json_builder({"summary": assistant_message})['text'])
        
        
    
        
        
for i in range(3):
    print('########################   Scenarion {}  ########################'.format(i+1))
    testbot.set_bot_with_scenario(i+1)
    Assistant, is_new_session = manager.get_or_create_session(chatid=i)
    
    create_conversation(Assistant, testbot, manager.get_json_builder())
    
        

    