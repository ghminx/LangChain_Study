
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import load_prompt
import time

def select_prompt(template_name):

    # prompt = load_prompt('./prompts/' + template_name + '.yaml', encoding = 'cp949')
    prompt = load_prompt('./prompts/' + template_name + '.yaml', encoding='utf-8')

    return prompt


def chat_model(model_name, text, prompt):

    # prompt = PromptTemplate.from_template(template)
    
    llm = ChatGroq(model = model_name,
                   temperature = 0.5)
    
    chain = prompt | llm | StrOutputParser()
    
    response = chain.stream(text)
    return response




