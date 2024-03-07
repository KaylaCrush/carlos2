
import pygame
from const import *
# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player Sprite Example")


from background import *
from player import *


# Create player object
player = Player()
bg = Para_BG()

# Create sprite group and add player to it
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    bg.update()
    all_sprites.update()


    # Draw
    # screen.fill((255, 255, 255))

    bg.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
