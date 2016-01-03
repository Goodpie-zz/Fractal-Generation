import random
import pygame
from pygame.locals import *
import math

"""
Based heavily off of https://github.com/hunterloftis/playfuljs-demos/blob/gh-pages/terrain/index.html#L65 and
http://www.bluh.org/code-the-diamond-square-algorithm/ with majority of theory from http://www.gameprogrammer.com/fractal.html
"""

class DiamondSquare:

	def __init__(self, size, roughness):

		self.size = (2 ** size) + 1
		self.max = self.size - 1
		self.roughness = roughness
		self.make_grid(self.size)
		self.divide(self.max) # Start

	# Sets x,y position in self.grid
	def set(self, x, y, val):
		self.grid[x + self.size * y] = val;

	# Get's value of x, y in self.grid
	def get(self, x, y):
		if (x < 0 or x > self.max or y < 0 or y > self.max):
			return -1
		return self.grid[x + self.size * y]

	# Clamps x between min and max
	def clamp(self, x, min, max):

		if (x < min):
			x = min
		elif (x > max):
			x = max

		return x

	# Main iteration
	def divide(self, size):

		x = size / 2
		y = size / 2
		half = size / 2
		scale = self.roughness * size

		if (half < 1):
			return

		# Square
		for y in range(half, self.max, size):
			for x in range(half, self.max, size):
				s_scale = random.uniform(0, 1) * scale * 2 - scale
				self.square(x, y, half, s_scale)

		# Diamond
		for y in range(0, self.max + 1, half):
			for x in range((y + half) % size, self.max + 1, size):
				d_scale = random.uniform(0, 1) * scale * 2 - scale
				self.diamond(x, y, half, d_scale)

		self.divide(size / 2) 

	def square(self, x, y, size, scale):

		top_left = self.get(x - size, y - size)
		top_right = self.get(x + size, y - size)
		bottom_left = self.get(x + size, y + size)
		bottom_right = self.get(x - size, y + size)

		average = ((top_left + top_right + bottom_left + bottom_right) / 4)
		self.set(x, y, self.clamp(average + scale, 0, 1))

	def diamond(self, x, y, size, scale):


		top = self.get(x, y - size)
		right = self.get(x + size, y)
		bottom = self.get(x, y + size)
		left = self.get(x - size, y)

		average = ((top + right + bottom + left) / 4)
		self.set(x, y, self.clamp(average + scale, 0, 1))

	def make_grid(self, size):

		self.grid = []

		# Make the grid
		for x in range(size * size):
			self.grid.append(-1)

		# Base value
		self.set(0, 0, 1)
		self.set(self.max, 0, 0.5)
		self.set(self.max, self.max, 0)
		self.set(0, self.max, 0.5)

	# Returns a 2D array of the grid
	# Used for easier readability and manipulation
	def get_grid_2D(self):
		grid_2d = [self.grid[x:x + self.size] for x in range(0, len(self.grid) , self.size)]
		return grid_2d

# Draws a square at x, y with grayscale color value
class Square(pygame.sprite.Sprite):

	def __init__(self, x, y, size, scale):

		pygame.sprite.Sprite.__init__(self) # Init pygame sprite object=
		color = int(scale * 255)
		self.x = x
		self.y = y
		self.image = pygame.Surface([size[0], size[1]])
		self.image.fill([color, color, color])
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

# Draws the diamon square grid with pygame
def diamond_square(grid):

	pygame.init()

	# Determine block size based on default screen size and then determine screen size. 
	# This prevents visual artifacts
	screen_size = 500, 500
	block_size = int(math.ceil(screen_size[0] / (len(grid[0]) * 1.0))), int(math.ceil(screen_size[1] / (len(grid) * 1.0)))
	screen_size = len(grid[0]) * block_size[0], len(grid) * block_size[1]

	# Basic pygame initialisation
	screen = pygame.display.set_mode(screen_size)
	clock = pygame.time.Clock()
	pygame.display.set_caption("DiamondSqaure")

	# Create squares every x, y position
	y_pos = 0
	squares = []
	for y in range(len(grid)):
		x_pos = 0
		for x in range(len(grid)):
			squares.append(Square(x_pos * block_size[0], y_pos * block_size[1], block_size, grid[y_pos][x_pos]))
			x_pos += 1
		y_pos += 1

	# Create sprite group for easy updating
	square_sprites = pygame.sprite.Group(squares)

	while True:

		# Draw background
		background = pygame.Surface(screen.get_size())
		background = background.convert()
		background.fill([255, 255, 255])
		screen.blit(background, (0, 0))

		# Handle events
		for event in pygame.event.get():

			if event.type == QUIT: # Close the game
				pygame.quit()
				quit()

		# Updates sprites
		square_sprites.clear(screen, background)
		square_sprites.update()
		square_sprites.draw(screen)

		# Update screen
		pygame.display.update()
		clock.tick(60)

# Any roughness value above 0.3 doesn't really provide nice results
a = DiamondSquare(8, 0.05)
grid = a.get_grid_2D()
diamond_square(grid)
