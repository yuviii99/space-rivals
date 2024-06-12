import pygame
from constants import *
import os

# Width and Height of the Game Window
WIDTH, HEIGHT = 1200, 800

FPS = 60
VELOCITY = 5
BULLET_VELOCITY = 7
MAX_BULLETS = 5

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

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'space.png')), (WIDTH, HEIGHT))

# Separating Line
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

# Bullet hit events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


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
        

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
    

def draw_window(red, yellow, yellow_bullets, red_bullets):
    GAME_WINDOW.blit(SPACE, (0, 0))
    pygame.draw.rect(GAME_WINDOW, BLACK, BORDER)
    GAME_WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    GAME_WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    
    for bullet in yellow_bullets:
        pygame.draw.rect(GAME_WINDOW, YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(GAME_WINDOW, RED, bullet)
    pygame.display.update()

def main():
    
    red = pygame.Rect(925, 350, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(275, 350, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            # If user closes the window
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RALT and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    
        
        keys_pressed = pygame.key.get_pressed()
        
        # Yellow Spaceship Movement
        handle_yellow_movement(keys_pressed, yellow)
        # Red Spaceship Movement
        handle_red_movement(keys_pressed, red)
        # Handle Bullets
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        draw_window(red, yellow, yellow_bullets, red_bullets)
        
    pygame.quit()
    

if __name__ == '__main__':
    main()
