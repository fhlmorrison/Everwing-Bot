#import cv2
from PIL import ImageGrab, ImageOps
#from numpy import *
import time
import win32api, win32con
import pyautogui
import random

#constants
playAgainBtn = (947, 886)
begPlayerCoor = (947, 832)
currPlayerCoor = (947, 832)
x_pad = -402
y_pad = 0
leftLimit = 721
rightLimit = 1173
playing = False

def leftClick(c):
    win32api.SetCursorPos((x_pad+c[0],y_pad+c[1]))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x_pad+c[0],y_pad+c[1])
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x_pad+c[0],y_pad+c[1])
    print("Left click", c[0],c[1])

def movePlayer(x):
    global currPlayerCoor
    if(x<-100 or x>100): 
        print("out of range, x must be bewteen -100 and 100")
    else:
        win32api.SetCursorPos((x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1]))
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1])
        time.sleep(0.05)
        factor = (begPlayerCoor[0]-leftLimit)/100
        currPlayerCoor = (currPlayerCoor[0]+int(factor*x), currPlayerCoor[1])
        win32api.SetCursorPos((x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1]))
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1])
        print("Moved to ", x)

def movePlayer2(x):
    global currPlayerCoor
    if(x<-100 or x>100): 
        print("out of range, x must be bewteen -100 and 100")
    else:
        pyautogui.moveTo(x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1])
        #time.sleep(0.05)
        factor = (begPlayerCoor[0]-leftLimit)/100
        currPlayerCoor = (currPlayerCoor[0]+int(factor*x), currPlayerCoor[1])
        pyautogui.dragTo(x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1], button='left')
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1])
        time.sleep(0.05)
        print("New Coors ", currPlayerCoor)
        print("Moved to ", x)

def sweepLeft(precision):
    global currPlayerCoor
    delta = int((currPlayerCoor[0]-leftLimit)/(precision+1))
    print(delta)
    delta2 = int(100/precision)
    for x in range(precision): #go left
        #movePlayer2(-x*delta2)
        pyautogui.moveTo(x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1])
        #time.sleep(0.05)
        currPlayerCoor = (currPlayerCoor[0]-delta, currPlayerCoor[1])
        pyautogui.dragTo(x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1], button='left')
        #time.sleep(0.05)
    for x in range(precision): #go back
        #movePlayer2(-100+x*delta2)
        pyautogui.moveTo(x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1])
        #time.sleep(0.05)
        currPlayerCoor = (currPlayerCoor[0]+delta, currPlayerCoor[1])
        pyautogui.dragTo(x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1], button='left')
        #time.sleep(0.05)

def sweepRight(precision):
    global currPlayerCoor
    delta = int((currPlayerCoor[0]-rightLimit)/(precision+1))
    for x in range(precision): #go left
        pyautogui.moveTo(x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1])
        time.sleep(0.05)
        currPlayerCoor = (currPlayerCoor[0]-delta, currPlayerCoor[1])
        pyautogui.dragTo(x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1], button='left')
        #time.sleep(0.05)
    for x in range(precision): #go back
        pyautogui.moveTo(x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1])
        time.sleep(0.05)
        currPlayerCoor = (currPlayerCoor[0]+delta, currPlayerCoor[1])
        pyautogui.dragTo(x_pad+currPlayerCoor[0],y_pad+currPlayerCoor[1], button='left')
        #time.sleep(0.05)

def farmSimple():
    print("Simple Farm...press 's' to stop")
    stop = False
    while(not stop):
        if(win32api.GetAsyncKeyState(0x53) & 0x8000):
            stop = True #farming will stop
        leftClick(playAgainBtn)
        time.sleep(1)
    print("Simple Farm is done.")

def farmMove():
    print("Moving Farm...press 'LSHIFT' to stop")
    active = True
    precision = 3
    print(win32api.GetAsyncKeyState(win32con.VK_LSHIFT) & 0x8000)
    while active:
        leftClick(playAgainBtn)
        time.sleep(1)
        #movePlayer2(0)
        #time.sleep(1)
        sweepLeft(precision)
        sweepRight(precision)
        #rand = random.random()
        #movePlayer2(200*rand-100)
        if(win32api.GetAsyncKeyState(win32con.VK_LSHIFT) & 0x8000):
            print("pressed stop code")
            active = False #farming will stop
    print("Moving Farm is done.")

def debug():
    ImageGrab.grab().save('images\\screenTest.png', 'PNG')

def main():
    print("EverWing Bot created by Michael You")
    print("Programmed specifically for the ASUS Zenbook 13\"")
    
    #SELECT BOT MODE
    option = 1

    print("Farming (", option, ") Mode...")
    if option==0:
        farmSimple()
    else:
        farmMove()
    print("Bot Stopped.")

if __name__ == '__main__':
    main()