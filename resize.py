'''
NOTE: The original code to this comes from exercises in the Beginning Python Games Development with Pygame Second Edition by
Harrison Kinsley and Will McGugan.  I have had to make some adjustments from their code as pygame has had some major updates.

Also... soon the code will reorganized and isolated into it's own function to be used with any and all assets within whatever
project you are currently working on.



'''

import pygame

from sys import exit

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

background_image = 'gear2.png'

#replace gear2.png with any background immage, I suggest something roughly the same size as the width/height 's begining dimensions)


pygame.init()
Main_Screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE, 32)

background = pygame.image.load(background_image).convert()

while True:

    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    elif event.type == pygame.VIDEORESIZE:
        #on videoreize event, this gets run
        #the background has to be reinitialized or it will get distorted with every resize
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
