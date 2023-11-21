from Application.memory import Memory
import boto3


class MemoryTest():
    
    def test_creation(self):
        memory = Memory(memory_type="DynamoDB")
        assert memory.memory_type == "DynamoDB"
        assert memory.SessionTable_name == "SessionTable"
        
        dynamodb = boto3.resource("dynamodb")
        

        assert memory.SessionTable_name in dynamodb.list_tables()["TableNames"]:
        
    