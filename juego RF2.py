import pygame, time, random
from pygame.locals import *

#==================================================
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla,alto_pantalla))
pygame.display.set_caption('Snake')
reloj = pygame.time.Clock()
#==================================================
#colores
#==================================================
blanco = 255, 255, 255
negro = 0, 0, 0
azul = 0, 0, 255
rojo = 255, 0, 0
verde = 0,255,0
amarillo = 255,255,0

#==================================================
# Imagenes
#==================================================
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
#player
#==================================================
car_one = pygame.image.load('Images/car_1.png')
ladoX = 400
ladoY = 300 
velx = 0
vely = 0
#==================================================
# manzana
#==================================================
bloquemanzana = 20
#ladoXmanzana = 250
#ladoYmanzana = 250
#==================================================
# inicializamos el constructor del juego
#==================================================
pygame.init()
#==================================================
#fuentes
#==================================================
pequeñafuente = pygame.font.Font(None, 15)
medianafuente = pygame.font.Font(None, 30)
grandefuente = pygame.font.Font(None, 80)
#==================================================
# entrada de texto, nombre del jugador
#==================================================
base_font = pygame.font.Font(None,32)
user_text = ''
#==================================================
#==================================================
#funciones a usar dentro del juego
#==================================================
def dirmanzana():
    dirXmanz = random.randrange(0,ancho_pantalla - bloquemanzana)
    dirymanz = random.randrange(0,alto_pantalla - bloquemanzana)
    return dirXmanz, dirymanz
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
# ingresar nombre jugador
#==================================================

#==================================================

#==================================================
# boton
#==================================================

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    introjuego = False
            pantalla.fill(blanco)
            pantalla.blit(title, (0,0))
            mensaje("s para iniciar, p para opciones, x para salir",verde,+150, "mediano")
            pygame.display.update()
            reloj.tick(15)

#==================================================


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
            mensaje("instrucciones del juego",azul,-250,tamaño="grande")
            pygame.display.update()
            reloj.tick(15)
#==================================================
def gameloop():

    salir = False
    global ladoX
    global ladoY
    global velx
    dirXmanz,dirYmanz = dirmanzana()

    while not salir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velx = -6
                if event.key == pygame.K_RIGHT:
                    velx = 6
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    velx = 0
                if event.key == pygame.K_RIGHT:
                    velx = 0

        ladoX += velx
        pantalla.fill(blanco)
        pantalla.blit(background, (0,0))
        pygame.draw.rect(pantalla,verde,(ladoX,ladoY,20,20))
        pantalla.blit(car_one, (400, 500))
        
        # colisiones


        pygame.display.update()
        reloj.tick(15)
#==================================================

introduccion()
quit()
gameloop()