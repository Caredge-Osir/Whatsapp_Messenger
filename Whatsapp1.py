import pywhatkit as pwk

##Define the recipient's phone number (With country code) and the message
phone_number = "+254 745 511354"
message = "Hello, this is a test message from Python!"

##Send the message using pywhatkit
pwk.sendwhatmsg(phone_number, message,18,36, wait_time=10, tab_close=True, close_time=3)    

