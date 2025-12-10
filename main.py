import streamlit as st
import random
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv # type: ignore
import os
import time

load_dotenv()

EMAIL = os.getenv("EMAIL_ID")
PASSWORD = os.getenv("APP_PASSWORD")

if not EMAIL or not PASSWORD:
    st.error("Email or App Password not found. Check your .env file.")
    
st.title("OTP Verification System")

# Initialize session_state
if "otp" not in st.session_state:
    st.session_state.otp = None


# User email input
email = st.text_input("Enter your email:")

# Send OTP button
if st.button("Send OTP"):
    if not email.strip():
        st.warning("Email cannot be empty!")
    else:
        otp = random.randint(100000, 999999)
        st.session_state.otp = otp  # store OTP for verification

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

            st.success(f"OTP sent successfully! Check your email **{email}**")
        
        except Exception as e:
            st.error(f"Failed to send OTP: {e}")

# OTP input appears only when OTP is generated
if st.session_state.otp:
    user_otp = st.text_input("Enter OTP:", type="password")

    if st.button("Verify OTP"):
        if str(user_otp) == str(st.session_state.otp):
            st.success("OTP Verified Successfully!")
            st.session_state.otp = None  # reset OTP after success
        else:
            st.error("Incorrect OTP! Please try again.")