import pygame

pygame.init()
pygame.mixer.init()
explosion_sound = pygame.mixer.Sound("sound/vxriv.wav")
explosion_sound.play()

while pygame.mixer.get_busy():
    pygame.time.delay(100)

pygame.quit()