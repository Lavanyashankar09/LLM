# Import necessary libraries
from dotenv import load_dotenv  # For loading environment variables
import streamlit as st  # For building the web application
import os  # For accessing environment variables
from PIL import Image  # For working with images
import google.generativeai as genai  # For accessing the Gemini model

# Load environment variables from .env file
load_dotenv()  # Load all the environment variables

# Configure Gemini model with API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model based on input text prompt, image, and additional prompt
def get_gemini_response(input, image, prompt):
    # Initialize the Gemini Pro Vision model
    model = genai.GenerativeModel('gemini-pro-vision')
    # Generate response based on input text prompt, image, and additional prompt
    response = model.generate_content([input, image[0], prompt])
    return response.text  # Return the response text

# Function to setup image data for Gemini model
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        # Prepare image parts data
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts  # Return the image parts data
    else:
        raise FileNotFoundError("No file uploaded")  # Raise an error if no file is uploaded

# Initialize the Streamlit web application
st.set_page_config(page_title="Gemini Image Demo")  # Set page title
st.header("Gemini Application")  # Add header

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

# Prompt text for additional context
input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

# If the submit button is clicked
if submit:
    # Setup image data for Gemini model
    image_data = input_image_setup(uploaded_file)
    # Get response from Gemini model
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is")  # Display subheader for response
    st.write(response)  # Display the response
