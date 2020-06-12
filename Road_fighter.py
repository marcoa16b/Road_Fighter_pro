import pygame
from pygame.locals import *
import time
# import ramdom





pygame.init()
 
pantalla = pygame.display.set_mode((800,600))
 
imagen = pygame.image.load("images/title1.png")
 

while True:
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            exit()
    pantalla.blit(imagen,(100,100))
    pygame.display.update()

