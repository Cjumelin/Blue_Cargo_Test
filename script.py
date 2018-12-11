import pyautogui, time, os
pathName = os.getenv('PWD')
print(pathName)
#time.sleep(1);
pyautogui.hotkey('command', 'space')
#time.sleep(1);

pyautogui.typewrite('mail')
#time.sleep(1);
pyautogui.press('enter')
time.sleep(2);
img = pathName + '/img.png'
print(img)
coor = pyautogui.locateCenterOnScreen(img, confidence=.7)
x = coor[0] / 2
y = coor[1] / 2
pyautogui.moveTo((x, y))
pyautogui.click((x, y))
print(coor)
pyautogui.typewrite('cjumelin@protonmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite('Hacker - Challenge')
pyautogui.press('tab')
pyautogui.typewrite('Hello BlueCargo, please find my attachment of the day! \nCheers. Clement Jumelin')
attachment = pathName + '/attachment.png'
print(img)
coor = pyautogui.locateCenterOnScreen(attachment, confidence=.7)
if coor:
    x = coor[0] / 2
    y = coor[1] / 2
    pyautogui.moveTo((x, y))
    pyautogui.click((x, y))

    desktopOn = pathName + '/desktopOn.png'
    print(desktopOn)
    if pyautogui.locateCenterOnScreen(desktopOff, confidence=.7):
        x = coor[0] / 2
        y = coor[1] / 2
        pyautogui.moveTo((x, y))
        pyautogui.click((x, y))

