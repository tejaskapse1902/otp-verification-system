import os
import random
import smtplib
import streamlit as st
from email.mime.text import MIMEText
from dotenv import load_dotenv # type: ignore


# MUST be the first Streamlit command

st.set_page_config(
    page_title="OTP Verification System",
    page_icon="🔐",
    layout="centered"
)


# Load environment variables for local development

load_dotenv()


# Read secrets safely (Streamlit Cloud + Local)

EMAIL = None
PASSWORD = None

try:
    EMAIL = st.secrets["EMAIL_ID"]
    PASSWORD = st.secrets["APP_PASSWORD"]
except FileNotFoundError:
    EMAIL = os.getenv("EMAIL_ID")
    PASSWORD = os.getenv("APP_PASSWORD")


# Stop app if credentials are missing

if not EMAIL or not PASSWORD:
    st.error("Email credentials not configured. Please set EMAIL_ID and APP_PASSWORD.")
    st.stop()


# App UI

st.title("🔐 OTP Verification System")
st.subheader("Secure email OTP verification")

# Initialize session state
if "otp" not in st.session_state:
    st.session_state.otp = None


# User email input

email = st.text_input("Enter your email:")


# Send OTP

if st.button("Send OTP"):
    if not email.strip():
        st.warning("Email cannot be empty!")
    else:
        otp = random.randint(100000, 999999)
        st.session_state.otp = otp

        try:
            msg = MIMEText(f"Your OTP is: {otp}")
            msg["Subject"] = "Your OTP Verification Code"
            msg["From"] = EMAIL
            msg["To"] = email

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, email, msg.as_string())
            server.quit()

            st.success(f"OTP sent successfully to **{email}**")

        except Exception as e:
            st.error(f"Failed to send OTP: {e}")


# Verify OTP

if st.session_state.otp:
    user_otp = st.text_input("Enter OTP:", type="password")

    if st.button("Verify OTP"):
        if str(user_otp) == str(st.session_state.otp):
            st.success("✅ OTP Verified Successfully!")
            st.session_state.otp = None
        else:
            st.error("❌ Incorrect OTP! Please try again.")
