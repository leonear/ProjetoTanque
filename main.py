import pygame;
from pygame.locals import *
from sys import exit

pygame.init() #inicia diversas funcionalidades do pygame
SCREEN_SIZE = (800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32) #retorna uma tela pronta com a dimensão passada por parametro

tank = pygame.image.load('tanque.png').convert_alpha()
tank = pygame.transform.flip(tank, False, True)
DEFAULT_IMAGE_SIZE = (200, 100)
tank = pygame.transform.scale(tank, DEFAULT_IMAGE_SIZE)

x,y = 0,0
move_x, move_y = 0,0
rotation = 0  # Ângulo de rotação do tanque



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
        #    (mouseX, mouseY) = pygame.mouse.get_pos()
        #    move_x = mouseX
        #    move_y = mouseY

        keys = pygame.key.get_pressed()
        if event.type == KEYDOWN:
            if event.key==K_LEFT:
                move_x=-10
                rotation = 180

            if event.key==K_RIGHT:
                move_x=+10
                rotation = 0
            if event.key == K_UP:
                move_y=-10
            if event.key == K_DOWN:
               move_y=+10
        if event.type == KEYUP:
            if event.key == K_LEFT:
                move_x=0
            if event.key == K_RIGHT:
               move_x=0
            if event.key == K_UP:
                move_y=0
            if event.key == K_DOWN:
                move_y=0

        x += move_x
        y += move_y

#        x = move_x
#        y = move_y

        screen.fill((255,255,255))
        rotated_tank = pygame.transform.rotate(tank, rotation)
        tank_rect = rotated_tank.get_rect(center=(x, y))
        screen.blit(rotated_tank, tank_rect.topleft)
        pygame.display.update()
