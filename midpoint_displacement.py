import random
import pygame

from pygame.locals import *

def displace(coordinates, max_displacement, mid_point_y):

	temp_coords = []

	for x in range(len(coordinates) - 1):

		pos0 = coordinates[x] # Get start position
		pos1 = coordinates[x + 1] # Get end position

		# Average out coordinates
		new_x_pos = (pos0[0] + pos1[0]) / 2.0 
		avg_y_pos = (pos0[1] + pos1[1] ) / 2
		new_y_pos = avg_y_pos + random.uniform(-max_displacement, max_displacement)

		temp_coords.append((new_x_pos, new_y_pos))

	# Add and sort coordinates by x value
	coordinates += temp_coords
	coordinates = sorted(coordinates, key=lambda x: x[0])

	return coordinates

def mid_point_displacement(displacements, max_displacement, scale):

	screen_size = 500, 500 # width and height

	# Start pygame
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption("Mid Point Displacement")


	# initialize the displacement and coordinates
	mid_point_x = screen_size[0] / 2 
	mid_point_y = screen_size[1] / 2
	coordinates = [(0, mid_point_y), (screen_size[0], mid_point_y)]

	# Create coordinates
	for i in range(displacements):
		coordinates = displace(coordinates, max_displacement, mid_point_y)
		max_displacement *= scale # Scale down max displacement

	# Draw white background
	background = pygame.Surface(screen.get_size())
	background.convert()
	background.fill([255, 255, 255])

	while True:
		
		# Handle events
		for event in pygame.event.get():

			if event.type == QUIT: # Close the game
				pygame.quit()
				quit()

		# Draw background
		screen.blit(background, (0, 0))
		pygame.draw.lines(screen, [0, 0, 0], False, coordinates, 1)

		pygame.display.update()
		clock.tick(15)

if __name__ == "__main__":
	mid_point_displacement(20, 250, 0.4)