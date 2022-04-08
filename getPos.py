import time
import win32api, win32con
import pyautogui

def main():
    while(True):
        if(win32api.GetAsyncKeyState(win32con.VK_LSHIFT)):
            print(pyautogui.position())
            time.sleep(1)

if __name__ == '__main__':
    main()