import pygame
#Задание Крест
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.init()


def draw():
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (500, 500), 5)
    pygame.draw.line(screen, (255, 255, 255), (500, 0), (0, 500), 5)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()