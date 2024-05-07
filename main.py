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
clock = pygame.time.Clock()


# moving main menu background
mainmenubg_surf = pygame.image.load('gameasset/backgroundmainmenuanimated.png').convert_alpha()
mainmenubg_rect = mainmenubg_surf.get_rect(topleft = (0,10))
mainmenubg2_surf = pygame.image.load('gameasset/backgroundmainmenuanimateddark.png').convert_alpha()
mainmenubg2_rect = mainmenubg2_surf.get_rect(topleft = (50,-50))


# main menu images
bg_game_screen = pygame.image.load('gameasset/background.png').convert_alpha()
title_img = pygame.image.load('gameasset/gametitle.png').convert_alpha()
start_img = pygame.image.load('gameasset/playbutton.png').convert_alpha()
credit_img = pygame.image.load('gameasset/creditbutton.png').convert_alpha()
exit_img = pygame.image.load('gameasset/quitbutton.png').convert_alpha()

# game images
pause_img = pygame.image.load('gameasset/pause.png').convert_alpha()
shop_img = pygame.image.load('gameasset/shopui.png').convert_alpha()
moneycounter_img = pygame.image.load('gameasset/moneycounter.png').convert_alpha()
daycounter_img = pygame.image.load('gameasset/daycounter.png').convert_alpha()
fern_img = pygame.image.load('gameasset/fern.png').convert_alpha()
chef_img = pygame.image.load('gameasset/chef.png').convert_alpha()
waiter_img = pygame.image.load('gameasset/waiter.png').convert_alpha()
npc1_img = pygame.image.load('gameasset/npc1.png').convert_alpha()
tablechair1_img = pygame.image.load('gameasset/tablechair.png').convert_alpha()
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
npc_rect = npc1_x_pos.get_rect()



# create button instances
title_button = button.Button(300, 100, title_img, 0.5)
start_button = button.Button(515, 350, start_img, 0.5)
credit_button = button.Button(515, 450, credit_img, 0.5)
exit_button = button.Button(515, 550, exit_img, 0.5)
pause_button = button.Button(20, 20, pause_img, 2/3)
shop_button  = button.Button(890, 510, shop_img, 2/3)
tablechair1_button = button.Button(600, 380, tablechair1_img, 0.6)

# click the chef and cat
fern_button = button.Button(508, 300, fern_img, 0.08)
chef_button = button.Button(200, 215, chef_img, 1)
# waiter_button = button.Button(450, 215, waiter_img, 1)

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
def npc(x, y):
    screen.blit(npc1_img, (x, y))


def waiter(x, y):
    screen.blit(waiter_img, (x, y))

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
    global npc_rect, npc1_img
    run = True

    # default money and day value
    money = 0   
    day = 1

    waiterX = 450
    waiterY =  215

    runchefUI = False
    cooking = emptybox_img
    progress = 0

    while run:
        # game screen code here
        screen.fill((255, 255, 255))
        screen.blit(bg_game_screen, (0, 0))
        

        tablechair1_button.draw(screen)

        if fern_button.draw(screen):
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

        #npc1_x_pos -= 1.5
        #if npc1_x_pos <= 550: 
        #    npc1_img = 1100
        #if npc1_x_pos
        #else: # NEED TO RECHECK THIS !!! 
        #    screen.blit(npc1_img,(npc1_x_pos, 70))
        speed = 0.5
            
        if npc_rect.x <= 600:
            npc_rect.x += 1 * speed

        if npc_rect.x == 601 and npc_rect.y <= 400:
            npc_rect.y += 1 * speed
                
        if npc_rect.y == 401 and npc_rect.x == 601:
            npc_rect.x = 800
            npc_rect.y = 600

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
        
        if shop_button.draw(screen):
            print('opened shop')
            # insert shop code here
        
        screen.blit(moneycounter_img, (30,530))
        screen.blit(daycounter_img, (380,615))
        screen.blit(daycycle_surf,daycycle_rect)
        screen.blit(money_surf,money_rect)
    
        # testing, add 12 money every 1 frame
        money += 12

        waiter(waiterX, waiterY)

        # Chef UI ====================================== #
        
        # chef progress bar
        progressbar_font = pygame.font.Font('font/segoepr.ttf', 15)
        progressbar_surf = progressbar_font.render('.'*progress, False, (64,64,64))
        progressbar_rect = progressbar_surf.get_rect(midleft = (615,535))

        if chef_button.draw(screen):
            runchefUI = True

        if runchefUI == True:
            
            screen.blit(chefuibackground_img, (410,65))
            # close chef UI
            # kinda not efficient code for now, I'll optimize it later
            if xbutton_button.draw(screen):
                runchefUI = False
            
            if chicken_button.draw(screen) and cooking == emptybox_img:
                cooking = chicken_img
                # if the player clicks on the food icon, it will be added to the cooking slot

            if fish_button.draw(screen) and cooking == emptybox_img:
                cooking = fish_img

            if burger_button.draw(screen) and cooking == emptybox_img:
                cooking = burger_img

            if pizza_button.draw(screen) and cooking == emptybox_img:
                cooking = pizza_img
                
            if steak_button.draw(screen) and cooking == emptybox_img:
                cooking = steak_img
            
            if cooking != emptybox_img:
                if progress <= 130:
                    progress += 1
                else:
                    cooking = emptybox_img
                    progress = 0
 
            screen.blit(cooking, (450,480))
            screen.blit(progressbar_img, (605,515))
            screen.blit(progressbar_surf, progressbar_rect)
            pygame.draw.rect(screen,'red',progressbar_rect)


        # mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)

        # Chef UI ====================================== #


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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