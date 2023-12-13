import pygame
#Задание Мишень
width, height = 500, 500
center = width // 2, height // 2

screen = pygame.display.set_mode((width, height))
pygame.init()

n, k = int(input()), int(input())


def draw():
    screen.fill((0, 0, 0))
    r = width // 2
    for i in range(1, k + 2):
        if i % 3 == 1:
            color = (0, 0, 255)
        elif i % 3 == 2:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)
        pygame.draw.circle(screen, color, center, r)
        r -= n


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
