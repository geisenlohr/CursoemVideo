# Programa para tocar mp3 no Python

import pygame
pygame.init()
pygame.mixer.music.load('jokertheme.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
