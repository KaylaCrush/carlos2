import spritesheet
import pygame
import os

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 640

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player Sprite Example")

sprite_sheet_image = pygame.image.load('assets/carlos_sprites.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

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
        self.parallax_factor = 2
        self.create_background_tiles()

    def create_background_tiles(self):
        for i, image in enumerate(self.bg_imgs):
            num_tiles = SCREEN_WIDTH*2 // image.get_width() +1
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

class Player(pygame.sprite.Sprite):
    def __init__(self, x=100,y=100,scale=1):
        super().__init__()
        self.color = (0,0,0)
        self.animations = {}
        self.scale = scale
        self.load_animations()
        self.image = self.animations['stand']
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initial position
        self.speed = 2
        self.walk_index = 0

    def load_animations(self):
        self.animations['walk_right'] = [sprite_sheet.get_image(11, i, self.scale, self.color) for i in range(9)]
        self.animations['walk_left'] = [sprite_sheet.get_image(9, i, self.scale, self.color) for i in range(9)]
        self.animations['jump_r'] = sprite_sheet.get_image(3,5, self.scale, self.color)
        self.animations['jump_l'] = sprite_sheet.get_image(1,5, self.scale, self.color)
        self.animations['jump'] = sprite_sheet.get_image(2,5, self.scale, self.color)
        self.animations['stand'] = sprite_sheet.get_image(2, 0, self.scale, self.color)

    def update(self):
        # Example: Move the player based on user input
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            #self.rect.x -= self.speed
            self.walk_index = (self.walk_index + .2) % len(self.animations['walk_left'])
            self.image = self.animations['walk_left'][int(self.walk_index)]

        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            #self.rect.x += self.speed
            self.walk_index = (self.walk_index + .2) % len(self.animations['walk_right'])
            self.image = self.animations['walk_right'][int(self.walk_index)]

        else:
            self.image = self.animations['stand']
            self.walk_index = 0

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

    #
    bg.update()
    all_sprites.update()


    # Draw
    screen.fill((255, 255, 255))

    bg.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
