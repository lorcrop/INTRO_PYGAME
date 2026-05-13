# crear una ciudad de hierro o parque de atracciones usando los elmentos graficos vistos con pygame 
import math
import pygame
import sys
import random

pygame.init()
ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("NIGGAS WHIT ACTITUDE")

# Colores
yelow=(255,255,0)
Nigga = (0, 0, 0)
WHI = (255, 255, 255)
gren= (0, 255, 0)
Cian = (0, 255, 255)
marron = (139, 69, 19)
gris= (128, 128, 128)
naranja=(255,165,0)
metal=(192,192,192)
RED=(255,0,0)
rancol=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#variables
pi = math.pi
XX = 100
MOVIMIENTO = 3

# Fondo
ventana.fill(Cian)



pygame.draw.line(ventana, metal, (70, 530), (300, 300), 30)
pygame.draw.line(ventana, metal, (300, 300), (530, 530), 30)


pygame.draw.circle(ventana, Nigga, (300, 300), 150, 5)

pygame.draw.line(ventana, gris, (300, 150), (300, 450), 5)
pygame.draw.line(ventana, gris, (150, 300), (450, 300), 5)
pygame.draw.line(ventana, gren, (00, 600) , (600, 600), 200)

pygame.draw.rect(ventana, WHI, (275, 150, 50, 50), 5)
pygame.draw.rect(ventana, WHI, (275, 450, 50, 50), 5)
pygame.draw.rect(ventana, WHI, (125, 300, 50, 50), 5)
pygame.draw.rect(ventana, WHI, (425, 300, 50, 50), 5)


# Objeto para la gestión del tiempo
clock = pygame.time.Clock()




# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(Cian)

    # Dibujar estructura
    pygame.draw.line(ventana, metal, (70, 530), (300, 300), 30)
    pygame.draw.line(ventana, metal, (300, 300), (530, 530), 30)
    pygame.draw.circle(ventana, Nigga, (300, 300), 150, 5)
    pygame.draw.line(ventana, gris, (300, 150), (300, 450), 5)
    pygame.draw.line(ventana, gris, (150, 300), (450, 300), 5)
    pygame.draw.line(ventana, gren, (0, 600), (600, 600), 200)

    # Rectángulos
    pygame.draw.rect(ventana, WHI, (275, 150, 50, 50), 5)
    pygame.draw.rect(ventana, WHI, (275, 450, 50, 50), 5)
    pygame.draw.rect(ventana, WHI, (125, 300, 50, 50), 5)
    pygame.draw.rect(ventana, WHI, (425, 300, 50, 50), 5)


# agregamos el nombre
    fuente = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente.render("Lorenzo perez", 1, WHI)
    ventana.blit(texto, (0, 50))


    # movimiento del pacman
    XX = XX + MOVIMIENTO

    if XX >= 450:
        XX = 450
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3

    # Dibujar Pacman
    pygame.draw.arc(ventana, yelow, (XX, 500, 50, 50), math.pi/4, 7*math.pi/4, 100)

    centro = pygame.image.load("esprectro_embrujado.png")

    # Mostrar imagen si se presiona ESCAPE
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        ventana.blit(centro, (200, 200))

    # actualizar visualización de la ventana
    pygame.display.flip()