
from decouple import config
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

SECRET_KEY=config('OPENAI_API_KEY')

llm = OpenAI(openai_api_key=SECRET_KEY)

# prompt having multiple input variable

multipleInputPrompt = PromptTemplate(input_variables=['language','topic'],template='tell me a {language} {topic} trick')
# oneInputPromptAnother = PromptTemplate.from_template('tell me a {language} {topic} trick')

formatMultiplePrompt = multipleInputPrompt.format(language='Java',topic='Array')

res = llm.invoke(formatMultiplePrompt)

print(res)