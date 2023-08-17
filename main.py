#Leonardo Medeiros Silva Aparicio - 32223617
import pygame
from pygame.locals import *
from sys import exit

pygame.init() #inicia diversas funcionalidades do pygame
SCREEN_SIZE = (800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32) #retorna uma tela pronta com a dimensão passada por parametro

tank = pygame.image.load('tanque2.png').convert_alpha()
DEFAULT_IMAGE_SIZE = (240, 240)
tank = pygame.transform.scale(tank, DEFAULT_IMAGE_SIZE)

#----- Tentativa com a primeira imagem -----
#tank_flip = pygame.transform.flip(tank, True, False)
#tank_image = tank

x,y = 0,0
move_x, move_y = 0,0
rotation = 0  # Ângulo de rotação do tanque




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

#----------Movendo o tanque com o mouse!-----------
#        if event.type == pygame.MOUSEMOTION:
#           (mouseX, mouseY) = pygame.mouse.get_pos()
#           move_x = mouseX
#           move_y = mouseY

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
                rotation = 90
            if event.key == K_RIGHT:
                move_x = 1
                rotation = -90
            if event.key == K_UP:
                move_y = -1
                rotation = 0
            if event.key == K_DOWN:
                move_y = 1
                rotation = 180
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                move_x = 0
            if event.key == K_UP or event.key == K_DOWN:
                move_y = 0

    x += move_x
    y += move_y

#   x = move_x #código para o movimento com o mouse
#   y = move_y #código para o movimento com o mouse

    screen.fill((255, 255, 255))
    rotated_tank = pygame.transform.rotate(tank, rotation)
    tank_rect = rotated_tank.get_rect(center=(x, y))
    screen.blit(rotated_tank, tank_rect.topleft)
    pygame.display.update()

