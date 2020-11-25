import pyautogui
import time
n = 0
time.sleep(3)
while n<=50:
    n +=1
    pyautogui.typewrite("We are monkey!")
    pyautogui.press("enter")
