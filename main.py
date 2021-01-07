import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()
sleep(10)
pygame.mixer.music.load('scary.mp3')
pygame.mixer.music.play()
sleep(0)
image = pygame.image.load('scry.jpg')
window.blit(image,(0,0))
pygame.display.update()
sleep(5)

