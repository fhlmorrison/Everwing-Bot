#import cv2
#from PIL import ImageGrab, ImageOps
import numpy as np
import time
import win32api, win32con
import pyautogui
import constant
import imageProcessing as imp

#constants
begPlayerCoor = (947, 832)
currPlayerCoor = (947, 832)
bossX = (1140, 254)
levelUp = (949, 699)
bossRaids = (1101, 421)

#params
x_pad = -430
y_pad = 0
leftLimit = 721
rightLimit = 1173
playing = False

def leftClick(c):
    pyautogui.click(c[0], c[1])

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

def sweepLeft():
    pyautogui.dragTo(constant.LEFT_LIMIT, constant.PLAY_AGAIN[1], 1/constant.SPEED, button='left')

def sweepRight():
    pyautogui.dragTo(constant.RIGHT_LIMIT, constant.PLAY_AGAIN[1], 1/constant.SPEED, button='left')

def farmSimple(t):
    print("Simple Farm...press 's' to stop")
    stop = False
    start_time = time.time()
    while(((time.time()-start_time)<t) and (not stop)):
        leftClick(constant.PLAY_AGAIN)
        time.sleep(5)
        while not (imp.dead() or stop):
            if(win32api.GetAsyncKeyState(0x53) & 0x8000):
                stop = True #farming will stop
                break
            sweepLeft()
            sweepRight()
        else: 
            if stop:
                continue
        imp.xShare()
        leftClick(constant.CONTINUE_X_BUTTON)
        time.sleep(8)
        leftClick(constant.SKIP_BUTTON)
        time.sleep(4)
        leftClick(constant.OKAY_BUTTON)
        time.sleep(4)

    print("Simple Farm is done.")

def farmMove(t):
    # Will have auto pathing
    print(f"Running Pathing Bot for {t} seconds")


def main():
    print("Bot starting")

    botName1 = "Simple"
    botName2 = "Pathing"

    #SELECT BOT MODE
    option = pyautogui.confirm(text="", title="", buttons=[botName1, botName2])

    #Select time
    response = pyautogui.prompt(text="Enter the number of seconds to run the bot for (integer)", title="Run Time", default="300")
    botTime = int(response)

    print("Farming (", option, ") Mode...")
    if option == botName1:
        farmSimple(botTime)
        print("Bot Stopped.")
        return
    if option == botName2:
        farmMove(botTime)
        print("Bot Stopped.")
        return

if __name__ == '__main__':
    main()