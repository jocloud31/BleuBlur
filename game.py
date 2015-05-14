import pygame
from pygame.sprite import Sprite
from colors import *


class Block(Sprite):
	def __init__(self, color=bleu, width=50, height=50):
		Sprite.__init__(self)

		self.image = pygame.Surface((width, height))

		self.image.fill(color)

		self.rect = self.image.get_rect()

if __name__ == "__main__":
	pygame.init()

	window_size = window_width, window_height = 640, 480
	window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

	pygame.display.set_caption("Bleu Blur")

	window.fill(sky)

	clock = pygame.time.Clock()
	FPS = 60

	block_group = pygame.sprite.Group()

	sanic = Block()
	block_group.add(sanic)

	block_group.draw(window)

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		clock.tick(FPS)
		pygame.display.update()

	pygame.quit()
	quit()
