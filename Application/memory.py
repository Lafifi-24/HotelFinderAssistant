from typing import Union
import ast

import boto3

from langchain.schema import messages_from_dict, messages_to_dict
from langchain.memory.chat_message_histories.in_memory import ChatMessageHistory
from langchain.chains import LLMChain


MemoryType = Union['DynamoDB', 'Mongodb']


class Memory:
    def __init__(self, memory_type: MemoryType = None):
        self.memory_type = memory_type
        self.SessionTable_name = "SessionTable"
        if self.memory_type == 'DynamoDB':
            self.__create_tables_in_dynamoDB()
        if self.memory_type == 'Mongodb':
            raise Exception("Mongodb is not supported yet")
    
    
    def __create_tables_in_dynamoDB(self):
        import boto3
    
        dynamodb = boto3.resource("dynamodb")
        

        if self.SessionTable_name not in [table.name for table in dynamodb.tables.all()]:
            table = dynamodb.create_table(
                TableName=self.SessionTable_name,
                KeySchema=[{"AttributeName": "SessionId", "KeyType": "HASH"}],
                AttributeDefinitions=[
                    {"AttributeName": "SessionId", "AttributeType": "S"},
                    ],
                BillingMode="PAY_PER_REQUEST",
            )

            table.meta.client.get_waiter("table_exists").wait(TableName=self.SessionTable_name)
            
            
    def save_history_in_dynamodb(self,chatbot: LLMChain, chat_id: str):
        extracted_messages = messages_to_dict(chatbot.memory.chat_memory.messages)
        dynamodb = boto3.client('dynamodb')
        dynamodb.put_item(TableName=self.SessionTable_name, Item={'SessionId':{'S':chat_id},'history':{'L':[ { 'S':str(message)} for message in extracted_messages]}})
        
    def load_history_from_dynamodb(self, chat_id: str):
        dynamodb = boto3.client('dynamodb')
        try:
            data = dynamodb.get_item(TableName=self.SessionTable_name, Key={'SessionId':{'S':chat_id}}).get('Item').get('history').get('L')
            dict_of_history = messages_from_dict([ast.literal_eval(message['S']) for message in data])
            chat_history = ChatMessageHistory(messages=dict_of_history)
            return chat_history, False
        except:
            chat_history = ChatMessageHistory(messages=[]), True
        
        

        
        
        