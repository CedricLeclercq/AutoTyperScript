#	Make sure that:
#		- Python has permission to type on your computer
#		- You have the library 'pyautogui' installed (if not, a simple google search will help you out)

import pyautogui
import time

# Getting input
iterations = int(input("Enter the amount of times the script should run: "))
input = input("Please enter the text you would like to print: ")

# Sleeping to give the user time
print("Starting in 10 seconds. Go to the location you want the script to type for you.")
time.sleep(10)

# Looping over the range of iterations, typewriting the data and sleeping for 0.5 seconds
for i in range(0, iterations):
    pyautogui.typewrite(input + '\n')
    time.sleep(0.5)
