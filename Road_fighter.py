import pygame, time
from pygame.locals import *

ancho_pantalla = 800
alto_pantalla = 600
blanco = 255, 255, 255
negro = 0, 0, 0
azul = 0, 0, 255
rojo = 255, 0, 0
verde = 0,255,0
amarillo = 255,255,0
pantalla = pygame.display.set_mode((ancho_pantalla,alto_pantalla))
pygame.display.set_caption('Snake')
reloj = pygame.time.Clock()

background = pygame.image.load('Images/background.png')
title = pygame.image.load('Images/title.png')
start = pygame.image.load('Images/start.png')
complete = pygame.image.load('Images/complete.png')
pause_img = pygame.image.load('Images/pause.png')
car_one = pygame.image.load('Images/car_1.png')
car_two = pygame.image.load('Images/car_2.png')
car_three = pygame.image.load('Images/car_3.png')
truck = pygame.image.load('Images/truck.png')
car_left = pygame.image.load('Images/left.png')
car_right = pygame.image.load('Images/right.png')
crash = pygame.image.load('Images/crash_1.png')

#==================================================

# inicializamos el constructor del juego
pygame.init()

#==================================================

#fuentes
pequeñafuente = pygame.font.Font(None, 15)
medianafuente = pygame.font.Font(None, 30)
grandefuente = pygame.font.Font(None, 80)

#==================================================

#funciones a usar dentro del juego

#==================================================

def objetotexto(texto,color,tamaño):
	if tamaño == "pequeño":
		textosuperficie = pequeñafuente.render(texto,True,color)
	if tamaño == "mediano":
		textosuperficie = medianafuente.render(texto,True,color)
	if tamaño == "grande":
		textosuperficie = grandefuente.render(texto,True,color)
	return textosuperficie, textosuperficie.get_rect()

#==================================================

def mensaje(msg,color,desplazamientoY=0,tamaño="pequeño"):
	textosuperficie, textorect = objetotexto(msg,color,tamaño)
	textorect.center = (int(ancho_pantalla/2)), (int(alto_pantalla/2))+desplazamientoY
	pantalla.blit(textosuperficie, textorect)

#==================================================

def introduccion():

	introjuego = True

	while introjuego:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				introjuego = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					gameloop()
					introjuego = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					opciones()
					introjuego = False
			#if event.type == pygame.KEYDOWN:
				#if event.key == pygame.K_x:
					#introjuego = False
			pantalla.fill(blanco)
			pantalla.blit(title, (0, 0))
			mensaje("presione S para iniciar, o presione P para opciones, X para salir", azul, tamaño="pequeño")
			pygame.display.update()
			reloj.tick(15)
#==================================================
def opciones():

	retroceso = True

	while retroceso:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				retroseso = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x:
					introduccion()
					retroceso = False
			pantalla.fill(blanco)
			mensaje("Opciones del juego",azul,-100,tamaño="grande")
			pygame.display.update()
			reloj.tick(15)
#==================================================
def gameloop():

	salir = False
	while not salir:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x:
					introduccion()
					retroceso = False
			pantalla.fill(blanco)
			mensaje("Bucle principal del juego",rojo,tamaño="grande")
			pygame.display.update()
			reloj.tick(15)
#==================================================

introduccion()
quit()
gameloop()