
from decouple import config
from langchain_openai import OpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate,PromptTemplate

SECRET_KEY=config('OPENAI_API_KEY')

llm = OpenAI(openai_api_key=SECRET_KEY)

# message prompt template using prompt template

sys_prompt = PromptTemplate(
    input_variables=['input_language','output_language'],
    template='you are a helpful assistant that translates {input_language} to {output_language}.'
    )

print(sys_prompt)
# input_variables=['input_language', 'output_language'] template='you are a helpful assistant that translates {input_language} to {output_language}.'

human_prompt = PromptTemplate(
    input_variables=['text'],
    template='{text}'                        
    )

print(human_prompt)
# input_variables=['text'] template='{text}'

systemMessagePrompt = SystemMessagePromptTemplate(prompt=sys_prompt)
print(systemMessagePrompt)
# prompt=PromptTemplate(input_variables=['input_language', 'output_language'], 
# template='you are a helpful assistant that translates {input_language} to {output_language}.')

humanMessagePrompt = HumanMessagePromptTemplate(prompt=human_prompt)
print(humanMessagePrompt)
# prompt=PromptTemplate(input_variables=['text'], template='{text}')

chatPrompt = ChatPromptTemplate.from_messages([
    systemMessagePrompt,
    humanMessagePrompt
])
print(chatPrompt)

# input_variables=['input_language', 'output_language', 'text'] 
# messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input_language', 'output_language'], 
# template='you are a helpful assistant that translates {input_language} to {output_language}.')),
#  HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['text'], template='{text}'))]

formattedChatPrompt = chatPrompt.format_messages(
    input_language='English',
    output_language='Hindi',
    text='I love Programming'
)
print(formattedChatPrompt)
# [SystemMessage(content='you are a helpful assistant that translates English to Hindi.'),
#  HumanMessage(content='I love Programming')]

res= llm.invoke(formattedChatPrompt)
print(res.content)