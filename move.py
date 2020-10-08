import pyautogui
import random
import threading

screenWidth, screenHeight = pyautogui.size() 

def triggerAction():
	targetX = random.randint(0, screenWidth)
	targetY = random.randint(0, screenHeight)
	print("moving to: ", targetX, targetY)
	pyautogui.moveTo(targetX, targetY, duration=0.3)
	pyautogui.press("shift")
	threading.Timer(5, triggerAction).start()

triggerAction();