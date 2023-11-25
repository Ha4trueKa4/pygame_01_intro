import pygame

# Задание 2:
# 1. Допишите код примера, чтобы он стал полноценной программой pygame.
# 2. "Продолжите ряд": выведите ещё один квадрат поверх существующих
#     с другими значениями параметров color.hsva.

size = width, height = (400, 300)
screen = pygame.display.set_mode(size)
pygame.init()

def draw_square(screen):
    color = pygame.Color(50, 150, 50)
    pygame.draw.rect(screen, color,
                     (20, 20, 100, 100), 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)

    color.hsva = (hsv[0], hsv[1], hsv[2] - 30, hsv[3])
    pygame.draw.rect(screen, color, (0, 0, 100, 100), 0)

draw_square(screen)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
