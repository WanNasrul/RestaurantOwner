import pygame
import button
from sys import exit #import one thing
from pygame import mixer

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

#load images

# bg_main_menu = pygame.image.load('gameasset/backgroundmainmenu.png')
bg_game_screen = pygame.image.load('gameasset/background.png').convert_alpha()
bg_credit_menu = pygame.image.load('gameasset/credit.png').convert_alpha()
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
shopbackground_img = pygame.image.load('gameasset/upgrade shop remaster/upgradebackground.png').convert_alpha()
xbutton_img = pygame.image.load('gameasset/chef ui/xbutton.png').convert_alpha()
click_sfx = pygame.mixer.Sound('gameasset/click (2).mp3')
xshopbutton_button = button.Button(1100, 30, xbutton_img, 1)
chefuibackground_img = pygame.image.load('gameasset/chef ui/chefuibackground.png').convert_alpha()
# npc position
star_img = pygame.image.load('gameasset/upgrade shop remaster/star.png').convert_alpha()
npc1_x_pos = 1000


upgradebutton_img = pygame.image.load('gameasset/upgrade shop remaster/upgradebuy.png').convert_alpha()
upgrade_button1 = button.Button(610, 155, upgradebutton_img, 1)
upgrade_button2 = button.Button(710,315, upgradebutton_img,1)
upgrade_button3 = button.Button(710,475, upgradebutton_img,1)
upgradebutton4 = button.Button(810,155, upgradebutton_img,1)

# create button instances
title_button = button.Button(300, 100, title_img, 0.5)
start_button = button.Button(515, 350, start_img, 0.5)
credit_button = button.Button(515, 450, credit_img, 0.5)
exit_button = button.Button(515, 550, exit_img, 0.5)
pause_button = button.Button(20, 20, pause_img, 2/3)
shop_button  = button.Button(890, 510, shop_img, 2/3)

# click the chef and cat
fern_button = button.Button(508, 300, fern_img, 0.08)
chef_button = button.Button(200, 215, chef_img, 1)
waiter_button = button.Button(450, 215, waiter_img, 1)

# sound effects
cat_sfx = pygame.mixer.Sound('gameasset/catmeow.mp3')
music_sfx = pygame.mixer.Sound('gameasset/music2.mp3')

# background music
mixer.music.load('gameasset/backgroundmusic.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.50)




# text
# daycycle_font = pygame.font.Font('font/segoepr.ttf', 50)
# daycycle_surf = daycycle_font.render(str(day), True, 'darkred')
# daycycle_rect = daycycle_surf.get_rect(topleft=(495,600))

# money_font = pygame.font.Font('font/segoepr.ttf', 50)
# money_surf = money_font.render(str(money), True, 'darkred')
# money_rect = daycycle_surf.get_rect(topleft=(170,590))

def main_menu():

    # default value for background intial position
    
    run = True
    while run:

        screen.fill((255, 235, 216))
        # screen.blit(bg_main_menu, (0, 0))

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
            game_screen()

        if credit_button.draw(screen):
            click_sfx.play()
            credit_menu()

        if exit_button.draw(screen):
            pygame.quit()  # quit pygame directly
            exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(60)


def load_highest_day():
    try:
        with open('highest_day.txt', 'r') as file:
            highest_day = int(file.read())
    except FileNotFoundError:
        highest_day = 1  # Default value if the file doesn't exist
    return highest_day

def save_highest_day(highest_day):
    with open('highest_day.txt', 'w') as file:
        file.write(str(highest_day))




def game_screen():
    global npc1_x_pos, npc1_img
    run = True

    # default money and day value
    money = 1000
    day = 1

     # Load highest day
    highest_day = load_highest_day()

    while run:
        # game screen code here
        screen.fill((255, 255, 255))
        screen.blit(bg_game_screen, (0, 0))

        if fern_button.draw(screen):
            cat_sfx.play()
            pygame.mixer.music.stop()

        if chef_button.draw(screen):
            print('Meals Pop Up')

        waiter_button.draw(screen)

        npc1_x_pos -= 1.5
        if npc1_x_pos < 550: 
            npc1_img = 1000
        else: # NEED TO RECHECK THIS !!! 
            screen.blit(npc1_img,(npc1_x_pos, 70))

        # game font variables such as day count and money count
        daycycle_font = pygame.font.Font('font/segoepr.ttf', 50)
        daycycle_surf = daycycle_font.render(str(day), True, 'darkred')
        daycycle_rect = daycycle_surf.get_rect(topleft=(495,600))

        money_font = pygame.font.Font('font/segoepr.ttf', 40)
        money_surf = money_font.render(str(money), True, 'darkred')
        money_rect = money_surf.get_rect(topleft=(165,598))

        highest_day_font = pygame.font.Font('font/segoepr.ttf', 30)
        highest_day_text = highest_day_font.render("Highest Day: " + str(highest_day), True, 'darkred')
        highest_day_rect = highest_day_text.get_rect(topleft=(30, 30))

        if pause_button.draw(screen):
            game_pause()
            # insert pause code here
            
        
        if shop_button.draw(screen):
            print('opened shop')
            # insert shop code here
        
        screen.blit(moneycounter_img, (30,530))
        screen.blit(daycounter_img, (380,615))
        screen.blit(daycycle_surf,daycycle_rect)
        screen.blit(money_surf,money_rect)
    
        # testing, add 12 money every 1 frame
        # money += 12

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        pygame.display.update()
        clock.tick(60)


   


def game_pause ():

    global runpauseUI

    runpauseUI = True

    music_playing = True
    

    

    # chef2 = star_img 
    # waiter2 = star_img

    while runpauseUI:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    runpauseUI = False
                if event.key == pygame.K_ESCAPE:
                    runpauseUI = False

        # Draw the shop background
        
        screen.blit(shopbackground_img, (410, 25))

        if upgrade_button1.draw(screen):
            click_sfx.play()
            if music_playing:
                mixer.music.stop()  # Stop background music if playing
            else:
                mixer.music.play(-1)  # Play background music if stopped
            music_playing = not music_playing  # Toggle music state

        if upgrade_button2.draw(screen):
            click_sfx.play()
            game_screen()

        if upgrade_button3.draw(screen):
            click_sfx.play()
            main_menu()

        if upgradebutton4.draw(screen):
            click_sfx.play
            click_sfx.stop()

        

        pygame.display.update()
        


def credit_menu():
    run = True
    while run :

        screen.fill((255, 255, 255))
        screen.blit(bg_credit_menu, (0, 0))

        if pause_button.draw(screen):
            print('game paused')
            # insert pause code here
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             run = False
        pygame.display.update()



# call the main menu
main_menu()

pygame.quit()