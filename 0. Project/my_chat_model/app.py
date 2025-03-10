import streamlit as st 
from utils import chat_model, select_prompt
from langchain_core.prompts import PromptTemplate


st.set_page_config(page_title="IamGPT", page_icon=":shark:", layout="wide")

st.title("STI Task Chatbot")


# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Display chat messages
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


with st.sidebar:
    st.title("Settings")
    
    if clear_btn:= st.button("Clear Chat", on_click=lambda: st.session_state.pop('messages', None)):
        st.info("대화 내용 초기화")
    
    tab1, tab2 = st.tabs(['Model', 'Templates'])


    with tab1:
        
        # Select model
        model_name = st.selectbox("Select Model", ["gemma2-9b-it", "qwen-2.5-32b", 'deepseek-r1-distill-qwen-32b', 'qwen-2.5-coder-32b','llama-3.3-70b-specdec'])
        st.info(f'{model_name} 모델이 적용되었습니다.')
            

    with tab2:
        # Select template
        templates_name = st.selectbox("Select Template", ["기본", "요약", '번역', 'sns'])
        
        # PromptTemplate 생성
        prompt = select_prompt(templates_name)
        
        st.info(f'{templates_name} 템플릿이 선택되었습니다.')
        

# if user_msg:= st.chat_input('what is up?')는 변수를 선언하면서 바로 조건문을 사용
# user_msg = st.chat_input('what is up?')
# if user_msg:  와 같음

# React to user input
if user_msg:= st.chat_input('what is up?'):
    
    # Ouput user message
    with st.chat_message('user'):
        st.markdown(user_msg)

    # Add user message to chat history        
    st.session_state['messages'].append({'role' : 'user', 'content' : user_msg})
    
    # Output response
    with st.chat_message('assistant'):
        
        chat_container = st.empty()
        
        response = chat_model(model_name, user_msg, prompt)
        
        assistant_answer = ''
        for chunk in response:
            assistant_answer += chunk
            chat_container.markdown(assistant_answer)
            
    # Add response to chat history
    st.session_state['messages'].append({'role' : 'assistant', 'content' : assistant_answer})
    
    


    