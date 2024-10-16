import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
prompt = ChatPromptTemplate.from_messages(
    [
        ('system','your name is Anil, answer all the questions asked by the human'),
        ('human','{text}')
        ]
)
llm = OllamaLLM(model="llama3.2")
outputparser = StrOutputParser()
chain = prompt|llm|outputparser
question = str(st.text_input("what's in your mind?"))
if question:
    #response = chain.invoke({'text':question})
    st.write(question)

if __name__ == "__main__":
    main()
