
from decouple import config
from langchain_openai import OpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate,PromptTemplate

SECRET_KEY=config('OPENAI_API_KEY')

llm = OpenAI(openai_api_key=SECRET_KEY)

# message prompt template as tuples

chatPrompt = ChatPromptTemplate.from_messages([
    ('system', 'you are a helpful assistant that translates {input_language} to {output_language}.'),
    ('human','{text}')
])

print(chatPrompt,'\n',chatPrompt.input_variables)
# input_variables=['input_language', 'output_language', 'text'] 
# messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input_language', 'output_language'], 
# template='yuo are a helpful assistant that translates {input_language} to {output_language}.')),
# HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['text'], template='{text}'))]
# \n
#  ['input_language', 'output_language', 'text']


formatedChatPrompt = chatPrompt.format_messages(
    input_language='English',
    output_language='Hindi',
    text='I love Programming'
)

print(formatedChatPrompt)
#  ['input_language', 'output_language', 'text']
# [SystemMessage(content='yuo are a helpful assistant that translates English to Hindi.'), 
# HumanMessage(content='I love Programming')]


res = llm.invoke(formatedChatPrompt)
print(res.content)
