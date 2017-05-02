import cv2
from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
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

def debug():
    im = pyautogui.screenshot("tests\\screenEW.png", region=gameBoxS)
    img = cv2.imread('tests\\screenEW.png')
    cv2.circle(img, (playAgainBtn[0], playAgainBtn[1]), 6, (255, 0, 0))
    cv2.circle(img, (bossRaids[0], bossRaids[1]), 6, (255, 255, 0))
    #cv2.WINDOW_NORMAL
    cv2.imshow('output', img)
    cv2.waitKey(0)

def readCoins():
    im = pyautogui.screenshot("tests\\screenEWCoin.png", region=coinBox)
    img = cv2.imread('tests\\screenEWCoin.png')
    #cv2.WINDOW_NORMAL
    cv2.imshow('output', img)
    cv2.waitKey(0)

def main():
    readCoins()

if __name__ == '__main__':
    main()