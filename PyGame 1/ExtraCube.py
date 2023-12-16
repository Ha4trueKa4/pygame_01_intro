import pygame

width, height = 300, 300
center = width // 3


try:
    w, hue = map(int, input().split())
    if not 0 <= hue <= 360 or w % 4 != 0 or w > 100:
        raise ValueError
    else:
        screen = pygame.display.set_mode((width, height))
        pygame.init()
        pygame.display.set_caption('Куб')

        def draw():
            screen.fill((0, 0, 0))

            color1 = pygame.Color(255, 255, 255)
            hsv1 = color1.hsva
            color1.hsva = (hue, hsv1[1] + 100, hsv1[2], hsv1[3])

            color2 = pygame.Color(255, 255, 255)
            hsv2 = color2.hsva
            color2.hsva = (hue, hsv2[1] + 100, hsv2[2] - 25, hsv2[3])

            color3 = pygame.Color(255, 255, 255)
            hsv3 = color3.hsva
            color3.hsva = (hue, hsv3[1] + 100, hsv3[2] - 50, hsv3[3])

            pygame.draw.rect(screen, color2, (center, center, w, w))

            pygame.draw.polygon(screen, color1,
                                ((center, center), (center + w, center), (center + w + w // 2, center - w // 2),
                                 (center + w // 2, center - w // 2)))
            pygame.draw.polygon(screen, color3,
                                ((center + w, center), (center + w + w // 2, center - w // 2),
                                 (center + w + w // 2, center + w // 2),
                                 (center + w, center + w)))


        draw()

        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()

        pygame.quit()
except ValueError:
    print('Неправильный формат ввода')