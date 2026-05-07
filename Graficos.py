import math
import pygame
import sys
import random

pygame.init()

ventana = pygame.display.set_mode((400, 400))

#coloritos
CIAN = (0, 255, 255)
BLA = (0, 0, 0)
RED = (255, 0, 0)
GRE = (0, 255, 0)
BLU = (0, 0, 255)
WHI = (255, 255, 255)
naranja = (255, 165, 0)
rancol = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
rosado = (237, 138, 237)



#variables :P
pi = math.pi

# formas, yo que sé? :P
ventana.fill(BLA)
# Formas
pygame.draw.line(ventana, WHI, (0, 0), (400, 400), 5)
pygame.draw.line(ventana, WHI, (400, 0), (0, 400), 5)
pygame.draw.line(ventana, WHI, (200, 0), (200, 400), 5)
pygame.draw.line(ventana, WHI, (0, 200), (400, 200), 5)

pygame.draw.line(ventana, RED, (0, 200), (200, 0), 5)
pygame.draw.line(ventana, RED, (400, 200), (200, 400), 5)
pygame.draw.line(ventana, RED, (200, 0), (400, 200), 5)
pygame.draw.line(ventana, RED, (200, 400), (0, 200), 5)

pygame.draw.rect(ventana, rosado, (150, 150, 50, 50))
pygame.draw.rect(ventana, GRE, ((200, 200), (50, 50)), 3)

puntos_3 = [(100, 200), (200, 300), (100, 400), (0, 300)]
pygame.draw.polygon(ventana, BLU, puntos_3)

puntos_1 = [(300, 0), (400, 100), (300, 200), (200, 100)]
pygame.draw.polygon(ventana, GRE, puntos_1)

puntos_2 = [(200, 0), (230, 170), (400, 200), (230, 230), (200, 400), (170, 230), (0, 200), (170, 170)]
pygame.draw.polygon(ventana, RED, puntos_2)

# circulo 
pygame.draw.circle(ventana, WHI, (300, 300), 100, 5)

# Ellipse 
pygame.draw.ellipse(ventana, GRE, (200, 250, 200, 100), 5)
pygame.draw.ellipse(ventana, naranja, (250, 200, 100, 200), 5)

# arcos
pygame.draw.arc(ventana, CIAN, (200, 0, 200, 200), 0, 7*pi/4, 100)

# Texto
fuente = pygame.font.SysFont("Arial", 35, 1, 1)
texto = fuente.render("Lorenzo perez", 1, WHI)
ventana.blit(texto, (0, 50))

centro = pygame.image.load("esprectro_embrujado.png")

# bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        ventana.blit(centro, (200, 200))


    pygame.display.flip()