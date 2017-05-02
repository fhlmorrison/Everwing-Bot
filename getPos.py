import time
import win32api, win32con
import pyautogui

def main():
    while(True):
        if(win32api.GetAsyncKeyState(win32con.VK_LSHIFT)):
            x, y = win32api.GetCursorPos()
            print("x: ", (x-291), "y: ", (y-178))
            print(pyautogui.position())
            time.sleep(1)

if __name__ == '__main__':
    main()