import pygame
pygame.init()
pygame.mixer.music.load("D:\Tu-Hai-Kahan(PaglaSongs) (3).mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
pygame.quit()