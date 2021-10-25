import pyautogui
import random
import time

gameOver = False

while gameOver == False:
    pyautogui.click(780,250) # buy dart monkey
    
    while True:
        pyautogui.moveTo(random.randint(40,720),random.randint(40,700)) #select random tower placement
        a = pyautogui.screenshot()
        x,y = pyautogui.position()
        i = a.getpixel((x-60,y))
        
        #check for game over (win or loose)
        if pyautogui.pixelMatchesColor(440,300,(80,232,80)) == True or pyautogui.pixelMatchesColor(440,300,(255,153,85)) == True: 
            gameOver = True
            break
            
        #place tower
        if i[0] > 100 and i[1] > 100 and i[2] > 100:
            pyautogui.click()
            break;
        
        
        
    pyautogui.click(800,500) # buy left upgrade
    pyautogui.click(900,500) # buy right upgrade
    pyautogui.click(900,700) # press Start Round