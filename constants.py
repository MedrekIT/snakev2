import pygame
from enum import Enum

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
GAME_FONT = pygame.font.SysFont("timesnewroman", 30)

RECT_EDGE = 20

class Difficulty(Enum):
    EASY = 1
    NORMAL = 2
    HARD = 3
    INSANE = 4

class Direction(Enum):
    UP = 'W'
    DOWN = 'S'
    LEFT = 'A'
    RIGHT = 'D'
    NONE = ''