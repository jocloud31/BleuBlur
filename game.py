import pygame
from pygame.sprite import Sprite
from colors import *


class Block(Sprite):
	def __init__(self, color, size):
		Sprite.__init__(self)

		self.color = color
		self.image = pygame.Surface(size)
		self.image.fill(self.color)

		self.rect = self.image.get_rect()
		self.hspeed = int(0)
		self.vspeed = int(0)
		self.target_hspeed = 0
		self.target_vspeed = 0
		block_group.append(self)

	def change_speed(self, hspeed_change, vspeed_change):
		if(hspeed_change is not "x"):
			self.target_hspeed = hspeed_change

		if(vspeed_change is not "x"):
			self.target_vspeed = vspeed_change

	def set_position(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def update_block(self):
		self.hspeed += (self.target_hspeed - self.hspeed) * .01
		self.vspeed += (self.target_vspeed - self.vspeed) * .01
		"""if -.1 < self.hspeed < .1:
			self.hspeed = 0
		if -.1 < self.vspeed < .1:
			self.vspeed = 0"""
		self.rect.x += int(self.hspeed)
		self.rect.y += int(self.vspeed)
		self.set_position(self.rect.x, self.rect.y)
		print "H: {0} V: {1}".format(self.hspeed, self.vspeed)

	def draw_to_screen(self):
		window.blit(self.image, [self.rect.x, self.rect.y])

	def gravity_falls(self):
		pass

if __name__ == "__main__":
	pygame.init()

	window_size = window_width, window_height = 640, 480
	window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

	pygame.display.set_caption("Bleu Blur")

	window.fill(sky)

	clock = pygame.time.Clock()
	FPS = 60

	block_group = []

	sky_box = Block(sky, [window_width, window_height])
	sky_box.set_position(0, 0)

	ground = Block(grass, [window_width, 15])
	ground.set_position(0, window_height - 15)

	sanic = Block(bleu, [25, 25])
	sanic.set_position(5, window_height - 40)

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

				if event.key == pygame.K_w:
					sanic.change_speed("x", -5)

				if event.key == pygame.K_s:
					sanic.change_speed("x", 5)

				if event.key == pygame.K_a:
					sanic.change_speed(-5, "x")

				if event.key == pygame.K_d:
					sanic.change_speed(5, "x")

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					sanic.change_speed("x", 0)

				if event.key == pygame.K_s:
					sanic.change_speed("x", 0)

				if event.key == pygame.K_a:
					sanic.change_speed(0, "x")

				if event.key == pygame.K_d:
					sanic.change_speed(0, "x")

		clock.tick(FPS)
		sanic.update_block()
		for item in block_group:
			item.draw_to_screen()
		pygame.display.update()

	pygame.quit()
	quit()
