import streamlit as st
'''
Main streamlit app
'''
st.title("Main App")
st.write("Some random stuff")

# hide watermark lol
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


