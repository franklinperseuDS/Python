# Faça um programa que abra e reporduza o áudio de um arquivo MP3

import pygame
pygame.init()
print('tocando musica')
pygame.mixer.music.load('exe021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
