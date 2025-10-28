import pywhatkit
import pyautogui
import time
from dotenv import load_dotenv
from datetime import datetime
import os






load_dotenv()

# WhatsApp number (with country code)
phone_number = os.getenv("PHONE_NUMBER")

# Message
current_hour = datetime.now().hour

# Decide message based on time
if 5 <= current_hour < 12:
    message = "🌅 Good Morning!"
elif 12 <= current_hour < 17:
    message = "☀️ Good Afternoon!"
elif 17 <= current_hour < 21:
    message = "🌇 Good Evening!"
else:
    message = "🌙 Good Night!"

print(f"Sending message: {message}")
# Time in 24-hour format
# hour = int(os.getenv("HOUR"))
# minute = int(os.getenv("MINUTE"))


send_hour = datetime.now().hour
send_minute = datetime.now().minute + 1
if send_minute >= 60:
    send_hour = (send_hour + 1) % 24
    send_minute = 0
    
# Schedule message
pywhatkit.sendwhatmsg(phone_number, message, send_hour, send_minute,15,True,3)
time.sleep(15)
pyautogui.press("enter")

print("✅ Message scheduled successfully! Wait for WhatsApp Web to open.")


