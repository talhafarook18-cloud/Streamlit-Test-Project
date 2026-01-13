from google import genai
import streamlit as st

client = genai.Client (api_key='AIzaSyA3uvDeUuRiY-E4Zcl2JOMSWOSxJONcwfc')

st.title("Finance Advisor")
st.write("This app demonstrates a conversational agent.")

user_input = st.text_input("How can I help you.")
if st.button("Submit"):
    with st.spinner("Agent is thinking...."):
        response = client.models.generate_content(
             model='gemini-2.5-flash', contents=user_input,
            config=types.GenerateContentConfig(
    system_instruction="Your name is IBBI and you are a finance advisor who only answere relevant questions."),
        )
    st.write(response.text)



