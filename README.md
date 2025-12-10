# 🔐 OTP Verification System (Python + Streamlit + SMTP)

This project implements a simple and secure **OTP Verification System** using **Python**, **Streamlit**, and **SMTP email service**.  
The user enters an email address, receives a 6-digit OTP in their inbox, and verifies it through the web interface.

---

## 🚀 Features

- ✉️ Send OTP to user’s email
- 🔢 Secure 6-digit OTP generation
- 🌐 Simple Streamlit UI
- 🧠 Session-based OTP storage
- 🔁 Proper error handling for SMTP failures
- 🛡 Environment variable support (`.env`)
- 🧹 Clean and beginner-friendly code

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming |
| Streamlit | Web UI framework |
| smtplib | Sending emails |
| python-dotenv | Secure environment variables |
| MIMEText | Formatting email content |

---

## 📂 Project Structure

```bash
otp_verification/
│── main.py
│── .env
│── README.md
```

---

## 🔧 Setup Instructions

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/tejaskapse1902/otp-verification-system.git
cd otp-verification-system
```

### **2️⃣ Install Dependencies**

```bash
pip install streamlit python-dotenv
```

### **3️⃣ Setup .env File**

- Create a .env file in the project directory:

```bash
EMAIL_ID=your_email@gmail.com
APP_PASSWORD=your_app_password
```

- ⚠️ Gmail users must enable App Password (not regular password).

### **4️⃣ Run the App**

```bash
streamlit run main.py
```

---

## 🖥 How It Works

- User enters an email.
- System generates a 6-digit OTP.
- OTP is sent to the provided email using SMTP.
- User enters OTP into the Streamlit interface.
- System verifies whether it matches the generated OTP.

---

## 🧪 Example

- Send OTP
- - Enter email → Click "Send OTP"

- Verify OTP
- - Enter received OTP → Click "Verify OTP"

---

## Screenshots
![outputs](/images/1.png)
![outputs](/images/2.png)
![outputs](/images/3.png)
![outputs](/images/4.png)

---

## 📌 Future Enhancements

- ⏳ OTP expiry timer (e.g., 60 seconds)
- 🔁 Resend OTP feature
- 🎨 Better UI with custom styling
- 📫 Email validation before sending
- 🗄 Save logs of verification attempts
- 🧩 Modular code structure using functions

---

## 🧑‍💻 Author
- Tejas Kapse
- Python Developer | Automation | Streamlit
- - 🔗 GitHub: https://github.com/tejaskapse1902
- - 🔗 LinkedIn: https://www.linkedin.com/in/tejas-kapse/
- - 📩 Email: tejaskapse19@gmail.com

---