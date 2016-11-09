import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((480, 480))
image = pygame.image.load('Happy.jpg')
image2 = pygame.image.load('Sad.jpg')

font = pygame.font.SysFont('Sans', 38)
text = font.render("When You're Having A Nice Day", True, (255, 255, 255))
text2 = font.render("And Drop Your Phone", True, (255, 255, 255))
pygame.time.Clock()

screen.blit(image, (0, 0))
screen.blit(image2, (0, 0))
screen.blit(text, (20, 0))
screen.blit(text2, (90, 400))

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()