import time

from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

class ClientChatSession:
    def __init__(self, chatid, model, prompt, history=None):
        self.timestamp_of_last_message = None
        self.timestamp_of_creation = time.time()
        self.timestamp_of_last_message = time.time()
        self.chatid = chatid
        
        memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True, history=history, max_history_length=20)
        self.chatbot = LLMChain(llm=model, prompt=prompt, memory=memory, verbose=False)
        
    def demand_response(self, message):
        self.timestamp_of_last_message = time.time()
        return self.chatbot({"human_message": message})['text']
    
    def add_in_bot_memory(self, message):
        self.chatbot.memory.chat_memory.add_ai_message(message)

class ChatbotManager:
    def __init__(self, openai_api_key):
        
        self.client_chat_sessions = {}
        
        
        
        # the approximate idea which I try to build is to create two Bots
            # self.llm_json_builder_bot = ChatOpenAI(openai_api_key = openai_api_key,temperature=0, model_name="gpt-3.5-turbo-instruct")the first one, interfaceBot :  we will create an instance for each user Session, its role is to engage in conversation with the user and gather the information from him,
            # the second one, JsonBuilder : it will create json object from the summary of the first bot, respecting the format of the json object 
        # the beneifits from this idea :
            # use less Quota from the openai api
            # the bots will be more accurate when they have a specific role
            # more secure, the user interact with interface bot without knowing how his data is processed
        
        self.llm_interface_bot = ChatOpenAI(openai_api_key = openai_api_key,temperature=0.1, model_name="gpt-3.5-turbo")
        self.prompt_interface_bot = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    "You are a hotel finder assistant system. Your task is to communicate with customers and build a summary of the user's information.\
                    You should gather this details ->  city, country, check-in, check-out, number of persons,number of rooms, number of children and their ages ,price preferences and desired hotel class. \
                    Avoid unrelated questions, and each question will be asked only once.\
                    Avoid any answer unrelated to your tasks.\
                    Add to your message ('##Summary':information that you collect)  every time you want to do a search for hotels. "
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{human_message}"),
            ] 
        )
        
        self.create_json_builder_bot(openai_api_key)
        
        
    
    def create_json_builder_bot(self, openai_api_key):
        
        llm_json_builder_bot = ChatOpenAI(openai_api_key = openai_api_key,temperature=0, model_name="gpt-3.5-turbo")
        prompt_json_builder = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    "your role is to take the input and extract data from it to build json object.\
                    Input: text\
                    your output as json:\
                    order_by: popularity or review_score or price by default put popularity\
                    adults_number: number\
                    checkin_date: YYYY-MM-DD\
                    currency: USD as a default or one of these(AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAM,BBD,BDT,BGN,BHD,BIF,BMD,BND,BOB,BRL,BSD,BTN,BWP,BYN,BYR,BZD,CAD,CDF,CHF,CLP,CNY,COP,CRC,CUP,CVE,CYP,CZK,DJF,DKK,DOP,DZD,EEK,EUR,EGP,ETB,FJD,GBP,GEL,GHS,GMD,GNF,GRD,GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,INR,IQD,IRR,ISK,JMD,JOD,JPY,KES,KGS,KHR,KMF,KRW,KWD,KYD,KZT,LAK,LBP,LKR,LRD,LSL,LTL,LVL,LYD,MAD,MDL,MGA,MKD,MMK,MNT,MOP,MRO,MTL,MUR,MVR,MWK,MXN,MYR,MZN,NAD,NGN,NIO,NOK,NPR,NZD,OMR,PAB,PEN,PGK,PHP,PKR,PLN,PYG,QAR,ROL,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SGD,SIT,SKK,SLL,SOS,SRD,STD,SVC,SYP,SZL,THB,TJS,TMM,TND,TOP,TRY,TTD,TWD,TZS,UAH,UGX,USD,UYU,UZS,VEB,VEF,VES,VND,VUV,WST,XAF,XCD,XOF,XPF,YER,ZAR,ZMK,ZMW),\
                    city: string\
                    country:string , you can deducated from city\
                    checkout_date: YYYY-MM-DD \
                    room_number: number by default is 1\
                    children_number: number by default is 0\
                    children_ages: array have numbers such as [2,3]\
                    price: [A,B] follows this logic [140,190], or [150,'min'] or '150,'max'] \
                    class: [list of stars(int)]"
                ),
                HumanMessagePromptTemplate.from_template("{summary}"),
            ]
        )
        self.json_builder_bot = LLMChain(llm=llm_json_builder_bot, prompt=prompt_json_builder)
        
    def get_or_create_session(self, chatid, history=None):
        is_new_session = False
        if chatid not in self.client_chat_sessions.keys():
            self.client_chat_sessions[chatid] = ClientChatSession(chatid, self.llm_interface_bot, self.prompt_interface_bot)
            is_new_session = True
        elif time.time() - self.client_chat_sessions[chatid].timestamp_of_last_message > 60*60*24 or self.client_chat_sessions[chatid].timestamp_of_last_message - self.client_chat_sessions[chatid].timestamp_of_creation > 60*60*24:
            del self.client_chat_sessions[chatid]
            is_new_session = True
            self.client_chat_sessions[chatid] = ClientChatSession(chatid, self.llm_interface_bot, self.prompt_interface_bot)
        return self.client_chat_sessions[chatid], is_new_session
    
    def delete_session(self, chatid):
        del self.client_chat_sessions[chatid]
    
    def get_json_builder(self):
        return self.json_builder_bot
        
        