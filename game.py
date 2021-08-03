import pygame

W = 800
H = 600



WINDOW = pygame.display.set_mode((W, H))


def main():
	run = True

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

	pygame.quit()



if __name__ == "__main__":
	main()