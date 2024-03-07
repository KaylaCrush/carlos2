
import spritesheet, pygame

sprite_sheet_image = pygame.image.load('assets/carlos_sprites.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

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
