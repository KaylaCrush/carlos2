
import pygame
from const import *
from floortile import FloorTile
# Initialize Pygame
pygame.init()


# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Carlos: THE EXPERIENCE")

from background import *
from player import *
from floortile import *

# Create player object
player = Player()
bg = Para_BG()

# # Create sprite group and add player to it
all_sprites = pygame.sprite.Group()
floor_tiles = pygame.sprite.Group()

all_sprites.add(player)

# def spawn_tile(x,y):
#     floor_tile = FloorTile(x,y, SCREEN_WIDTH//2)
#     all_sprites.add(floor_tile)
#     floor_tiles.add(floor_tile)
# spawn_tile(0,SCREEN_HEIGHT-32)
# spawn_tile(SCREEN_WIDTH//2,SCREEN_HEIGHT-64)
# spawn_tile(SCREEN_WIDTH,SCREEN_HEIGHT-128)
for i in range(5):
    floor_tiles.add(FloorTile(32*i,SCREEN_HEIGHT-32))
# Main loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            player.relocate(pygame.mouse.get_pos())

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move_right()
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
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
    floor_tiles.draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
