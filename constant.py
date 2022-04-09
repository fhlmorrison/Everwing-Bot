# Change these two when using a new setup
# Values can be found using getPos.py
# TOP_LEFT = (2447, 173)
# BOTTOM_RIGHT = (2934, 1036)
TOP_LEFT = (528, 173)
BOTTOM_RIGHT = (1015, 1036)


# Speed of player movement
SPEED = 2

# Screen size derived from above coords
SCREEN_WIDTH = BOTTOM_RIGHT[0] - TOP_LEFT[0]
SCREEN_HEIGHT = BOTTOM_RIGHT[1] - TOP_LEFT[1]

# Generates coordinates based on ratio of game screen size
ratioToCoord = lambda x, y : (int(TOP_LEFT[0] + SCREEN_WIDTH * x), int(TOP_LEFT[1] + SCREEN_HEIGHT * y))

ratioToRegion = lambda x1, y1, x2, y2 : (int(TOP_LEFT[0] + SCREEN_WIDTH * x1),
 int(TOP_LEFT[1] + SCREEN_HEIGHT * y1),
  int(TOP_LEFT[0] + SCREEN_WIDTH * x2),
   int(TOP_LEFT[1] + SCREEN_HEIGHT * y2))


# Regions, defined by top left and bottom right corners
GAME_BOX = (TOP_LEFT[0], TOP_LEFT[1], BOTTOM_RIGHT[0], BOTTOM_RIGHT[1])
X_BOX = (528, 173, 528 + SCREEN_WIDTH, 173 + SCREEN_HEIGHT) #TODO
MINI_X_BOX = ratioToRegion(0.850, 0.050, 0.950, 0.120)


# Coordinates of buttons
PLAY_AGAIN = ratioToCoord(0.500, 0.589)
CONTINUE_X_BUTTON = ratioToCoord(0.926, 0.114)
SKIP_BUTTON = ratioToCoord(0.500, 0.963)
OKAY_BUTTON = ratioToCoord(0.246, 0.890)
MINI_X_BOX = ratioToCoord(0.908, 0.080)

# Values of x axis limits on fast character movement mode 
# +-2 buffer to avoid drift
LEFT_LIMIT = int(TOP_LEFT[0] + SCREEN_WIDTH * 0.228) + 2
RIGHT_LIMIT = int(TOP_LEFT[0] + SCREEN_WIDTH * 0.733) - 2

# Gets ratio to game screen size based on coords (used when creating constants)
getRatio = lambda x, y : ((x - TOP_LEFT[0])/SCREEN_WIDTH, (y - TOP_LEFT[1])/SCREEN_HEIGHT)

def main():
    print("Debugging mode")
    print(getRatio(970, 242))
    print(MINI_X_BOX)


if __name__ == '__main__':
    main()