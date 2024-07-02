from decouple import config
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
SECRET_KEY=config('OPENAI_API_KEY')


chat = ChatOpenAI(openai_api_key=SECRET_KEY)
messages=[
    SystemMessage(content='You are a standup comedian'),
    HumanMessage(content='how to make tea')
]
response = chat.invoke(messages)
print(response)