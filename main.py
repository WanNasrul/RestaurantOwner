import pygame
import button
from sys import exit #import one thing

# initialize pygame
pygame.init()

# create display window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Restaurant Owner!')

# load images
bg_main_menu = pygame.image.load('gameasset/backgroundmainmenu.png')
bg_game_screen = pygame.image.load('gameasset/background.png')
title_img = pygame.image.load('gameasset/gametitle.png').convert_alpha()
start_img = pygame.image.load('gameasset/playbutton.png').convert_alpha()
credit_img = pygame.image.load('gameasset/creditbutton.png').convert_alpha()
exit_img = pygame.image.load('gameasset/quitbutton.png').convert_alpha()
pause_img = pygame.image.load('gameasset/pause.png').convert_alpha()
shop_img = pygame.image.load('gameasset/shopui.png').convert_alpha()
moneycounter_img = pygame.image.load('gameasset/moneycounter.png').convert_alpha()
daycounter_img = pygame.image.load('gameasset/daycounter.png').convert_alpha()

# create button instances
title_button = button.Button(300, 100, title_img, 0.5)
start_button = button.Button(515, 350, start_img, 0.5)
credit_button = button.Button(515, 450, credit_img, 0.5)
exit_button = button.Button(515, 550, exit_img, 0.5)
pause_button = button.Button(20, 20, pause_img, 2/3)
shop_button  = button.Button(890, 510, shop_img, 2/3)

# text
daycycle_font = pygame.font.Font('font/Pixeltype.ttf', 60)
daycycle_surf = daycycle_font.render('Day 1', False, 'Black')
daycycle_rect = daycycle_surf.get_rect(topleft=(40, 40))


def main_menu():
    run = True
    while run:
        screen.fill((255, 235, 216))
        screen.blit(bg_main_menu, (0, 0))
        title_button.draw(screen)

        if start_button.draw(screen):
            game_screen()

        if credit_button.draw(screen):
            print('CREDIT')

        if exit_button.draw(screen):
            pygame.quit()  # quit pygame directly
            exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

def game_screen():
    run = True
    while run:
        screen.fill((255, 255, 255))
        screen.blit(bg_game_screen, (0, 0))

        # game screen code here
        screen.blit(daycycle_surf,daycycle_rect)

        if pause_button.draw(screen):
            print('game paused')
            # insert pause code here
        
        if shop_button.draw(screen):
            print('opened shop')
            # insert shop code here
        
        screen.blit(moneycounter_img, (30,530))
        screen.blit(daycounter_img, (380,615))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

# def credits_menu():
   # run = True
   # while run:
        # credits menu code here
     #   pass

# call the main menu
main_menu()

pygame.quit()