from typing import Union

MemoryType = Union['DynamoDB', 'Mongodb']


class Memory:
    def __init__(self, memory_type: MemoryType = None):
        self.memory_type = memory_type
        self.SessionTable_name = "SessionTable"
        if self.memory_type == 'DynamoDB':
            self.__create_tables_in_dynamoDB()
    
    
    def __create_tables_in_dynamoDB(self):
        import boto3
    
        dynamodb = boto3.resource("dynamodb")
        

        if self.SessionTable_name not in dynamodb.list_tables()["TableNames"]:
            table = dynamodb.create_table(
                TableName=self.SessionTable_name,
                KeySchema=[{"AttributeName": "SessionId", "KeyType": "RANGE"}],
                AttributeDefinitions=[{"AttributeName": "SessionId", "AttributeType": "N"}],
                BillingMode="PAY_PER_REQUEST",
            )

            table.meta.client.get_waiter("table_exists").wait(TableName=self.SessionTable_name)
            
            
    def get_or_create_session_history_from_dynamodb(self, chat_id):
        
        if self.memory_type != 'DynamoDB':
            raise Exception("This method is only for DynamoDB")
        
        from langchain.memory.chat_message_histories import DynamoDBChatMessageHistory

        history = DynamoDBChatMessageHistory(table_name = self.SessionTable_name, session_id=chat_id)

        return history

        
        
        