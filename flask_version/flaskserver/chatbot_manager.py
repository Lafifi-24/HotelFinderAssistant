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

class ChatSession:
    def __init__(self, chatid, model, prompt):
        self.timestamp_of_last_message = None
        self.timestamp_of_creation = time.time()
        
        self.chatid = chatid
        
        memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
        self.chatbot = LLMChain(llm=model, prompt=prompt, memory=memory)
        
    def demand_response(self, message):
        self.timestamp_of_last_message = time.time()
        return self.chatbot({"human_message": message})['text']

class ChatbotManager:
    def __init__(self, openai_api_key):
        
        self.sessions = {}
        self.llm = ChatOpenAI(openai_api_key = openai_api_key)
        self.prompt = ChatPromptTemplate(
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
        
    def GetTheSession(self, chatid):
        is_new_session = False
        if chatid not in self.sessions.keys():
            self.sessions[chatid] = ChatSession(chatid, self.llm, self.prompt)
            is_new_session = True
        elif time.time() - self.sessions[chatid].timestamp_of_last_message > 60*60*24 or self.sessions[chatid].timestamp_of_last_message - self.sessions[chatid].timestamp_of_creation > 60*60*24:
            del self.sessions[chatid]
            is_new_session = True
            self.sessions[chatid] = ChatSession(chatid, self.llm, self.prompt)
        return self.sessions[chatid], is_new_session
        