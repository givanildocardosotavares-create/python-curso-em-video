'''Faça um programa que abre e reproduz o áudio de um arquivo MP3.'''

import pygame

pygame.mixer.init()
pygame.mixer.music.load("mundo-01/exe021.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.wait(100)