import pyautogui
import random
import threading

screenWidth, screenHeight = pyautogui.size() 

def triggerMove():
	targetY = random.randint(0, screenHeight)
	targetX = random.randint(0,screenWidth)
	print("moving to: ", targetX,targetY)
	pyautogui.moveTo(targetX, targetY, duration=0.25)
	threading.Timer(3, triggerMove).start()

triggerMove();