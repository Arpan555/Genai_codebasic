from decouple import config
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

SECRET_KEY=config('OPENAI_API_KEY')

llm = OpenAI(openai_api_key=SECRET_KEY)

noInputPrompt = PromptTemplate(input_variables=[], template='tell me a python trick')
# noIptDiffPrompt = PromptTemplate.from_template('tell me a python trick')

formatednoInputPrompt  = noInputPrompt.format()

res = llm.invoke(formatednoInputPrompt)

print(res)
