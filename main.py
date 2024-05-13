import pygame
import button
from sys import exit #import one thing
import random

# initialize pygame
pygame.init()

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


# main menu images
# main menu images
bg_game_screen = pygame.image.load('gameasset/background.png').convert_alpha()
bg_credit_menu = pygame.image.load('gameasset/credit.png').convert_alpha()
title_img = pygame.image.load('gameasset/gametitle.png').convert_alpha()
shoppic_img = pygame.image.load('gameasset/shop.jpg').convert_alpha()
start_img = pygame.image.load('gameasset/playbutton.png').convert_alpha()
credit_img = pygame.image.load('gameasset/creditbutton.png').convert_alpha()
exit_img = pygame.image.load('gameasset/quitbutton.png').convert_alpha()

# game images

# game images
pause_img = pygame.image.load('gameasset/pause.png').convert_alpha()
shop_img = pygame.image.load('gameasset/shopui.png').convert_alpha()
moneycounter_img = pygame.image.load('gameasset/moneycounter.png').convert_alpha()
daycounter_img = pygame.image.load('gameasset/daycounter.png').convert_alpha()
fern_img = pygame.image.load('gameasset/fern.png').convert_alpha()
chef_img = pygame.image.load('gameasset/chef.png').convert_alpha()
waiter_img = pygame.image.load('gameasset/waiter.png').convert_alpha()
npc1_img = pygame.image.load('gameasset/casher.png').convert_alpha()
tablechair1_img = pygame.image.load('gameasset/tablechair.png').convert_alpha()
tablechair2_img = pygame.image.load('gameasset/tablechair.png').convert_alpha()
tablechair3_img = pygame.image.load('gameasset/tablechair.png').convert_alpha()

# Rchair1_img = pygame.image.load('gameasset/Rchair.png').convert_alpha()
# Lchair1_img = pygame.image.load('gameasset/Lchair.png').convert_alpha()
# table_img = pygame.image.load('gameasset/table.png').convert_alpha()

# chef ui images
chefuibackground_img = pygame.image.load('gameasset/chef ui/chefuibackground.png').convert_alpha()
xbutton_img = pygame.image.load('gameasset/chef ui/xbutton.png').convert_alpha()
chicken_img = pygame.image.load('gameasset/chef ui/chicken.png').convert_alpha()
fish_img = pygame.image.load('gameasset/chef ui/fish.png').convert_alpha()
burger_img = pygame.image.load('gameasset/chef ui/burger.png').convert_alpha()
pizza_img = pygame.image.load('gameasset/chef ui/pizza.png').convert_alpha()
steak_img = pygame.image.load('gameasset/chef ui/steak.png').convert_alpha()
progressbar_img = pygame.image.load('gameasset/chef ui/progressbar.png').convert_alpha()
emptybox_img = pygame.image.load('gameasset/chef ui/emptybox.png').convert_alpha()
# chef ui buttons
xbutton_button = button.Button(1100, 70, xbutton_img, 1)
chicken_button = button.Button(440, 250, chicken_img, 1)
fish_button = button.Button(590, 250, fish_img, 1)
burger_button = button.Button(740, 250, burger_img, 1)
pizza_button = button.Button(890, 250, pizza_img, 1)
steak_button = button.Button(1040, 250, steak_img, 1)

# npc position
npc1_x_pos = 1000
npc1_y_pos = 100
# chef ui images
chefuibackground_img = pygame.image.load('gameasset/chef ui/chefuibackground.png').convert_alpha()
xbutton_img = pygame.image.load('gameasset/chef ui/xbutton.png').convert_alpha()
chicken_img = pygame.image.load('gameasset/chef ui/chicken.png').convert_alpha()
fish_img = pygame.image.load('gameasset/chef ui/fish.png').convert_alpha()
burger_img = pygame.image.load('gameasset/chef ui/burger.png').convert_alpha()
pizza_img = pygame.image.load('gameasset/chef ui/pizza.png').convert_alpha()
steak_img = pygame.image.load('gameasset/chef ui/steak.png').convert_alpha()
progressbar_img = pygame.image.load('gameasset/chef ui/progressbar.png').convert_alpha()
emptybox_img = pygame.image.load('gameasset/chef ui/emptybox.png').convert_alpha()
# chef ui buttons
xbutton_button = button.Button(1100, 70, xbutton_img, 1)
chicken_button = button.Button(440, 250, chicken_img, 1)
fish_button = button.Button(590, 250, fish_img, 1)
burger_button = button.Button(740, 250, burger_img, 1)
pizza_button = button.Button(890, 250, pizza_img, 1)
steak_button = button.Button(1040, 250, steak_img, 1)

# npc position
npc1_x_pos = 1000


# create button instances
title_button = button.Button(300, 100, title_img, 0.5)
start_button = button.Button(515, 350, start_img, 0.5)
credit_button = button.Button(515, 450, credit_img, 0.5)
exit_button = button.Button(515, 550, exit_img, 0.5)
pause_button = button.Button(20, 20, pause_img, 2/3)
shop_button  = button.Button(890, 510, shop_img, 2/3)
#tablechair1_button = button.Button(900, 830, tablechair1_img, 0.6)
#tablechair2_button = button.Button(900, 680, tablechair2_img, 0.6)
#tablechair3_button = button.Button(600, 680, tablechair3_img, 0.6)
#tablechair4_button = button.Button(600, 880, tablechair4_img, 0.6)

# click the chef and cat
fern_button = button.Button(508, 300, fern_img, 0.08)
chef_button = button.Button(200, 215, chef_img, 1)
# waiter_button = button.Button(450, 215, waiter_img, 1)

# sound effects
cat_sfx = pygame.mixer.Sound('gameasset/catmeow.mp3')
music_sfx = pygame.mixer.Sound('gameasset/music2.mp3')
click_sfx = pygame.mixer.Sound('gameasset/click (2).mp3')
click_sfx = pygame.mixer.Sound('gameasset/click (2).mp3')



# text
# daycycle_font = pygame.font.Font('font/segoepr.ttf', 50)
# daycycle_surf = daycycle_font.render(str(day), True, 'darkred')
# daycycle_rect = daycycle_surf.get_rect(topleft=(495,600))

# money_font = pygame.font.Font('font/segoepr.ttf', 50)
# money_surf = money_font.render(str(money), True, 'darkred')
# money_rect = daycycle_surf.get_rect(topleft=(170,590))

def npc(x, y):
    npc1_width = int(npc1_img.get_width() * 1)
    npc1_height = int(npc1_img.get_height() * 1)
    npc1_resize= pygame.transform.scale(npc1_img, (npc1_width, npc1_height))
    screen.blit(npc1_resize, (x, y))

def waiter(x, y):
    waiter_width = int(waiter_img.get_width() * 1)
    waiter_height = int(waiter_img.get_height() * 1)
    waiter_resize = pygame.transform.scale(waiter_img, (waiter_width, waiter_height))
    waiter_flip = pygame.transform.flip(waiter_resize, True, False)
    screen.blit(waiter_flip, (x, y))

def table1(x, y):
    tablechair1_width = int(tablechair1_img.get_width() * 1)
    tablechair1_height = int(tablechair1_img.get_height() * 1)
    tablechair1_resize = pygame.transform.scale(tablechair1_img, (tablechair1_width, tablechair1_height))
    screen.blit(tablechair1_resize, (x, y))

def table2(x, y):
    tablechair2_width = int(tablechair2_img.get_width() * 1)
    tablechair2_height = int(tablechair2_img.get_height() * 1)
    tablechair2_resize = pygame.transform.scale(tablechair2_img, (tablechair2_width, tablechair2_height))
    screen.blit(tablechair2_resize, (x, y))

def table3(x, y):
    tablechair3_width = int(tablechair3_img.get_width() * 1)
    tablechair3_height = int(tablechair3_img.get_height() * 1)
    tablechair3_resize = pygame.transform.scale(tablechair3_img, (tablechair3_width, tablechair3_height))
    screen.blit(tablechair3_resize, (x, y))

def foodserve(x, y):
    foodserve_width = int(chicken_img.get_width() *0.5)
    foodserve_height = int(chicken_img.get_height() * 0.5)
    foodserve_resize = pygame.transform.scale(chicken_img, (foodserve_width, foodserve_height))
    screen.blit(foodserve_resize, (x, y))

def collision_detection(waiter_rect, table_rect):

    # print("waiter_rect:", waiter_rect)
    # print("table_rect:", table_rect)
    # print("Collision:", waiter_rect.colliderect(table_rect))


    # Check if two rectangles collide while taking into account the waiter's position
    return waiter_rect.colliderect(table_rect)





def main_menu():

    # default value for background intial position
    
    run = True
    while run:

        screen.fill((255, 235, 216))
        # screen.blit(bg_main_menu, (0, 0)
        # moving main menu background
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
            click_sfx.play()
            click_sfx.play()
            game_screen()



        if credit_button.draw(screen):
            click_sfx.play()
            credit_menu()
            click_sfx.play()
            credit_menu()

        if exit_button.draw(screen):
            click_sfx.play() 
            pygame.quit() 
             # quit pygame directly
            click_sfx.play() 
            pygame.quit() 
             # quit pygame directly
            exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(60)

def game_screen():

    global npc1_x_pos, npc1_img, npc1_y_pos
    run = True

    # default money and day value
    money = 0   
    day = 1

    tablechair1X = 740
    tablechair1Y = 405

    tablechair2X = 750
    tablechair2Y = 250

    tablechair3X = 400
    tablechair3Y = 480

    waiterX = 570
    waiterY =  150

    foodserveX = 490
    foodserveY = 240

    runchefUI = False
    cooking = emptybox_img
    progress = 0

    waiterfood = emptybox_img

    # rect object for waiter
    waiter_rect = pygame.Rect(waiterX, waiterY, waiter_img.get_width(), waiter_img.get_height())
    # rect object for table and chair
    tablechair1_rect = pygame.Rect(430, 480, 220, 15)
    tablechair2_rect = pygame.Rect(760, 410, 220, 10)
    tablechair3_rect = pygame.Rect(765, 255, 220, 10)

    # food rect and surf
    emptybox_surf = pygame.image.load('gameasset/chef ui/emptybox.png').convert_alpha()
    emptybox_rect = emptybox_surf.get_rect(topleft = (550, 210))


    while run:
        # game screen code here
        screen.fill((255, 255, 255))
        screen.blit(bg_game_screen, (0, 0))


        if fern_button.draw(screen) and runchefUI == False:
            cat_sfx.play()

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

        # update waiter Rect object position
        waiter_rect.topleft = (waiterX, waiterY)

        # check for collision between waiter and table chair (1)
        if collision_detection(waiter_rect, tablechair1_rect):
        # If collision is detected, prevent waiter from moving in that direction
            if keys[pygame.K_w] and waiter_rect.top < tablechair1_rect.bottom:
                waiterY += 3
            if keys[pygame.K_s] and waiter_rect.bottom > tablechair1_rect.top:
                waiterY -= 3
            if keys[pygame.K_a] and waiter_rect.left < tablechair1_rect.right:
                waiterX += 3
            if keys[pygame.K_d] and waiter_rect.right > tablechair1_rect.left:
                waiterX -= 3

            waiterfood = emptybox_img
            cooking = emptybox_img

        # check for collision between waiter and table chair (2)
        if collision_detection(waiter_rect, tablechair2_rect):
        # If collision is detected, prevent waiter from moving in that direction
            if keys[pygame.K_w] and waiter_rect.top < tablechair2_rect.bottom:
                waiterY += 3
            if keys[pygame.K_s] and waiter_rect.bottom > tablechair2_rect.top:
                waiterY -= 3
            if keys[pygame.K_a] and waiter_rect.left < tablechair2_rect.right:
                waiterX += 3
            if keys[pygame.K_d] and waiter_rect.right > tablechair2_rect.left:
                waiterX -= 3

        # check for collision between waiter and table chair (3)
        if collision_detection(waiter_rect, tablechair3_rect):
        # If collision is detected, prevent waiter from moving in that direction
            if keys[pygame.K_w] and waiter_rect.top < tablechair3_rect.bottom:
                waiterY += 3
            if keys[pygame.K_s] and waiter_rect.bottom > tablechair3_rect.top:
                waiterY -= 3
            if keys[pygame.K_a] and waiter_rect.left < tablechair3_rect.right:
                waiterX += 3
            if keys[pygame.K_d] and waiter_rect.right > tablechair3_rect.left:
                waiterX -= 3



        npc1_x_pos -= 1.5
        if npc1_x_pos <= 650: 
            npc1_x_pos = 651
            npc1_y_pos += 1.5

            if npc1_y_pos >= 250:
                npc1_y_pos = 250  

                if npc1_y_pos == 250:
                    npc1_y_pos = 425
                    npc1_x_pos = 400
                    npc

        # game font variables such as day count and money count
        daycycle_font = pygame.font.Font('font/segoepr.ttf', 50)
        daycycle_surf = daycycle_font.render(str(day), True, 'darkred')
        daycycle_rect = daycycle_surf.get_rect(topleft=(495,600))

        money_font = pygame.font.Font('font/segoepr.ttf', 40)
        money_surf = money_font.render(str(money), True, 'darkred')
        money_rect = money_surf.get_rect(topleft=(165,598))

        if pause_button.draw(screen):
            click_sfx.play()
            click_sfx.play()
            print('game paused')
            # insert pause code here
            run = False


        if shop_button.draw(screen):
            click_sfx.play()
            shop_open()


        # insert shop code here

        
        screen.blit(moneycounter_img, (30,530))
        screen.blit(daycounter_img, (380,615))
        screen.blit(daycycle_surf,daycycle_rect)
        screen.blit(money_surf,money_rect)
    
        # testing, add 12 money every 1 frame
        money += 12

        table1(tablechair1X,tablechair1Y)

        table2(tablechair2X,tablechair2Y)

        table3(tablechair3X,tablechair3Y)

        npc(npc1_x_pos, npc1_y_pos)

        screen.blit(emptybox_surf, emptybox_rect)


        #table4(tablechair4X,tablechair4Y)

        # Chef UI ====================================== #
        
        # chef progress bar
        progressbar_font = pygame.font.Font('font/segoepr.ttf', 15)
        progressbar_surf = progressbar_font.render('.'*progress, False, (64,64,64))
        progressbar_rect = progressbar_surf.get_rect(midleft = (615,535))

        if chef_button.draw(screen):
            click_sfx.play()
            runchefUI = True

        waiter(waiterX, waiterY)
        screen.blit(waiterfood, (waiterX - 35,waiterY - 105))
        foodserve(foodserveX,foodserveY)

        if runchefUI == True:
            
            screen.blit(chefuibackground_img, (410,65))
            # close chef UI
            # kinda not efficient code for now, I'll optimize it later
            if xbutton_button.draw(screen):
                click_sfx.play()
                runchefUI = False
            
            if chicken_button.draw(screen) and cooking == emptybox_img:
                click_sfx.play()
                cooking = chicken_img
                # if the player clicks on the food icon, it will be added to the cooking slot

            if fish_button.draw(screen) and cooking == emptybox_img:
                click_sfx.play()
                cooking = fish_img

            if burger_button.draw(screen) and cooking == emptybox_img:
                click_sfx.play()
                cooking = burger_img

            if pizza_button.draw(screen) and cooking == emptybox_img:
                click_sfx.play()
                cooking = pizza_img
                
            if steak_button.draw(screen) and cooking == emptybox_img:
                click_sfx.play()
                cooking = steak_img
            
            if cooking != emptybox_img:
                if progress <= 130:
                    progress += 1
                # else:
                #     cooking = emptybox_img
                #     progress = 0
 
            screen.blit(cooking, (450,480))
            screen.blit(progressbar_img, (605,515))
            screen.blit(progressbar_surf, progressbar_rect)
            pygame.draw.rect(screen,'red',progressbar_rect)

            
        # CHECK MOUSE POSITION
        # mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)

        # Chef UI ====================================== #

        # food serve ================================ #

        if emptybox_rect.colliderect(waiter_rect):
            print("waiter pick food")
            waiterfood = cooking

        # food serve ================================ #





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # saveloadmanager.save_data() # <--- STOP HERE 7/5/24 
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)

def credit_menu():
    run = True
    while run :

        screen.fill((255, 255, 255))
        screen.blit(bg_credit_menu, (0, 0))

        if pause_button.draw(screen):
            click_sfx.play()
            print('game paused')
            # insert pause code here
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             run = False
        pygame.display.update()

def shop_open():
    run = True
    while run :

        screen.fill((255, 255, 255))
        screen.blit(bg_game_screen, (0,0))
        screen.blit(shoppic_img, (150,150))
        

        if pause_button.draw(screen):
            click_sfx.play()
            print('game paused')
            # insert pause code here
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             run = False
        pygame.display.update()






def credit_menu():
    run = True
    while run :

        screen.fill((255, 255, 255))
        screen.blit(bg_credit_menu, (0, 0))

        if pause_button.draw(screen):
            click_sfx.play()
            print('game paused')
            # insert pause code here
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             run = False
        pygame.display.update()

def shop_open():
    run = True
    while run :

        screen.fill((255, 255, 255))
        screen.blit(bg_game_screen, (0,0))
        screen.blit(shoppic_img, (150,150))
        

        if pause_button.draw(screen):
            click_sfx.play()
            print('game paused')
            # insert pause code here
            run = False

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