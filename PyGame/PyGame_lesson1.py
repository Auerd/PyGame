import pygame

WIDTH = 800  # Ширина окна
HEIGHT = 600  # Высота

# Кадры в сек
FPS = 30


RED = (255, 0, 0)  # Красный цвет в RGB
GREEN = (0, 255, 0)  # Зелёный цвет в RGB
BLUE = (0, 0, 255)  # Голубой цвет в RGB
WHITE = (255, 255, 255)  # Белый
BLACK = (0, 0, 0)  # Чёрный

GREEN_BLUE = (3, 118, 71)  # Бирюзовый


pygame.init()  # Запуск PyGame
pygame.mixer.init()  # Звук

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(
    "Second Game"
)
clock = pygame.time.Clock()


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Обновление и визуализация
    screen.fill(RED)
    pygame.display.flip()


pygame.quit()
