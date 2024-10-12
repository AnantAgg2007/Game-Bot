import pyautogui
import time
import keyboard
import pyscreeze

def check_and_click():
    abc = ["wood.png", "gold.png", "ore.png", "stone.png"]
    for x in abc:
        try:
            image_location = pyautogui.locateOnScreen(x, region=(166, 97, 952, 535), confidence=0.6)
            if image_location is not None:
                pyautogui.click(pyautogui.center(image_location))
                time.sleep(1)
                pyautogui.click(640,379)
                time.sleep(1)  
                pyautogui.click(970,427)
                time.sleep(1) 
                pyautogui.click(941,535)
                time.sleep(3) 
                pyautogui.click(772,423)
                time.sleep(1)
                return True
            else:
                return False
        except (pyscreeze.ImageNotFoundException, pyautogui.ImageNotFoundException):
            continue
    return False

keys = ['s', 'a', 'w', 'd']
repetitions = 35
delay = 0.2

print("Starting the main loop")
try:
    while True:
        for key in keys:            
            for _ in range(repetitions):
                pyautogui.keyDown(key)
                time.sleep(delay)
                pyautogui.keyUp(key)
                
                if check_and_click():
                    print("Detected and clicked on image")
                    break
                
                if keyboard.is_pressed('P'):
                    print("Exiting due to key press 'P'")
                    exit()
            else:
                continue
            break
except KeyboardInterrupt:
    print("\nExecution interrupted. Exiting...")
