import pywhatkit
import pyautogui
import time
from dotenv import load_dotenv
import os

load_dotenv()

# WhatsApp number (with country code)
phone_number = os.getenv("PHONE_NUMBER")

# Message
message = os.getenv("MESSAGE")

# Time in 24-hour format
hour = int(os.getenv("HOUR"))
minute = int(os.getenv("MINUTE"))

# Schedule message
pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
time.sleep(15)
pyautogui.press("enter")

print("✅ Message scheduled successfully! Wait for WhatsApp Web to open.")

