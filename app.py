import streamlit as st

st.title("GenAI-Powered Conversational Agent")

st.write("This is a placeholder for the application.")
st.write("You can start building your agent here!")

user_input = st.text_input("Ask the agent a question:")

if user_input:
    st.write(f"You asked: {user_input}")
    st.write("Agent's response will appear here...")
