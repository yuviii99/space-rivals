import pygame
from constants import *
import os

# Width and Height of the Game Window
WIDTH, HEIGHT = 1200, 800

FPS = 60

# Actual Game Window
GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Rivals")

# Images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_red.png'))
BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'space.png'))

# Transform Images
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window():
    GAME_WINDOW.fill(WHITE)
    GAME_WINDOW.blit(YELLOW_SPACESHIP, (275, 400))
    GAME_WINDOW.blit(RED_SPACESHIP, (925, 400))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            # If user closes the window
            if event.type == pygame.QUIT:
                run = False
        draw_window()
        
    pygame.quit()
    

if __name__ == '__main__':
    main()
