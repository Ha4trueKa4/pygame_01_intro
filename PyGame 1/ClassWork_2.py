import pygame
#Задание Прямоугольник

try:
    width, height = map(int, input().split())
    screen = pygame.display.set_mode((width, height))
    pygame.init()


    def draw():
        screen.fill((0, 0, 0))
        screen.fill((255, 0, 0), (1, 1, width - 2, height - 2))


    draw()

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()

except ValueError:
    print('Неправильный формат ввода')

