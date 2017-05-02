import cv2
from PIL import ImageGrab, ImageOps, Image, ImageEnhance, ImageFilter
import pyautogui
import pytesseract
import time
import win32api, win32con

#constants
playAgainBtn = (226, 704)
begPlayerCoor = (223, 662)
currPlayerCoor = (223, 662)
bossX = (414, 77)
bossFight = (223,679)
bossRaids = (374, 243)
levelUp = (226, 521)
sidekicks = (320,454)
characters = (220,317)

#params
x_pad = 291 #-402
y_pad = 178
gameBox = (291,178,738,969)
gameBoxS = (291,178,447,791)
gameBoxC = ((291,178),(738,178),(738,969),(291,969))
coinBox = (284+x_pad, 1+y_pad, 120, 35)
xPossible = [378, 422, 504, 571, 620, 660]

#others
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

def debug():
    im = pyautogui.screenshot("tests\\screenEW.png", region=gameBoxS)
    img = cv2.imread('tests\\screenEW.png')
    cv2.circle(img, (playAgainBtn[0], playAgainBtn[1]), 6, (255, 0, 0))
    cv2.circle(img, (bossRaids[0], bossRaids[1]), 6, (255, 255, 0))
    #cv2.WINDOW_NORMAL
    cv2.imshow('output', img)
    cv2.waitKey(0)

def readCoins():
    pyautogui.screenshot("tests\\screenEWCoin.png", region=coinBox)
    #im = Img.open('tests\\screenEWCoin.png')
    #im = im.filter(ImageFilter.MedianFilter())
    #rip need to fix path
    text = pytesseract.image_to_string(Image.open('tests\\screenEWCoin.png'))

def findButtons():
    im = pyautogui.screenshot("tests\\screenEW.png", region=gameBoxS)
    location = pyautogui.locateOnScreen('buttons\\bossRaids.png')
    #found = False
    while(False):
        imTemp = pyautogui.screenshot(region=gameBoxS)
        location = pyautogui.locate('buttons\\bossRaids.png', imTemp, grayscale=True)
        if(location is not None):
            found = True
        print(location)
    pyautogui.click(pyautogui.center(location))
    #print(x,y)

def findButtons2():
    im = pyautogui.screenshot("tests\\screenEW.png", region=gameBoxS)
    img = cv2.imread("buttons\\lily.png")
    template = cv2.imread("tests\\screenEW.png",0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    w,h = template.shape[::-1]
    print("w:",w,"h:",h)
    m = eval('cv2.TM_CCOEFF_NORMED')
    res = cv2.matchTemplate(img,template,m)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0]+w,top_left[1]+h)
    print("found:", top_left, bottom_right)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    cv2.imshow("buttons", template)
    cv2.waitKey(0)

def findHead():
    im = pyautogui.screenshot("tests\\screenEW.png", region=gameBoxS)
    active = True
    while(active):
        if(win32api.GetAsyncKeyState(win32con.VK_LSHIFT) & 0x8000):
            print("pressed stop code")
            active = False #farming will stop
        imTemp = pyautogui.screenshot(region=gameBoxS)
        #location = pyautogui.locate('buttons\\quests.png', imTemp, grayscale=True)
        location = pyautogui.locateOnScreen("buttons\\lilyHead.png")
        print(location)
        if(location is not None):
            print(location)
            pyautogui.moveTo(pyautogui.center(location))

def getHead():
    while(True):
        location = pyautogui.locateOnScreen("buttons\\lilyHead.png")
        if (location is not None):
            return pyautogui.center(location)

def getComet():
    location = pyautogui.locateOnScreen("buttons\\comet.png")
    if (location is not None):
        return pyautogui.center(location)
    else:
        return -1

def moveTo(x):
    pyautogui.moveTo(getHead()) #move to Head
    yC = 818
    xC = xPossible[x]
    pyautogui.dragTo((xC, yC))

def farm():
    print("press LSHIFT to stop")
    isPlaying = False
    active = True
    #for x in range(4):
        #moveTo(3-x)
    
    while(active):    
        if(win32api.GetAsyncKeyState(win32con.VK_LSHIFT) & 0x8000):
            print("pressed stop code")
        playAgain = pyautogui.locateOnScreen("buttons\\playAgain.png")
        if(playAgain is not None):
            print("Play Again")
            pyautogui.click(pyautogui.center(playAgain))
        for x in range(len(xPossible)):
            cometW = getComet()
            if(cometW==-1):
                moveTo(x)
            else:
                xT,yT = cometW
                if(abs(xT-xPossible[x])<26):
                    moveTo((x+1) % (len(xPossible)))
                    x = (x+1 % len(xPossible))
        for x in range(len(xPossible)):
            cometW = getComet()
            if(cometW==-1):
                moveTo((len(xPossible)-x) % len(xPossible))
            else:
                xT,yT = cometW
                if(abs(xT-xPossible[len(xPossible)-x])<26):
                    moveTo((x+1) % len(xPossible))
                    x = (x+1 % len(xPossible))
        print("Done Farming")
def main():
    #while(True):
    #    print(getHead())
    #    time.sleep(0.5)
    #print(getHead())
    #findButtons()
    #findButtons2()
    farm()

if __name__ == '__main__':
    main()