import pygame.locals

WINDOW_NAME = 'Pixel Bowmaster'
ICON = 'Assets/menu/icon.png'

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800


ARROW_COUNT_LEVEL_1 = 10
ARCHER_STARTING_POSITION = [20,20]
ARCHER_SHOOTING_ANIMATION_SPEED = 0.10
ARCHER_IDLE_ANIMATION_SPEED = 0.07
ARCHER_MOVING_SPEED = 7

BALLOON_SPEED = 1.7
BALLOON_ANIMATION_SPEED = 0.15
FIRST_BALLOON_DISTANCE = 600

ARROW_SPEED = 6.8

CLOCK = 60

MOVE_UP_KEY = pygame.K_UP
MOVE_DOWN_KEY = pygame.K_DOWN
SHOOT_KEY = pygame.K_SPACE


MENU_TITLE = ('Assets/menu/game_title_with_arrow.png')
MENU_SIZE_MULTIPLIER = 6.5
MENU_SIZE = (int(111*MENU_SIZE_MULTIPLIER),int(58*MENU_SIZE_MULTIPLIER))

PIXEL_FONT = ('Assets/font/pixel_font.ttf')

PLAY_BUTTON = ('Assets/menu/Play_button.png')
PLAY_BUTTON_RED = ('Assets/menu/Play_button_red.png')
PLAY_BUTTON_MULTIPLIER = 3.1
PLAY_BUTTON_SIZE = ((int(55*PLAY_BUTTON_MULTIPLIER), int(20*PLAY_BUTTON_MULTIPLIER)))

GAME_OVER = [
'Assets/menu/game_over/game_over_1.png',\
'Assets/menu/game_over/game_over_2.png',\
'Assets/menu/game_over/game_over_3.png',\
'Assets/menu/game_over/game_over_4.png',\
'Assets/menu/game_over/game_over_5.png',\
'Assets/menu/game_over/game_over_6.png',\
'Assets/menu/game_over/game_over_7.png',\
'Assets/menu/game_over/game_over_8.png',\
'Assets/menu/game_over/game_over_9.png',\
'Assets/menu/game_over/game_over_10.png',\
'Assets/menu/game_over/game_over_11.png',\
'Assets/menu/game_over/game_over_12.png',\
'Assets/menu/game_over/game_over_13.png',\
'Assets/menu/game_over/game_over_14.png',\
'Assets/menu/game_over/game_over_15.png',\
'Assets/menu/game_over/game_over_16.png',\
'Assets/menu/game_over/game_over_17.png',\
'Assets/menu/game_over/game_over_18.png',\
'Assets/menu/game_over/game_over_19.png',\
'Assets/menu/game_over/game_over_20.png',\
'Assets/menu/game_over/game_over_21.png',\
'Assets/menu/game_over/game_over_22.png',\
'Assets/menu/game_over/game_over_23.png',\
'Assets/menu/game_over/game_over_24.png',\
'Assets/menu/game_over/game_over_25.png',\
'Assets/menu/game_over/game_over_26.png',\
'Assets/menu/game_over/game_over_27.png',\
'Assets/menu/game_over/game_over_28.png',\
'Assets/menu/game_over/game_over_29.png',\
'Assets/menu/game_over/game_over_30.png',\
'Assets/menu/game_over/game_over_31.png',\
'Assets/menu/game_over/game_over_32.png',\
'Assets/menu/game_over/game_over_33.png'
]

STATIC_GAME_OVER =  'Assets/menu/game_over/game_over.png'
GAME_OVER_ANIMATION_SPEED = 0.3
GAME_OVER_SCALE = 9

