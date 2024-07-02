from decouple import config
from langchain_openai import OpenAI
SECRET_KEY=config('OPENAI_API_KEY')


llm = OpenAI(openai_api_key=SECRET_KEY)
response = llm.invoke('I want to start a indian restaurant, suggest me a fancy name')
print(response)