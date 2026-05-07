# crear una ciudad de hierro o parque de atracciones usando los elmentos graficos vistos con pygame 
import math
import pygame
import sys

pygame.init()
ventana = pygame.display.set_mode((1000, 700))

# Colores
Nigga = (0, 0, 0)
Derechos = (255, 255, 255)
gren= (0, 255, 0)
Cian = (0, 255, 255)
marron = (139, 69, 19)
#variables
pi = math.pi

# Fondo del cielo
ventana.fill(Cian)

# Hacemos los soportes de la rueda de la fortuna
pygame.draw.line(ventana, Nigga, (200, 700), (450, 450), 20)
pygame.draw.line(ventana, Nigga, (800, 700), (550, 450), 20)
pygame.draw.line(ventana, marron, (400, 450), (600,450), 10)
pygame.draw.line(ventana, Nigga, (500, 250), (500, 450), 5)
pygame.draw.line(ventana, Nigga, (400, 350), (600, 350), 5)
pygame.draw.line(ventana, Nigga, (350, 250), (650, 450), 5)

# Hacemos la rueda de la fortuna
pygame.draw.circle(ventana, Nigga, (500, 350), 100, 9)

# Hacemos el suelo
pygame.draw.line(ventana, gren, (0, 700), (1000, 700), 100)



# bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()