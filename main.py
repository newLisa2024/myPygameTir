import pygame
import random
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("img/e6eda1.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 50
target_height = 50

target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint(0,SCREEN_HEIGHT - target_height)

target_dx = random.randint(-5, 5)
target_dy = random.randint(-5, 5)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            score += 1  # Увеличение счета при успешном попадании
            target_dx = random.randint(-5, 5)  # Задаем новое случайное направление движения по X
            target_dy = random.randint(-5, 5)  # Задаем новое случайное направление движения по Y

            # Обновляем положение цели
        target_x += target_dx
        target_y += target_dy

        # Ограничение выхода цели за пределы экрана
        if target_x < 0 or target_x > SCREEN_WIDTH - target_width:
            target_dx = -target_dx

        if target_y < 0 or target_y > SCREEN_HEIGHT - target_height:
            target_dy = -target_dy

    score_text = font.render('Очки: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()
pygame.quit()