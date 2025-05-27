import pywhatkit as pwk

phone_number = "+254111888517"
message = "Dijkstra's algorithm.com"

pwk.sendwhatmsg_instantly(phone_number, message, wait_time=20, tab_close=True, close_time=5)
 