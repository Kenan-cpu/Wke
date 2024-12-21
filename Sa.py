import pygame
import time
import random

pygame.init()

# Ekran boyutları
width = 800
height = 600

# Renkler
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Ekran oluşturma
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Yılan Oyunu')

# Yılanın başlangıç pozisyonu
x1 = width / 2
y1 = height / 2

# Yılanın hareket hızı
x1_change = 0
y1_change = 0

# Yemek
foodx = round(random.randrange(0, width - 20) / 20) * 20
foody = round(random.randrange(0, height - 20) / 20) * 20

# Yılanın boyutu ve listesi
snake_block = 20
snake_list = []
snake_length = 1

# Oyun döngüsü
clock = pygame.time.Clock()
game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_over = True

    # Yılanın hareketi
    x1 += x1_change
    y1 += y1_change

    screen.fill(black)
    pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
    
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    # Yılanın kendine çarpması kontrolü
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Yılanı çizme
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

    pygame.display.update()

    # Yemek yeme kontrolü
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, width - snake_block) / 20) * 20
        foody = round(random.randrange(0, height - snake_block) / 20) * 20
        snake_length += 1

    clock.tick(15)

pygame.quit()
quit()
