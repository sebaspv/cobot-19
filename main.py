import streamlit as st
from transformers import pipeline

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
        initial_sidebar_state = "collapsed",
        page_icon = "🦠"
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
user_choice_model = st.selectbox(
        'Language options',
        ('English', 'Spanish')
)
# data pipeline

# main app
st.title("Covid-Line Chatbot")
st.write("#### Write any of your questions here!")
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

