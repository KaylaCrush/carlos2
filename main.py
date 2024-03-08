
import pygame
from const import *
# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player Sprite Example")

from background import *
from player import *
from floortile import *

# Create player object
player = Player()
bg = Para_BG()

# Create sprite group and add player to it
all_sprites = pygame.sprite.Group()
floor_tiles = pygame.sprite.Group()

all_sprites.add(player)

floor_tile = FloorTile(5,500)
all_sprites.add(floor_tile)
floor_tiles.add(floor_tile)

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.move_right()
    elif keys[pygame.K_LEFT]:
        player.move_left()
    else:
        player.stand_still()

    if keys[pygame.K_SPACE]:
        player.jump(floor_tiles)

    # Update
    bg.update()
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, floor_tiles, False)
    if hits:
        player.rect.bottom = hits[0].rect.top
        player.vel_y = 0

    # Draw
    bg.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
