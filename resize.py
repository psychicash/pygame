import pygame

from sys import exit

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

background_image = 'gear2.png'

pygame.init()
Main_Screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE, 32)

background = pygame.image.load(background_image).convert()

while True:

    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    elif event.type == pygame.VIDEORESIZE:
        background = pygame.image.load(background_image).convert()
        SCREEN_SIZE = event.size
        Main_Screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE, 32)
        background = pygame.transform.scale(background, SCREEN_SIZE)
        pygame.display.set_caption("Window resized to " + str(event.size))

    SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE
    for y in range(0, SCREEN_HEIGHT, background.get_height()):
        for x in range(0, SCREEN_WIDTH, background.get_width()):
            Main_Screen.blit(background, (x, y))

    pygame.display.update()
