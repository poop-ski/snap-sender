# Author: Utkarsh Yadav
# Date: 20/10/2022
import pyautogui
import time

# Sleep initially to give you some time to focus on the Snapchat window
time.sleep(3)

# Define a function to click a specific position
def click_position(x, y):
    pyautogui.click(x, y)

# Define a function to type a string
def type_text(text):
    pyautogui.write(text)

# Main loop for your actions
while True:
    # Click on specific positions
    click_position(1012, 700)  # Adjusted Y-coordinate for the snap button
    click_position(1095, 775)
    time.sleep(0.2)
    click_position(1054, 320)

    # Type the "utkarsh" text
    type_text("utkarsh")

    # Click on more positions
    click_position(1079, 507)
    click_position(1134, 800)
