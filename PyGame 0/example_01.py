import pygame

# Задание 1:
# 1. Измените надпись "Hello, Pygame!" на что-то близкое вам
# 2. Выведите измененную надпись цветом Яндекса: https://clck.ru/36jRKn
# 3. Выведите ещё одну произвольную надпись снизу более мелким шрифтом.
#    Выровняйте эту надпись по горизонтали по центру. Используйте другой цвет.


size = width, height = (400, 300)
screen = pygame.display.set_mode(size)
pygame.init()


def draw():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Добрый день!", 1, (255, 204, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0),
                     (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)
    font = pygame.font.Font(None, 30)
    text = font.render("Доброй ночи!", 1, (255, 204, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height - 100 // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0),
                     (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()