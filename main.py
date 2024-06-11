import pygame
from constants import *
import os

# Width and Height of the Game Window
WIDTH, HEIGHT = 1200, 800

FPS = 60
VELOCITY = 5

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

# Separating Line
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)


def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY >= 0:
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x + yellow.width <= BORDER.x:
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY >= 0:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT - 15:
        yellow.y += VELOCITY


def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x -  VELOCITY >= BORDER.x + BORDER.width:
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width <= WIDTH:
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and red.y - VELOCITY >= 0:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY + red.height < HEIGHT - 15:
        red.y += VELOCITY

def draw_window(red, yellow):
    GAME_WINDOW.fill(WHITE)
    pygame.draw.rect(GAME_WINDOW, BLACK, BORDER)
    GAME_WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    GAME_WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def main():
    
    red = pygame.Rect(925, 350, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(275, 350, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            # If user closes the window
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        
        # Yellow Spaceship Movement
        handle_yellow_movement(keys_pressed, yellow)
        # Red Spaceship Movement
        handle_red_movement(keys_pressed, red)
        
        draw_window(red, yellow)
        
    pygame.quit()
    

if __name__ == '__main__':
    main()
