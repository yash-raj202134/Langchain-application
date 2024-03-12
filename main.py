## Integrate the open AI API

import os
from constants import openai_key

# from langchain.llms import OpenAI
from langchain_community.llms import OpenAI

import streamlit as st



os.environ['OPENAI_APT_KEY'] = openai_key


# streamlit framework
st.title('Langchain Demo with openAI API')
input_text = st.text_input("Search the topic you want")


## OPENAI LLMS
llm=OpenAI(temperature=0.8,openai_api_key=openai_key)



if input_text:
    st.write(llm(input_text))
