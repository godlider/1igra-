import pygame
import random
import os

pygame.init()

# Устанавливаем размеры окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Тир")

# Цвета
white = (255, 255, 255)

# Параметры цели
target_width = 50
target_height = 50
target_x = random.randint(0, screen_width - target_width)
target_y = random.randint(0, screen_height - target_height)

# Параметры движения цели
target_speed = 5
target_direction = random.choice(['up', 'down', 'left', 'right'])

# Параметры попаданий
hits = 0

# Параметры скорости цели
target_speed_input = int(input("Введите скорость движения цели (1-10): ")) # Добавляем возможность выбора скорости цели
target_speed = target_speed_input

# Основной игровой цикл
running = True
while running:
    screen.fill(white)

    # Рисуем цель
    target_image = pygame.image.load(os.path.join("img", "target.png"))

    # Отображаем количество попаданий
    font = pygame.font.Font(None, 36)
    text = font.render("Попаданий: " + str(hits), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Движение цели с учетом скорости
    if target_direction == 'up':
        target_y -= target_speed
    elif target_direction == 'down':
        target_y += target_speed
    elif target_direction == 'left':
        target_x -= target_speed
    elif target_direction == 'right':
        target_x += target_speed

    # Проверка выхода цели за границы экрана
    if target_x < 0:
        target_x = 0
        target_direction = random.choice(['down', 'left', 'right'])
    elif target_x > screen_width - target_width:
        target_x = screen_width - target_width
        target_direction = random.choice(['up', 'left', 'right'])
    if target_y < 0:
        target_y = 0
        target_direction = random.choice(['up', 'right', 'down'])
    elif target_y > screen_height - target_height:
        target_y = screen_height - target_height
        target_direction = random.choice(['up', 'left', 'down'])

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1
                target_x = random.randint(0, screen_width - target_width)
                target_y = random.randint(0, screen_height - target_height)
                target_direction = random.choice(['up', 'down', 'left', 'right'])

    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()