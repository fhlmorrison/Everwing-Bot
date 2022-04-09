from doctest import OutputChecker
import cv2
from PIL import ImageGrab
import constant
import numpy as np
import pyautogui

def match_all(image, template, threshold=0.8, debug=False, color=(0, 0, 255)):
    """ Match all template occurrences which have a higher likelihood than the threshold """
    width, height = template.shape[:2]
    match_probability = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    match_locations = np.where(match_probability >= threshold)

    # Add the match rectangle to the screen
    locations = []
    for x, y in zip(*match_locations[::-1]):
        locations.append(((x, x + width), (y, y + height)))

        if debug:
            cv2.rectangle(image, (x, y), (x + width, y + height), color, 1)
    return locations

def findImg(imgPath, region=constant.GAME_BOX,  confidence=0.7):
    im = ImageGrab.grab(bbox=region)
    img = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    testMatch = cv2.imread(imgPath)
    return match_all(img, testMatch, confidence)

def dead(): # Returns true when x button is visible
    return (len(findImg('buttons\\x.png', region=constant.X_BOX))>0)

def share(): # Returns true when the share screen is visible
    return (len(findImg('buttons\\greatScore.png', region=constant.X_BOX))>0)
    return False

def xShare(): # Exits share screen if it is open
    if share():
        #findAndClick('buttons\\miniX.png', region=constant.MINI_X_BOX)
        pyautogui.click(constant.MINI_X_BOX[0], constant.MINI_X_BOX[1])

def findAndClick(imgPath, region=constant.GAME_BOX, confidence=0.7):
    locations = findImg(imgPath, region, confidence)
    if len(locations) > 0:
        print(locations)
        coords = getCenter(locations[0], region)
        pyautogui.click(coords[0], coords[1])
        return True
    getCenter()
    return False

# Gets screen coords of center of rectangle
def getCenter(rect, region=constant.GAME_BOX):
    avg = lambda x, y : (x + y)//2
    print(rect)
    center = tuple(map(avg, rect[0], rect[1]))
    print(center[0] + region[0], center[1] + region[1])
    return (center[0] + region[0], center[1] + region[1])

def main():
    print("Debugging mode")
    xShare()
    print("Done")

if __name__ == '__main__':
    main()