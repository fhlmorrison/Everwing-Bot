# Change these two when using a new setup
# Values can be found using getPos.py
TOP_LEFT = (2447, 173)
BOTTOM_RIGHT = (2934, 1036)

# Speed of player movement
SPEED = 2

# Screen size derived from above coords
SCREEN_WIDTH = BOTTOM_RIGHT[0] - TOP_LEFT[0]
SCREEN_HEIGHT = BOTTOM_RIGHT[1] - TOP_LEFT[1]

# Generates coordinates based on ratio of game screen size
ratioToCoord = lambda x, y : (int(TOP_LEFT[0] + SCREEN_WIDTH * x), int(TOP_LEFT[1] + SCREEN_HEIGHT * y)) 

# Coordinates of buttons
PLAY_AGAIN = ratioToCoord(0.500, 0.589)
CONTINUE_X_BUTTON = ratioToCoord(0.926, 0.114)
SKIP_BUTTON = ratioToCoord(0.500, 0.963)
OKAY_BUTTON = ratioToCoord(0.246, 0.890)

# Values of x axis limits on fast character movement mode 
# +-2 buffer to avoid drift
LEFT_LIMIT = int(TOP_LEFT[0] + SCREEN_WIDTH * 0.228) + 2
RIGHT_LIMIT = int(TOP_LEFT[0] + SCREEN_WIDTH * 0.733) - 2

# Gets ratio to game screen size based on coords (used when creating constants)
getRatio = lambda x, y : ((x - TOP_LEFT[0])/SCREEN_WIDTH, (y - TOP_LEFT[1])/SCREEN_HEIGHT)

def main():
    print("Debugging mode")


if __name__ == '__main__':
    main()