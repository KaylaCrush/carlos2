import pygame, spritesheet

class FloorTile(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 32, height = 32):
        super().__init__()
        self.image = pygame.image.load('assets/block.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4

    def update(self):
        self.rect.x -= self.speed
