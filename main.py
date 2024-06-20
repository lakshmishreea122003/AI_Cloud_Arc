import streamlit as st

st.set_page_config(
    page_title="Main",
    page_icon="☁️",
)

st.markdown("<h1 style='color: black; font-style: italic; font-family: Comic Sans MS; font-size:5rem' >AICloudArc ☁️</h1> <h3 style='color: black; font-style: italic; font-family: Comic Sans MS; font-size:2rem'>Provides cloud architecture tailored to your needs and visualizes it.</h3>", unsafe_allow_html=True)


st.markdown("<p style='color: #4FC978; font-style: italic; font-family: Comic Sans MS; ' >AICloudArc is an AI powered platform that suggests cloud architectures to the user based on their needs and also uses fine tuned models to help visualize the architecture.</p>", unsafe_allow_html=True)

prompt = st.text_input("Enter your requirements here.")



