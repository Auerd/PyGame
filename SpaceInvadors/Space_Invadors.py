import math
import random
import random
import pygame
from pygame import mixer

# Величины
WIDTH = 800
HEIGHT = 600
FPS = 60

# инициализация pygame
pygame.init()
clock = pygame.time.Clock()

Font = pygame.font.Font

score = 0

font = Font('freesansbold.ttf', 30)
over_font = Font('freesansbold.ttf', 64)

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
enemiesIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 2
num_of_enemies += 1
change_num = 4-num_of_enemies

# спрайт противника
for i in range(num_of_enemies):
    random_size = random.randint(enemyIMG.get_width() - 10, enemyIMG.get_width() + 10)
    enemyX.append(random.randint(0, WIDTH - random_size))
    enemyY.append(change_num*enemyIMG.get_height())
    enemiesIMG.append(pygame.transform.scale(enemyIMG, (random_size, random_size)))
    enemyX_change.append(random_size/30 - 1)
    enemyY_change.append(40)
    change_num += 1

# Спрайт пули
bulletIMG = pygame.image.load("Images/bullet.png")
bulletX, bulletY = playerX, playerY
bullet_state = "ready"
explosion_sound = mixer.Sound('Sounds/explosion.wav')

# Пуля
def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x, y))


# Игрок
def player(x, y):
    screen.blit(playerIMG, (x, y))


# Противники
def enemy(x, y, i):
    screen.blit(enemiesIMG[i], (x, y))


# Игровой цикл
running = True
player_speed = 3
player_frequency = 0.04


# def show_score(score):
#     score = font.render("Очки" + str(score))
#
# def game_over_text():
#     text = font.render("игра окончена", )

def is_collision(enemyY, enemyX, bulletX, bulletY):
    # enemyY = enemyY + enemyIMG.get_height()/2
    # bulletY = bulletY + bulletIMG.get_height()/2
    # enemyX = enemyX + enemyIMG.get_width()/2
    # bulletX = bulletX + bulletIMG.get_width()/2
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 150:
        print(distance)
        return True
    else:
        return False


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Реакция на нажатия
    if event.type == pygame.KEYUP:
        if -player_frequency <= playerX_change <= player_frequency:
            playerX_change = 0
        elif playerX_change > 0:
            playerX_change -= player_frequency
        elif playerX_change < 0:
            playerX_change += player_frequency
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -player_speed
        if event.key == pygame.K_RIGHT:
            playerX_change = player_speed
        if event.key == pygame.K_UP and bullet_state == "ready":
            bulletX = playerX + playerIMG.get_width()/2 - bulletIMG.get_width()/2
            bulletY = playerY
            bullet(bulletX, bulletY)
            bullet_Ychange = random.randint(50, 70) / 10

    if bulletY <= 0 - bulletIMG.get_height():
        bullet_state = "ready"

    if playerX <= -playerIMG.get_width() - 1:
        playerX = WIDTH - 1
    if playerX >= WIDTH:
        playerX = -playerIMG.get_width()

    screen.fill((0, 25, 0))
    playerX += playerX_change
    if bullet_state == "fire":
        bulletY -= bullet_Ychange
        bullet(bulletX, bulletY)

    for i in range(num_of_enemies):
        # if enemyY[i] < 400:
        #     for j in range(num_of_enemies):
        #         enemyY[j] = 2000
        #     game_over_text()
        #     running = False
        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0 or enemyX[i] > WIDTH - enemiesIMG[i].get_width():
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_change[i]
        if is_collision(enemyX[i], enemyY[i], bulletX, bulletY):
            explosion_sound.play()
            enemyY[i] = 2000
        enemy(enemyX[i], enemyY[i], i)
    player(playerX, playerY)
    pygame.display.flip()
pygame.quit()
