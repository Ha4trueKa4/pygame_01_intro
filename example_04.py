# Задание 4:
#   Напишите программу, выводящую на экран оранжевый треугольник с вершинами в точках:
#   (0, 0), (60, 20) и (120, 60)
import pygame

width, height = 200, 100

screen = pygame.display.set_mode((width, height))
pygame.init()

screen.fill((0, 0, 0))
color = pygame.Color(255, 100, 0)

pygame.draw.polygon(screen, color, ((0, 0), (60, 20), (120, 60)))

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
