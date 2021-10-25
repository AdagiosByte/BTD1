import pyautogui
import random
import time

gameOver = False

while gameOver == False:
    pyautogui.click(780,250) # buy dart monkey
    pyautogui.doubleClick(random.randint(0,720),random.randint(0,700)) #select random tower placement
    #time.sleep(1)
    pyautogui.click(800,500) # buy left upgrade
    pyautogui.click(900,500) # buy right upgrade
    pyautogui.click(900,700) # press Start Round
    
    #check for game over
    gameOver = pyautogui.pixelMatchesColor(440,300,(255,153,85))
    
#pyautogui.click(800,600) # sell tower
#pyautogui.click(800,500) # buy left upgrade
#pyautogui.click(900,500) # buy right upgrade
#pyautogui.click(780,250) # buy dart monkey
#pyautogui.click(820,250) # buy tack tower
#pyautogui.click(random.randint(0,720),random.randint(0,700)) #select random tower placement
#pyautogui.click(900,700) # press Start Round