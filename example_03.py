import pygame
import random

# Задание 3:
# 1. Допишите код примера, чтобы он стал полноценной программой pygame.
# 2. Оформите код отрисовки в виде функции draw(screen).


width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.init()

for i in range(10000):
    screen.fill(pygame.Color('white'),
                (random.random() * width,
                 random.random() * height, 1, 1))

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
