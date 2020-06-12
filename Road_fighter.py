import pygame
from pygame.locals import *
import time
# import ramdom


WIDTH = 800
HEIGHT = 600

def imagen(filename, transparent=False):
	try: image = pygame.image.load(filename)
except pygame.error, message:
	raise SystemExit, message
image = image.convert()







'''
pygame.init()
 
pantalla = pygame.display.set_mode((800,600))
 
imagen = pygame.image.load("images/title1.png")
 

while True:
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            exit()
    pantalla.blit(imagen,(100,100))
    pygame.display.update()

'''