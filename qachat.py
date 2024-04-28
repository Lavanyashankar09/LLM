# Import necessary libraries
from dotenv import load_dotenv  # For loading environment variables
import streamlit as st  # For building the web application
import os  # For accessing environment variables
import google.generativeai as genai  # For accessing the Gemini model

# Load environment variables from .env file
load_dotenv()  # Load all the environment variables

# Configure Gemini model with API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to initialize the Gemini Pro model and start a chat session
model = genai.GenerativeModel("gemini-pro")  # Initialize Gemini Pro model
chat = model.start_chat(history=[])  # Start chat session

# Function to get response from Gemini model based on user input
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)  # Send user input to Gemini model
    return response  # Return the response

# Initialize the Streamlit web application
st.set_page_config(page_title="Q&A Demo")  # Set page title
st.header("Gemini LLM Application")  # Add header

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []  # Initialize empty list for chat history

# Text input field for users to input questions
input = st.text_input("Input: ", key="input")

# Button for users to submit their questions
submit = st.button("Ask the question")

# If the submit button is clicked and there's user input
if submit and input:
    response = get_gemini_response(input)  # Get response from Gemini model based on user input
    
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")  # Display subheader for response
    
    # Display response from Gemini model
    for chunk in response:
        st.write(chunk.text)  # Write response chunk to the app
        st.session_state['chat_history'].append(("Bot", chunk.text))  # Add bot response to chat history

# Display chat history
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")  # Write role (user or bot) and corresponding text to the app
