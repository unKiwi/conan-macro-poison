import random
import time
import keyboard
import pyautogui

class Case:
	def __init__(self, key, x, y):
		self.key = key
		self.x = x
		self.y = y

inventoryKey = "i"
poison = Case("²", 106, 259)
searchBar = Case("", 139, 161)
currentWeapon = 0
weapon = [
	Case("!", 1300, 1000),
	Case("*", 1200, 1000),
	Case("ù", 1100, 1000)
]

while True:
	key = keyboard.read_key()
	print(key)
	if key.lower() == poison.key:
		# open inventory
		pyautogui.keyDown(inventoryKey)
		pyautogui.keyUp(inventoryKey)
		# search "reaper poison"
		pyautogui.moveTo(searchBar.x  + random.randint(-93, 93), searchBar.y  + random.randint(-10, 10))
		pyautogui.click()
		pyautogui.write('reaper poison')
		time.sleep(0.3)
		# move poison
		pyautogui.moveTo(poison.x  + random.randint(-30, 30), poison.y  + random.randint(-30, 30))
		pyautogui.mouseDown()
		pyautogui.moveTo(weapon[currentWeapon].x + random.randint(-30, 30), weapon[currentWeapon].y  + random.randint(-30, 30), 0.2)
		pyautogui.mouseUp()
		# close inventory
		pyautogui.keyDown(inventoryKey)
		pyautogui.keyUp(inventoryKey)
	# elif key == "i":
	# 	print(pyautogui.position())
	else:
		for i in range(len(weapon)):
			if key == weapon[i].key:
				currentWeapon = i
