import pyautogui, time, os, datetime

pathName = os.getenv('PWD')
print(pathName)

pyautogui.hotkey('command', 'space')
pyautogui.typewrite('Sublime Text')
pyautogui.press('enter')
time.sleep(.2)
pyautogui.hotkey('command', 'n')
time.sleep(.2)
now = datetime.datetime.now()
strToBlueCargoFile = "Hi Bluecargo, today is " + str(now) + "."
pyautogui.typewrite(strToBlueCargoFile)
pyautogui.hotkey('command', 'shift', 's')
pyautogui.typewrite('BlueCargoFile')
desktopDayModeOff = pathName + '/desktopDayModeOff.png'
print(desktopDayModeOff)
time.sleep(.2);
coor = pyautogui.locateCenterOnScreen(desktopDayModeOff, confidence=.7)
print (coor)
if coor:
    x = coor[0] / 2
    y = coor[1] / 2
    pyautogui.moveTo((x, y))
    pyautogui.click((x, y))
    saveBlueCargoFile = pathName + '/saveBlueCargoFile.png'
    print(saveBlueCargoFile)
    time.sleep(.2);
    coor = pyautogui.locateCenterOnScreen(saveBlueCargoFile, confidence=.7)
    print (coor)
    if coor:
        x = coor[0] / 2
        y = coor[1] / 2
        pyautogui.moveTo((x, y))
        pyautogui.click((x, y))
        replaceBlueCargoFile = pathName + '/replaceBlueCargoFile.png'
        print(replaceBlueCargoFile)
        time.sleep(.2);
        coor = pyautogui.locateCenterOnScreen(replaceBlueCargoFile, confidence=.7)
        print (coor)
        if coor:
            x = coor[0] / 2
            y = coor[1] / 2
            pyautogui.moveTo((x, y))
            pyautogui.click((x, y))

time.sleep(.5)

pyautogui.hotkey('command', 'space')
pyautogui.typewrite('mail')
pyautogui.press('enter')
time.sleep(2);
img = pathName + '/img.png'
print(img)
coor = pyautogui.locateCenterOnScreen(img, confidence=.7)
x = coor[0] / 2 # It's divide by two because of the retina resolution particularities
y = coor[1] / 2
pyautogui.moveTo((x, y))
pyautogui.click((x, y))
print(coor)
pyautogui.typewrite('jobs@bluecargo.io')
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
    desktopOff = pathName + '/desktopOff.png'
    print(desktopOff)
    time.sleep(1);
    coor = pyautogui.locateCenterOnScreen(desktopOff, confidence=.7)
    print (coor)
    if coor:
        x = coor[0] / 2
        y = coor[1] / 2
        pyautogui.moveTo((x, y))
        pyautogui.click((x, y))
        pyautogui.hotkey('command', 'f')
        pyautogui.typewrite('BlueCargoFile')
        blueCargoFileNightMode = pathName + '/blueCargoFileNightMode.png'
        print(blueCargoFileNightMode)
        time.sleep(.2);
        coor = pyautogui.locateCenterOnScreen(blueCargoFileNightMode, confidence=.7)
        print (coor)
        if coor:
            x = coor[0] / 2
            y = coor[1] / 2
            pyautogui.moveTo((x, y))
            pyautogui.click((x, y))
            time.sleep(.2)
        else :
            blueCargoFileNightModeGray = pathName + '/blueCargoFileNightModeGray.png'
            print(blueCargoFileNightModeGray)
            time.sleep(.2);
            coor = pyautogui.locateCenterOnScreen(blueCargoFileNightModeGray, confidence=.7)
            print (coor)
            if coor:
                x = coor[0] / 2
                y = coor[1] / 2
                pyautogui.moveTo((x, y))
                pyautogui.click((x, y))
        if coor:
            chooseBlueCargoFile = pathName + '/chooseBlueCargoFile.png'
            print(chooseBlueCargoFile)
            time.sleep(.2);
            coor = pyautogui.locateCenterOnScreen(chooseBlueCargoFile, confidence=.7)
            print (coor)
            if coor:
                x = coor[0] / 2
                y = coor[1] / 2
                pyautogui.moveTo((x, y))
                pyautogui.click((x, y))
                sendMail = pathName + '/sendMail.png'
                print(sendMail)
                time.sleep(.2);
                coor = pyautogui.locateCenterOnScreen(sendMail, confidence=.7)
                print (coor)
                if coor:
                    x = coor[0] / 2
                    y = coor[1] / 2
                    pyautogui.moveTo((x, y))
                    pyautogui.click((x, y))
