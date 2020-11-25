# spam_bot
# A simple code to spam the same message over and over.

import pyautogui
import time
n = 0
time.sleep(3)
# while loop to set the number of messages sent 
while n<=50:
    n +=1
    # this text will be spammed over and over
    pyautogui.typewrite("We are monkey!")
    pyautogui.press("enter")
