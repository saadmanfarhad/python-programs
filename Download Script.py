import pyautogui

x, y = 609, 215
move = 40

def clickToDownload(xVal, yVal, i):
    if i < 15:
        pyautogui.rightClick()
        pyautogui.moveTo(x+65, y+150, .5)
        pyautogui.moveTo(x+325, y+150, .5)
        pyautogui.click()
        pyautogui.moveTo(770,620, 1)
        pyautogui.click()
        pyautogui.moveTo(770,670, 1)
        pyautogui.moveTo(1100,670, 1)
        pyautogui.click()
    elif i < 19:
        pyautogui.rightClick()
        pyautogui.moveTo(x+65, y-90, .5)
        pyautogui.moveTo(x+325, y-90, .5)
        pyautogui.click()
        pyautogui.moveTo(770,620, 1)
        pyautogui.click()
        pyautogui.moveTo(770,670, 1)
        pyautogui.moveTo(1100,670, 1)
        pyautogui.click()
    elif i < 22:
        pyautogui.rightClick()
        pyautogui.moveTo(x+65, y+180, .5)
        pyautogui.moveTo(x+325, y+180, .5)
        pyautogui.click()
        pyautogui.moveTo(770,620, 1)
        pyautogui.click()
        pyautogui.moveTo(770,670, 1)
        pyautogui.moveTo(1100,670, 1)
        pyautogui.click()
    else:
        pyautogui.rightClick()
        pyautogui.moveTo(x+65, y-60, .5)
        pyautogui.moveTo(x+325, y-60, .5)
        pyautogui.click()
        pyautogui.moveTo(770,620, 1)
        pyautogui.click()
        pyautogui.moveTo(770,670, 1)
        pyautogui.moveTo(1100,670, 1)
        pyautogui.click()

for i in range(1, 24):
    print(i)
    if i > 18 and i < 20:
        pyautogui.scroll(-10)
        y= y - 320
        pyautogui.moveTo(x,y, .5)
    else:
        if i < 19:
            pyautogui.moveTo(x,y, .5)
            y = y + move
            move = move + .5
        else:
            y = y + move
            move = move - .5
            pyautogui.moveTo(x,y, .5)
    clickToDownload(x, y, i)

    
    
##pyautogui.moveTo(610, 220, 2)
##pyautogui.rightClick()
##pyautogui.moveTo(675,405, 1)
##pyautogui.moveTo(1000,405, 1)
##pyautogui.click()
##pyautogui.moveTo(770,620, 1)
##pyautogui.click()
##pyautogui.moveTo(770,670, 1)
##pyautogui.moveTo(1100,670, 1)
##pyautogui.click()
