import pygame
from const import *

class BackgroundTile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, parallax_factor):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.parallax_factor = parallax_factor

class Para_BG(pygame.sprite.Group):
    def __init__(self, scale = 4):
        super().__init__()
        raw_bg = [pygame.image.load(f"assets/bg/bg_{i}.png") for i in range(0,5)]
        self.bg_imgs = [pygame.transform.scale_by(pic, scale) for pic in raw_bg]
        self.bg_widths = [pic.get_width() for pic in self.bg_imgs]
        self.scroll = 0
        self.speed = 10
        self.parallax_factor = 1
        self.create_background_tiles()

    def create_background_tiles(self):
        for i, image in enumerate(self.bg_imgs):
            num_tiles = SCREEN_WIDTH // image.get_width() +2
            print(num_tiles)
            for j in range(num_tiles):
                self.add(BackgroundTile(image, j*image.get_width(),0, i*self.parallax_factor))

    def update(self):
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #     self.scroll += self.speed
        # elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        #     self.scroll -= self.speed

        if self.scroll < 0:
            self.scroll = SCREEN_WIDTH

        for sprite in self.sprites():
            if sprite.rect.right < 0:
                sprite.rect.left = sprite.rect.width
            sprite.rect.x -= sprite.parallax_factor

    # def draw(self, win):
    #     self.draw(win)
        # for i in range(0,5):
        #     offset = self.scroll * i * self.parallax_factor
        #     offset = offset%self.bg_widths[i]
        #     win.blit(self.bg_imgs[i],(offset,0))
        #     win.blit(self.bg_imgs[i],(-self.bg_widths[i]+offset,0))
