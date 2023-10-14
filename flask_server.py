from flask import Flask,request
import os

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
            "you are a hotel assistant, you are helping a customer to find a hotel, you well collect informations from costumer like check in and check out ,city\
                ,price range, number of stars, and number of adults and children, avoid talk about any thing else, you can ask the customer about any thing you need\
                    , then return jsson have this information"
                
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{human_message}"),
    ]
)





global_memory = {}
app = Flask(__name__)
def sendmessage(chatid, message):
    url = "https://api.telegram.org/bot{}/sendMessage".format(TELEGRAM_API_key)
    payload = {
        "text":message,
        "chat_id":chatid
        }
    
    resp = requests.get(url,params=payload)
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
        result = global_memory[chatid]({"human_message": message})
        sendmessage(chatid,result["text"])
    return "Done"
@app.route("/setwebhook/")
def setwebhook():
    url = "https://939e-197-253-204-147.ngrok.io"#ngrok http 5000
    s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}".format(TELEGRAM_API_key,url))
    if s:
        return "yes"
    else:
        return "fail"
    
if __name__ == "__main__":
    app.run(debug=True)