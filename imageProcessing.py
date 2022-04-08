import cv2
from PIL import ImageGrab
import constant
import numpy as np

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

def findImg(imgPath, region=constant.GAME_BOX,  confidence = 0.7):
    im = ImageGrab.grab(bbox=region)
    img = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    testMatch = cv2.imread(imgPath)
    return match_all(img, testMatch, confidence)

def dead():
    return (len(findImg('buttons\\x.png', region=constant.X_BOX))>0)
    


if __name__ == '__main__':
    main()