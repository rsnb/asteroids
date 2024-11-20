import pygame

from constants import *

def main():
	num_pass, num_fail = pygame.init()
	print(f"Stats: passing {num_pass}, failing {num_fail}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:
		screen.fill((0,0,0))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

if __name__ == "__main__":
	main()

