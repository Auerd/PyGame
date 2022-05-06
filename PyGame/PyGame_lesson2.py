import pygame

WIDTH = 1365  # Ширина окна
HEIGHT = 700  # Высота

# Кадры в сек
FPS = 60


RED = (255, 0, 0)  # Красный цвет в RGB
GREEN = (0, 255, 0)  # Зелёный цвет в RGB
BLUE = (0, 0, 255)  # Голубой цвет в RGB
WHITE = (255, 255, 255)  # Белый
BLACK = (0, 0, 0)  # Чёрный

GREEN_BLUE = (3, 118, 71)  # Бирюзовый

# Размеры прямоугольника
OBJWIDTH = 20
OBJHEIGHT = 30
# Координаты отображения
x = WIDTH/2 - OBJWIDTH/2
y = HEIGHT/2 - OBJHEIGHT/2
# Cкорость
speed = 10
jump_Count = 10

Key_up = False
Key_down = False
Key_right = False
Key_left = False
Key_jump = False


pygame.init()  # Запуск PyGame
pygame.mixer.init()  # Звук
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Это экран
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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        Key_right = False
        Key_left = True
    elif keys[pygame.K_RIGHT] and x < (WIDTH - OBJWIDTH):
        x += speed
        Key_left = False
        Key_right = True

 # if keys[pygame.K_UP] and y > 0:
 #     y -= speed
 #     Key_down = False
 #     Key_up = True
 # elif keys[pygame.K_DOWN] and y < (HEIGHT - OBJHEIGHT):
 #     y += speed
 #     Key_up = False
 #     Key_down = True
    if keys[pygame.K_SPACE]:
        Key_jump = True
    if Key_jump:
        if jump_Count >= -10:
            y -= (jump_Count * jump_Count**2) * 0.025
            jump_Count -= 0.5
        else:
            jump_Count = 10
            Key_jump = False

    # Обновление и визуализация
    screen.fill(GREEN)
    pygame.draw.rect(screen, GREEN_BLUE, (x, y, OBJWIDTH, OBJHEIGHT))
    # Переворачиваем доску
    pygame.display.flip()


pygame.quit()
