import pygame
import sys
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((400, 585))
image = pygame.image.load('Lute.jpg')


font = pygame.font.SysFont('Sans', 58)
text = font.render("Anyway", True, (255, 255, 255))
text2 = font.render("Here's Wonderwall", True, (255, 255, 255))
screen.blit(image, (0, 0))
screen.blit(text, (115, 0))
screen.blit(text2, (0, 500))


pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()