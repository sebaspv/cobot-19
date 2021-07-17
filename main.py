import streamlit as st
from transformers import pipeline
from PIL import Image
import numpy as np

def get_key(val, dictionary): # get key from value in dictionary
    for key, value in dictionary.items():
         if val == value:
             return key

             
def get_text():
    input_text = st.text_input("Question: ")
    return input_text

def preprocess_txt(file_path):
        with open(file_path, 'r', encoding='utf-8') as my_file:
                file = my_file.read().splitlines()
        file = ' '.join(file)
        return file

# english dataset
data = preprocess_txt('data/cleaned_data_en.txt')
data_es = preprocess_txt('data/cleaned_data_es.txt')
# page config
st.set_page_config(
        page_title = "Covid-Line",
        layout = "wide",
        initial_sidebar_state = "expanded"
)
# hide watermark lol
hide_streamlit_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# model pipeline
models = {
        'English':'mrm8488/electra-small-finetuned-squadv2',
        'Spanish':'mrm8488/electricidad-small-finetuned-squadv1-es'
}
default_language = 'English'
user_choice_model = default_language
col1, col2, col3 = st.sidebar.beta_columns([1,6,1])

with col1:
        st.sidebar.write("")

with col2:
        st.sidebar.image("assets/logo_cobot.png")

with col3:
        st.sidebar.write("")
#st.sidebar.image(np.array(Image.open('assets/logo_cobot.png').resize((200, 200))))
user_choice_model = st.sidebar.selectbox(
        'Language options',
        ('English', 'Spanish')
)

# main app
st.title("CoBot-19")
st.write("#### Write any of your questions about coronavirus here!")
st.write("For the bot to get a better understanding about your question, preferably write descriptive questions using keywords")
st.write("Use keywords such as how, when or what to get a better answer.")
user_input = get_text()
if user_input:
        # get answer from model as a dictionary
        if user_choice_model == 'English':
                context = data
        elif user_choice_model == 'Spanish':
                context = data_es
        question_pipeline = pipeline('question-answering', model=models[user_choice_model])
        answer_dict = question_pipeline({'context': context, 'question': user_input})
        st.text_area("Bot:", value=answer_dict['answer'].capitalize(), height=100, max_chars=None, key=None)

