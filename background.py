import pygame
from const import *

class BackgroundTile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

class Para_BG(pygame.sprite.Group):
    def __init__(self, scale = 4):
        super().__init__()
        raw_bg = [pygame.image.load(f"assets/bg/bg_{i}.png") for i in range(0,5)]
        self.bg_imgs = [pygame.transform.scale_by(pic, scale) for pic in raw_bg]
        self.bg_widths = [pic.get_width() for pic in self.bg_imgs]
        self.parallax_factor = 1
        self.create_background_tiles()

    def create_background_tiles(self):
        for i, image in enumerate(self.bg_imgs):
            self.add(BackgroundTile(image, 0, 0, i*self.parallax_factor))
            if i != 0:
                self.add(BackgroundTile(image, image.get_width(), 0, i*self.parallax_factor))

    def update(self):
        for sprite in self.sprites():
            sprite.rect.x -= sprite.speed
            if sprite.rect.right <= 0:
                sprite.rect.left = sprite.rect.width - sprite.speed
