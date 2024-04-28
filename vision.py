from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Gemini model with API key from environment variables
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model based on input text prompt and image
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')  # Initialize Gemini model for text and images
    if input != "":
        response = model.generate_content([input, image])  # Generate response based on text prompt and image
    else:
        response = model.generate_content(image)  # Generate response based on image only
    return response.text  # Return the response text

# Initialize the Streamlit web application
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

# Text input field for users to input prompts
input = st.text_input("Input Prompt: ", key="input")

# File uploader for users to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""  # Initialize image variable

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button for users to request information about the image
submit = st.button("Tell me about the image")

# If the submit button is clicked
if submit:
    response = get_gemini_response(input, image)  # Get response from Gemini model
    st.subheader("The Response is")  # Display subheader for response
    st.write(response)  # Display the response
