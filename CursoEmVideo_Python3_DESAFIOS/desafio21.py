import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
while(pygame.mixer.music.get_busy()): pass

# import playsound
# playsound.playsound('desafio21.mp3')