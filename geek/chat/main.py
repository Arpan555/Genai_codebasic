from decouple import config

from langchain_openai import ChatOpenAI
SECRET_KEY=config('OPENAI_API_KEY')


chat = ChatOpenAI(openai_api_key=SECRET_KEY)
response = chat.invoke('who is pm of india?')
print(response,response.content)