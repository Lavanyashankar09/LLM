# Import necessary libraries
from dotenv import load_dotenv  # For loading environment variables
import streamlit as st  # For building the web application
import os  # For accessing environment variables
import textwrap  # For text manipulation
import google.generativeai as genai  # For accessing the Gemini model
from IPython.display import Markdown  # For displaying Markdown

# Function to convert text to Markdown format
def to_markdown(text):
    text = text.replace('•', '  *')  # Replace bullet points with Markdown format
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))  # Indent text and convert to Markdown

# Load environment variables from .env file
load_dotenv()

# Configure Gemini model with API key from environment variables
os.getenv("GOOGLE_API_KEY")  # Fetch Google API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Configure Gemini model with API key

# Function to get response from Gemini model based on input question
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')  # Initialize Gemini model
    response = model.generate_content(question)  # Generate response based on input question
    return response.text  # Return the response text

# Initialize the Streamlit web application
st.set_page_config(page_title="Q&A Demo")  # Set page title
st.header("Gemini Application")  # Add header

# Input field for users to enter their questions
input = st.text_input("Input: ", key="input")

# Button for users to submit their questions
submit = st.button("Ask the question")

# If the submit button is clicked
if submit:
    response = get_gemini_response(input)  # Get response from Gemini model
    st.subheader("The Response is")  # Add subheader for response
    st.write(response)  # Display the response
