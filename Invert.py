# Imports Libraries
import pygame
import sys
from pygame.locals import *

Width = 750
Height = 499


# Initialise Pygame
pygame.init()

# declare variable 'screen' and set the display window
screen = pygame.display.set_mode((Width, Height))


# Declare variable for image and load it into pygame
Rose = pygame.image.load('Roses.jpg')
screen.blit(Rose, (0, 0))
pygame.display.flip()
PixArray = pygame.PixelArray(screen)

def Invert():
    """ Inverts colours of the picture"""
    for Y in range(0, Height):
        for X in range(0, Width):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b

            # Inverts the value
            red = 255 - red
            green = 255 - green
            blue = 255 - blue

            # Updates the Pixel Array
            PixArray[X, Y] = (red, green, blue)


Invert()

# Update the full display surface to the screen
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()