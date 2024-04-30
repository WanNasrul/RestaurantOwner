import pygame
import button

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

# create button instances
title_button = button.Button(300, 100, title_img, 0.5)
start_button = button.Button(515, 350, start_img, 0.5)
credit_button = button.Button(515, 450, credit_img, 0.5)
exit_button = button.Button(515, 550, exit_img, 0.5)

# characters
# cheftest = pygame.image.load('gameasset/testchef.png').convert_alpha()
fern_img = pygame.image.load('gameasset/fern.png').convert_alpha()
# waitertest = pygame.image.load('gameasset/testwaiter.png').convert_alpha()


# cheftest_button = button.Button(175, 65, cheftest, 0.09)
fern_button = button.Button(508, 300, fern_img, 0.11)
# waitertest_button = button.Button(460, 65, waitertest, 0.03)


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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

def game_screen():
    run = True
    while run:
        screen.fill((255, 255, 255))
        screen.blit(bg_game_screen, (0, 0))

        # game screen code here
        # if cheftest_button.draw(screen):
        #     chef_menu()

        # waitertest_button.draw(screen)

        fern_button.draw(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

def chef_menu():

    chef_menu_screen = pygame.Surface((350, 350))
    run = True
    while run:
        screen.blit(bg_game_screen, (0,0))
        chef_menu_screen.fill((255, 0, 0))

        screen.blit(chef_menu_screen, (100, 100))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

# def credits_menu():
   # run = True
   # while run:
        # credits menu code here
     #   pass

# call the main menu
main_menu()

pygame.quit()