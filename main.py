import pygame
import button
from sys import exit #import one thing
from SaveLoadManager import SaveLoadSystem

# initialize pygame
pygame.init()

saveloadmanager = SaveLoadSystem(".save", "save_data")
# create display window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Restaurant Owner!')
clock = pygame.time.Clock()


# moving main menu background
mainmenubg_surf = pygame.image.load('gameasset/backgroundmainmenuanimated.png').convert_alpha()
mainmenubg_rect = mainmenubg_surf.get_rect(topleft = (0,10))
mainmenubg2_surf = pygame.image.load('gameasset/backgroundmainmenuanimateddark.png').convert_alpha()
mainmenubg2_rect = mainmenubg2_surf.get_rect(topleft = (50,-50))

#load images

# bg_main_menu = pygame.image.load('gameasset/backgroundmainmenu.png')
bg_game_screen = pygame.image.load('gameasset/background.png').convert_alpha()
title_img = pygame.image.load('gameasset/gametitle.png').convert_alpha()
start_img = pygame.image.load('gameasset/playbutton.png').convert_alpha()
credit_img = pygame.image.load('gameasset/creditbutton.png').convert_alpha()
exit_img = pygame.image.load('gameasset/quitbutton.png').convert_alpha()
pause_img = pygame.image.load('gameasset/pause.png').convert_alpha()
shop_img = pygame.image.load('gameasset/shopui.png').convert_alpha()
moneycounter_img = pygame.image.load('gameasset/moneycounter.png').convert_alpha()
daycounter_img = pygame.image.load('gameasset/daycounter.png').convert_alpha()
fern_img = pygame.image.load('gameasset/fern.png').convert_alpha()
chef_img = pygame.image.load('gameasset/chef.png').convert_alpha()
waiter_img = pygame.image.load('gameasset/waiter.png').convert_alpha()
npc1_img = pygame.image.load('gameasset/npc1.png').convert_alpha()
tablechair1_img = pygame.image.load('gameasset/tablechair.png').convert_alpha()


# create button instances
title_button = button.Button(300, 100, title_img, 0.5)
start_button = button.Button(515, 350, start_img, 0.5)
credit_button = button.Button(515, 450, credit_img, 0.5)
exit_button = button.Button(515, 550, exit_img, 0.5)
pause_button = button.Button(20, 20, pause_img, 2/3)
shop_button  = button.Button(890, 510, shop_img, 2/3)
tablechair1_button = button.Button(600, 380, tablechair1_img, 0.6)

# click the chef and cat
fern_button = button.Button(502, 300, fern_img, 0.08)
chef_button = button.Button(200, 215, chef_img, 1)


# sound effects
cat_sfx = pygame.mixer.Sound('gameasset/catmeow.mp3')
music_sfx = pygame.mixer.Sound('gameasset/music2.mp3')



# text
# daycycle_font = pygame.font.Font('font/segoepr.ttf', 50)
# daycycle_surf = daycycle_font.render(str(day), True, 'darkred')
# daycycle_rect = daycycle_surf.get_rect(topleft=(495,600))

# money_font = pygame.font.Font('font/segoepr.ttf', 50)
# money_surf = money_font.render(str(money), True, 'darkred')
# money_rect = daycycle_surf.get_rect(topleft=(170,590))

def collision_detection(rect1, rect2):
    # check if two rectangles collide
    return rect1.colliderect(rect2)

def npc(x, y):
    screen.blit(npc1_img, (x, y))


def waiter(x, y):
    screen.blit(waiter_img, (x, y))


def main_menu():

    # default value for background intial position
    
    run = True
    while run:

        screen.fill((255, 235, 216))

        mainmenubg_rect.x -= 2
        if mainmenubg_rect.left <= -743: 
            mainmenubg_rect.left = 0
        
        mainmenubg2_rect.x -= 1
        if mainmenubg2_rect.left <= -743: 
            mainmenubg2_rect.left = 0

        screen.blit(mainmenubg2_surf, mainmenubg2_rect)
        screen.blit(mainmenubg_surf, mainmenubg_rect)

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
        clock.tick(60)

def game_screen():
    global npc1_x_pos, npc1_img
    run = True

    # default money and day value
    money = 0   
    day = 1

    waiterX = 450
    waiterY =  215
   
    # npc position
    npc1_x_pos = 1000

    # rect object for waiter
    waiter_rect = pygame.Rect(waiterX, waiterY, waiter_img.get_width(), waiter_img.get_height())
    # rect object for table and chair
    tablechair1_rect = pygame.Rect(615, 380, 195, 20)

    while run:
        # game screen code here
        screen.fill((255, 255, 255))
        screen.blit(bg_game_screen, (0, 0))


        tablechair1_button.draw(screen)

        if fern_button.draw(screen):
            cat_sfx.play()

        if chef_button.draw(screen):
            print('Text bubble')

        # get the state of all keyboard keys
        keys = pygame.key.get_pressed()

        # update waiter position based on key presses
        if keys[pygame.K_w]:
            if waiterY > 0:
                waiterY -= 3
        if keys[pygame.K_s]:
            if waiterY < 520:
                waiterY += 3
        if keys[pygame.K_a]:
            if waiterX > 381:
                waiterX -= 3
        if keys[pygame.K_d]:
            if waiterX < 1045:
                waiterX += 3

        
        # Update waiter Rect object position
        waiter_rect.topleft = (waiterX, waiterY)

        # if collision_detection(waiter_rect, tablechair1_rect):
            # print("Collision Detected!")
            # print("Waiter Rect:", waiter_rect)
            # print("Table Chair Rect:", tablechair1_rect)


            # heck for collision between waiter and table chair
        if collision_detection(waiter_rect, tablechair1_rect):
            # if collision is detected, prevent waiter from moving in that direction
            if keys[pygame.K_w] and waiter_rect.top < tablechair1_rect.bottom:
                waiterY += 3
            if keys[pygame.K_s] and waiter_rect.bottom > tablechair1_rect.top:
                waiterY -= 3
            if keys[pygame.K_a] and waiter_rect.left < tablechair1_rect.right:
                waiterX += 3
            if keys[pygame.K_d] and waiter_rect.right > tablechair1_rect.left:
                waiterX -= 3



        npc1_x_pos -= 1.5
        if npc1_x_pos < 550: 
            npc1_img = 1100
        else: # NEED TO RECHECK THIS !!! 
            screen.blit(npc1_img,(npc1_x_pos, 70))

        # game font variables such as day count and money count
        daycycle_font = pygame.font.Font('font/segoepr.ttf', 50)
        daycycle_surf = daycycle_font.render(str(day), True, 'darkred')
        daycycle_rect = daycycle_surf.get_rect(topleft=(495,600))

        money_font = pygame.font.Font('font/segoepr.ttf', 40)
        money_surf = money_font.render(str(money), True, 'darkred')
        money_rect = money_surf.get_rect(topleft=(165,598))

        if pause_button.draw(screen):
            print('game paused')
            # insert pause code here

            run = False
        
        waiter(waiterX, waiterY)

        if shop_button.draw(screen):
            print('opened shop')
            # insert shop code here

        
        screen.blit(moneycounter_img, (30,530))
        screen.blit(daycounter_img, (380,615))
        screen.blit(daycycle_surf,daycycle_rect)
        screen.blit(money_surf,money_rect)
    
        # testing, add 12 money every 1 frame
        money += 12


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                saveloadmanager.save_data() # <--- STOP HERE 7/5/24 
                pygame.quit()
                exit()

        pygame.display.update() 
        clock.tick(60)

# def credits_menu():
   # run = True
   # while run:
        # credits menu code here
     #   pass

# call the main menu
main_menu()

pygame.quit()