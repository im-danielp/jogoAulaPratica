# C
import pygame

COLOR_ORANGE = (155, 128, 50)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 0,
                'Level1Bg2': 1,
                'Level1Bg3': 2,
                'Level1Bg4': 4,
                'Player1': 6,
                'Player2': 6,
                'Enemy1': 4,
                'Enemy2': 2,
                }

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOP',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w,
                 }
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s,
                   }
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a,
                   }
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d,
                    }

# W
WIN_WIDTH = 1300
WIN_HEIGHT = 731
