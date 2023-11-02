import os
import pytest

from flaskserver.chatbot_manager import ChatbotManager
from flaskserver.chatbot_manager import ChatSession
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
OPENAI_API_key=os.getenv('OPENAI_API_key')
llm = ChatOpenAI(openai_api_key = OPENAI_API_key)
    

class TestChatSession:
    
    @pytest.fixture(autouse=True)
    def build_instance(self):
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template('you are an assistant'),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{human_message}")])
        self.session = ChatSession(chatid=1, model=llm, prompt=prompt)
        
    def test_CreateSession(self):
        assert self.session.chatid == 1
        assert isinstance(self.session.chatbot.llm, ChatOpenAI)
        assert isinstance(self.session.chatbot, LLMChain)
        assert self.session.timestamp_of_creation != None
        
    def test_DemandResponse(self):
        assert self.session.demand_response('hello') != None
        assert self.session.timestamp_of_last_message != None
    
class TestChatBotManager:
    

    def test_Creation(self):
        TestChatBotManager.manager = ChatbotManager(openai_api_key=OPENAI_API_key)
        assert isinstance(TestChatBotManager.manager.llm, ChatOpenAI)
        assert isinstance(TestChatBotManager.manager.prompt, ChatPromptTemplate)
        assert isinstance(TestChatBotManager.manager.sessions, dict)
        
    def test_CreateSessionUsingManager(self):
        TestChatBotManager.session, is_new_session = TestChatBotManager.manager.GetTheSession(chatid=1)
        TestChatBotManager.session.demand_response('hello')
        assert isinstance(TestChatBotManager.session, ChatSession)
        assert is_new_session == True
        
    def test_GetExistingSession(self):
        TestChatBotManager.session, is_new_session = TestChatBotManager.manager.GetTheSession(chatid=1)
        assert isinstance(TestChatBotManager.session, ChatSession)
        assert is_new_session == False
    
    
        
