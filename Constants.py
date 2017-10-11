#color information
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

#window information
HEIGHT = 480
WIDTH = 360
FPS = 60
TITLE = 'olol making a game in python? kids.'

#player information
PLAYER_ACC = 2
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 1.4


#Starting platforms
PLATFORM_LIST = \
[
    (WIDTH/2-50, HEIGHT *3/4, 100, 20),
    (0, HEIGHT-40, WIDTH, 40),
    (125, HEIGHT-350, 100, 20),
    (350, 200, 100, 20),
    (175, 100, 50, 20)
]


