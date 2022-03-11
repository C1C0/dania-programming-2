import os
import pygame

class COLORS:
    WHITE = (255,255,255)
    
class IMAGES:
    YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'spaceship_yellow.png'))
    RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join(os.path.dirname(__file__), '..', 'assets', 'spaceship_red.png'))
