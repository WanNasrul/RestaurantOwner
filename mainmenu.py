import pygame
import button

from maingame import *

#hello
#create display window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Restaurant Owner!')

# background
bg = pygame.image.load('gameasset/backgroundmainmenu.png')


#load button images
title_img = pygame.image.load('gameasset/gametitle.png').convert_alpha()
start_img = pygame.image.load('gameasset/playbutton.png').convert_alpha()
credit_img = pygame.image.load('gameasset/creditbutton.png').convert_alpha()
exit_img = pygame.image.load('gameasset/quitbutton.png').convert_alpha()


#create button instances
title = button.Button(300, 100, title_img, 0.5)
start_button = button.Button(515, 350, start_img, 0.5)
credit_button = button.Button(515, 450, credit_img, 0.5)
exit_button = button.Button(515, 550, exit_img, 0.5)

#game loop
run = True
while run:

    screen.fill((255,235,216))
    screen.blit(bg, (0,0))
    title.draw(screen)
    
    # print these
    if start_button.draw(screen):
        print('START')
    
    if credit_button.draw(screen):
        print('CREDITS')
        
    if exit_button.draw(screen):
        run = False

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()

pygame.quit()