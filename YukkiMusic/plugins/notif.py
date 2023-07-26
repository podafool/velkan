# banner- notification -twilio 

# bot_monitor.py

import time
import subprocess
from twilio.rest import Client

# Replace with your Twilio account information
TWILIO_ACCOUNT_SID = 'AC96636123c0a13b720f392b60ba3f8d41'
TWILIO_AUTH_TOKEN = '1597930f8b6bc9cd4ab7ff0346ffc77b'
TWILIO_PHONE_NUMBER = '+15733076359'
YOUR_PHONE_NUMBER = '+917092719924'

# Replace with your bot's Python script command
BOT_SCRIPT_COMMAND = 'bash start'

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms_notification(message):
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=YOUR_PHONE_NUMBER
    )

def display_warning_message():
    warning_message = r"""
               ********** WARNING **********
       The bot is going to stop in 5 minutes!
  Please save any important data and take necessary
             actions before it stops.
               ******************************

    """
    print(warning_message)

def check_bot_status():
    while True:
        try:
            # Check if the bot process is running
            result = subprocess.run(
                BOT_SCRIPT_COMMAND.split(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                print("Bot is running.")
            else:
                # Warn before stopping
                display_warning_message()
                time.sleep(4 * 60)  # Wait 4 minutes (adjust as needed)
                
                send_sms_notification("Bot is stopped!")
                print("Bot is stopped! Notification sent.")
        except subprocess.TimeoutExpired:
            send_sms_notification("Bot is not responding!")
            print("Bot is not responding! Notification sent.")
        except Exception as e:
            print("Error occurred:", str(e))
        time.sleep(60)  # Check every 1 minute

if __name__ == "__main__":
    check_bot_status()

# In this updated script, I've added the display_warning_message() function that contains the ASCII art warning message. When the bot is detected to be stopped, this function will be called, and the warning message will be printed in the console output.

# You can customize the ASCII art warning message by modifying the warning_message variable. Feel free to adjust the layout or add more decoration to suit your preferences. The warning message will be visible in the console output when the bot is going to stop. Additionally, the SMS notification will still be sent via Twilio as before.

# Keep in mind that the appearance of the ASCII art may vary depending on the font used in your console or terminal, but it should be reasonably visible on half the screen.
