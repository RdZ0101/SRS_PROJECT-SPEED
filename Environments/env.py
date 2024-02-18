import pygame
import math

screen_width = 800
screen_height = 1500
check_point = ((1200,660), (1250,120), (190,200), (1030, 270), (250,475), (650,690))

class Environment:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.map = pygame.image.load("Tack1.jpg")