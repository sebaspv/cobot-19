import streamlit as st
from transformers import pipeline

# .txt file to strings in a list
with open ("data.txt", "r") as myfile:
    data = myfile.read().splitlines()
# join the strings as context
data = ' '.join(data)
def get_text():
    input_text = st.text_input("Question: ")
    return input_text
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
tiny_electra = "mrm8488/electra-small-finetuned-squadv2" # model name (can be changed)
# data pipeline
question_pipeline = pipeline('question-answering', model=tiny_electra)

# main app
st.title("Covid-Line Chatbot")
st.write("#### Write any of your questions here!")
user_input = get_text()
if user_input:
        # get answer from model as a dictionary
        answer_dict = question_pipeline({'context': data, 'question': user_input})
        st.text_area("Bot:", value=answer_dict['answer'].capitalize(), height=100, max_chars=None, key=None)

