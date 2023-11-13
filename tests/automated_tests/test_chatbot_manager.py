import os
import pytest

from Application.chatbot_manager import ChatbotManager
from Application.chatbot_manager import ClientChatSession
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
    

class TestClientChatSession:
    
    @pytest.fixture(autouse=True)
    def build_instance(self):
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template('you are an assistant'),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{human_message}")])
        self.session = ClientChatSession(chatid=1, model=llm, prompt=prompt)
        
    def test_CreateSession(self):
        assert self.session.chatid == 1
        assert isinstance(self.session.chatbot, LLMChain)
        assert self.session.timestamp_of_creation != None
        
    def test_DemandResponse(self):
        assert self.session.demand_response('hello') != None
        assert self.session.timestamp_of_last_message != None
        
    def test_AddInBotMemory(self):
        self.session.add_in_bot_memory('hello')
        assert self.session.chatbot.memory.chat_memory.messages[-1].content == 'hello'
    
class TestChatBotManager:
    

    def test_Creation(self):
        TestChatBotManager.manager = ChatbotManager(openai_api_key=OPENAI_API_key)
        assert isinstance(TestChatBotManager.manager.llm_interface_bot, ChatOpenAI)
        assert isinstance(TestChatBotManager.manager.prompt_interface_bot, ChatPromptTemplate)
        assert isinstance(TestChatBotManager.manager.client_chat_sessions, dict)
        assert isinstance(TestChatBotManager.manager.json_builder_bot, LLMChain)
        
    def test_CreateSessionUsingManager(self):
        TestChatBotManager.session, is_new_session = TestChatBotManager.manager.get_or_create_session(chatid=1)
        TestChatBotManager.session.demand_response('hello')
        assert isinstance(TestChatBotManager.session, ClientChatSession)
        assert is_new_session == True
        
    def test_GetExistingSession(self):
        TestChatBotManager.session, is_new_session = TestChatBotManager.manager.get_or_create_session(chatid=1)
        assert isinstance(TestChatBotManager.session, ClientChatSession)
        assert is_new_session == False
    
    def test_DeleteSession(self):
        TestChatBotManager.manager.delete_session(chatid=1)
        assert TestChatBotManager.manager.client_chat_sessions == {}
        
    def test_GetJsonBuilder(self):
        assert isinstance(TestChatBotManager.manager.get_json_builder() ,LLMChain)
    
    
        
