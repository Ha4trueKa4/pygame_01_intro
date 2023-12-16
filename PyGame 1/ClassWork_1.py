import pygame
#Задание Крест
try:
    width, height = map(int, input().split())
    screen = pygame.display.set_mode((width, height))
    pygame.init()


    def draw():
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), 5)
        pygame.draw.line(screen, (255, 255, 255), (width, 0), (0, height), 5)


    draw()

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()
except ValueError:
    print('Неправильный формат ввода')
