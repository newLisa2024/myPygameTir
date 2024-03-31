import pygame
import random
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("img/e6eda1.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target1.png")
explosion_img = pygame.image.load("img/vzryiv.png")  # Загрузка картинки взрыва
# explosion_sound = pygame.mixer.Sound("sound/vxriv.wav")  # Загрузка звука взрыва
target_width = 80
target_height = 80

target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint(0,SCREEN_HEIGHT - target_height)

target_dx = random.randint(-5, 5)
target_dy = random.randint(-5, 5)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0
font = pygame.font.Font(None, 36)

explosion_display_time = 250
last_explosion_time = None

running = True
while running:
    current_time = pygame.time.get_ticks()
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
               # explosion_sound.play()
                last_explosion_time = current_time
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            score += 1
            target_dx = random.randint(-5, 5)
            target_dy = random.randint(-5, 5)

        target_x += target_dx
        target_y += target_dy

        if target_x < 0 or target_x > SCREEN_WIDTH - target_width:
            target_dx = -target_dx

        if target_y < 0 or target_y > SCREEN_HEIGHT - target_height:
            target_dy = -target_dy

        if last_explosion_time and current_time - last_explosion_time < explosion_display_time:
            screen.blit(explosion_img, (target_x, target_y))
        else:
            screen.blit(target_img, (target_x, target_y))

    score_text = font.render('Очки: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()
pygame.quit()