import pygame
#Задание Шахматная клетка

try:
    width, n = map(int, input().split())
    size = width // n

    white = (255, 255, 255)
    black = (0, 0, 0)

    screen = pygame.display.set_mode((width, width))
    pygame.init()


    def draw():
        screen.fill((0, 0, 0))

        x = size

        y = width - size
        for i in range(n):
            while x < width:
                screen.fill(white, (x, y, size, size))
                x += size * 2
            y -= size
            if i % 2 == 0:
                x = 0
            else:
                x = size


    draw()

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()
except ValueError:
    print('Неправильный формат ввода')

