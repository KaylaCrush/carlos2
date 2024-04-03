import pygame
SPRITE_WIDTH = 64
SPRITE_HEIGHT = 64

class SpriteSheet():
	def __init__(self, image, grid_width = 64, grid_height = 64,):
		self.sheet = image
		self.grid_width = grid_width
		self.grid_height = grid_height

	def get_image(self, x, y, scale = 1, color = (0,0,0), marg_right = 0, magrg_left = 0, marg_top = 0, marg_bot = 0):
		image = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT)).convert_alpha()
		rect = ((y*SPRITE_HEIGHT), (x*SPRITE_WIDTH), ((y+1)*SPRITE_WIDTH), ((x+1)*SPRITE_HEIGHT))
		image.blit(self.sheet, (0, 0), rect)
		image = pygame.transform.scale(image, (SPRITE_WIDTH * scale, SPRITE_HEIGHT * scale))
		image.set_colorkey(color)

		return image
