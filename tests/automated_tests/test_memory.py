from Application.memory import Memory
import boto3


class MemoryTest():
    
    def test_creation(self):
        memory = Memory(memory_type="DynamoDB")
        assert memory.memory_type == "DynamoDB"
        assert memory.SessionTable_name == "SessionTable"
        
        dynamodb = boto3.resource("dynamodb")
        
        assert memory.SessionTable_name in dynamodb.list_tables()["TableNames"]
        
        table = dynamodb.Table(memory.SessionTable_name)
        table.delete()
        table.wait_until_not_exists()
        
    def test_create_session(self):
        memory = Memory(memory_type="DynamoDB")
        
        history = memory.create_session(1233)
        history.add_ai_message("Hello")
        
        
    