import random
import random
import pygame

# Величины
WIDTH = 800
HEIGHT = 600
FPS = 60

# инициализация pygame
pygame.init()
clock = pygame.time.Clock()

# Экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Заголовок экрана
pygame.display.set_caption("Космозахватчики")
# Иконка
icon = pygame.image.load("Images/ufo.png")
pygame.display.set_icon(icon)
# Спрайт игрока
playerIMG = pygame.image.load("Images/player.png")
# Спавн
playerX = WIDTH/2 - playerIMG.get_width()
playerY = 500
# Смещение игрока по оси X
playerX_change = 0

# Спрайт противника
enemyIMG = pygame.image.load("Images/enemy.png")
enemyX = random.randint(0, WIDTH - enemyIMG.get_width())
enemyY = random.randint(0, 50)
enemyX_change = 2

# Спрайт пули
bulletIMG = pygame.image.load("Images/bullet.png")
bulletX, bulletY = playerX, playerY
bullet_state = "ready"

# Пуля
def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x, y))


# Игрок
def player(x, y):
    screen.blit(playerIMG, (x, y))


# Противник
def enemy(x, y):
    screen.blit(enemyIMG, (x, y))


# Игровой цикл
running = True
player_speed = 3
player_frequency = 0.04
bounce = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Реакция на нажатия
    if event.type == pygame.KEYUP or not bounce:
        if -player_frequency <= playerX_change <= player_frequency:
            playerX_change = 0
            bounce = True
        elif playerX_change > 0:
            playerX_change -= player_frequency
        elif playerX_change < 0:
            playerX_change += player_frequency
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -player_speed
        if event.key == pygame.K_RIGHT:
            playerX_change = player_speed
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        if bullet_state == "ready":
            bulletX = playerX + playerIMG.get_width()/2 - bulletIMG.get_width()/2
            bullet(bulletX, bulletY)
            bullet_Ychange = random.randint(50, 55) / 10

    if bulletY <= 0 - bulletIMG.get_height():
        bullet_state = "ready"
        bulletY = playerY

    if playerX <= 0 or playerX >= WIDTH - playerIMG.get_width():
        playerX_change = -playerX_change
        bounce = False

    print(playerX_change)

    if enemyX <= 0 or enemyX >= WIDTH - enemyIMG.get_width():
        enemyX_change = -enemyX_change
        enemyY += 20

    enemyX += enemyX_change
    playerX += playerX_change
    screen.fill((0, 25, 0))
    if bullet_state == "fire":
        bulletY -= bullet_Ychange
        bullet(bulletX, bulletY)
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.flip()
pygame.quit()
