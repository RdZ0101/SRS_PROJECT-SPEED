import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Resize the map image to screen size

screen_width = 800
screen_height = 800
checkpoint = [(100, 100), (200, 100), (200, 200), (100, 200)]


class Environment:
    def __init__(self):
        # Set up the screen
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("PROJECT:SPEED")

        # Load the map image
        self.map = pygame.image.load("Track1.jpg")
        self.map = pygame.transform.scale(self.map, (screen_width, screen_height))

    def run(self):
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 

            # Draw the map
            self.screen.blit(self.map, (0, 0))

            # Update the display
            pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    # Create an instance of the Environment class
    env = Environment()

    # Run the application
    env.run()
