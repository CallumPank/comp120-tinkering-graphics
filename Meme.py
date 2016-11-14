# Imports Libraries
import pygame
import sys
from pygame.locals import *

# Initialise Pygame
pygame.init()

# Set Caption for display window
pygame.display.set_caption("Meme")

# declare variable 'screen' and set the display window
screen = pygame.display.set_mode((480, 480,))

# Declare variable for image and load it into pygame
image = pygame.image.load('Sad.jpg')

# Declare style and size of font
font = pygame.font.SysFont('Sans', 38)

# Render text and text colour for image
text = font.render("When You're Having A Nice Day", True, (255, 255, 255))
text2 = font.render("And Drop Your Phone", True, (255, 255, 255))

# Blit image to the screen and set coordinates for centre of the screen
screen.blit(image, (0, 0))

# Blit text and to screen and set coordinates
screen.blit(text, (20, 0))
screen.blit(text2, (90, 400))


# Update the full display surface to the screen
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()