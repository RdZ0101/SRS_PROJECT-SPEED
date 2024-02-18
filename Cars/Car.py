import pygame
import math

class Car:
    def __init__(self, pos):
        self.image = pygame.image.load("car.png")
        self.image = pygame.transform.scale(self.image, (40, 20))
        self.pos = pos
        self.steering = 0
        self.speed = 0
        self.center = (self.pos[0] + 50, self.pos[1] + 50)
        
    def draw(self, screen):
        screen.blit(self.image, self.pos)
    
    def move(self):
        if input[pygame.K_UP]:
            self.speed += 0.1
        if input[pygame.K_DOWN]:
            self.speed -= 0.1
        if input[pygame.K_LEFT]:
            self.steering += 0.01
        if input[pygame.K_RIGHT]:
            self.steering -= 0.01
            