import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Streamlit page settings
st.set_page_config(
    page_title="AI Email Generator",
    page_icon="📧",
    layout="centered"
)

# Title
st.title("📧 AI Email Generator")
st.write("Generate professional emails using Google's Gemini AI.")

# User Inputs
recipient = st.text_input("Recipient Name")

purpose = st.text_input("Email Purpose")

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Formal", "Friendly", "Casual"]
)

details = st.text_area("Additional Details")

# Generate Email
if st.button("Generate Email"):

    if recipient == "" or purpose == "" or details == "":
        st.warning("Please fill in all the fields.")
    else:

        prompt = f"""
Write a {tone} email.

Recipient: {recipient}

Purpose: {purpose}

Additional Details:
{details}

The email should include:
1. Subject
2. Greeting
3. Email Body
4. Closing
5. Professional signature as 'Your Name'
"""

        with st.spinner("Generating email..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.success("Email Generated Successfully!")

        st.subheader("Generated Email")

        st.text_area(
            "Email",
            response.text,
            height=350
        )