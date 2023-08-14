import pygame;
from pygame.locals import *
from sys import exit

pygame.init() #inicia diversas funcionalidades do pygame
SCREEN_SIZE = (800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32) #retorna uma tela pronta com a dimensão passada por parametro

tank = pygame.image.load('tanque.png').convert()
DEFAULT_IMAGE_SIZE = (200, 100)
tank = pygame.transform.scale(tank, DEFAULT_IMAGE_SIZE)

x,y = 0,0
move_x, move_y = 0,0


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEMOTION:
           (mouseX, mouseY) = pygame.mouse.get_pos()
           move_x = mouseX
           move_y = mouseY



        #if event.type == KEYDOWN:
        #    if event.key==K_LEFT:
        #        move_x=-10
        #if event.type == KEYUP:
        #    if event.key== K_LEFT:
        #        move_x = 0

        #if event.type == KEYDOWN:
        #    if event.key==K_RIGHT:
        #        move_x= +10
        #if event.type == KEYUP:
        #    if event.key== K_RIGHT:
        #        move_x = 0

        #if event.type == KEYDOWN:
        #    if event.key == K_UP:
        #        move_y = -10
        #if event.type == KEYUP:
        #    if event.key == K_UP:
        #        move_y = 0

        #if event.type == KEYDOWN:
        #    if event.key == K_DOWN:
        #        move_y = +10
        #if event.type == KEYUP:
        #    if event.key == K_DOWN:
        #        move_y = 0




        x = move_x
        y = move_y

        screen.fill((255, 255, 255)) #preenche a tela com uma determinada área
        screen.blit(tank,(x,y))


        pygame.display.update()#atualiza o display
