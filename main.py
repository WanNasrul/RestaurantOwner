import pygame
import button
from sys import exit #import one thing
import random
import time
import math
from pygame import mixer
import pickle
# import os 

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
bg_credit_menu = pygame.image.load('gameasset/credit.png').convert_alpha()
title_img = pygame.image.load('gameasset/gametitle.png').convert_alpha()
shoppic_img = pygame.image.load('gameasset/shopui2/shopuibackground.png').convert_alpha()
start_img = pygame.image.load('gameasset/playbutton.png').convert_alpha()
credit_img = pygame.image.load('gameasset/creditbutton.png').convert_alpha()
exit_img = pygame.image.load('gameasset/quitbutton.png').convert_alpha()


# intro dialog

waiterdialogue_img = pygame.image.load('gameasset/dialogue ui/waiterdialogue.png').convert_alpha()
chefdialogue_img = pygame.image.load('gameasset/dialogue ui/chefdialogue.png').convert_alpha()
cashierdialogue_img = pygame.image.load('gameasset/dialogue ui/cashierdialogue.png').convert_alpha()
dialogue_img = pygame.image.load('gameasset/dialogue ui/dialogue.png').convert_alpha()
nextdialogue_img = pygame.image.load('gameasset/dialogue ui/nextdialogue.png').convert_alpha()
skipdialogue_img = pygame.image.load('gameasset/dialogue ui/skipdialogue.png').convert_alpha()

nextdialogue_button = button.Button(1070, 620, nextdialogue_img, 1)
skipdialogue_button = button.Button(100, 620, skipdialogue_img, 1)

nextday_img = pygame.image.load('gameasset/nextdaybutton.png').convert_alpha()
nextday_button = button.Button(963,50, nextday_img, 1)


# game images
pause_img = pygame.image.load('gameasset/pause.png').convert_alpha()
shop_img = pygame.image.load('gameasset/shopui.png').convert_alpha()
moneycounter_img = pygame.image.load('gameasset/moneycounter.png').convert_alpha()
daycounter_img = pygame.image.load('gameasset/daycounter.png').convert_alpha()
fern_img = pygame.image.load('gameasset/fern.png').convert_alpha()

chefstanding_img = pygame.image.load('gameasset/chef.png').convert_alpha()
chefcooking1_img = pygame.image.load('gameasset/chef2.png').convert_alpha()
chefcooking2_img = pygame.image.load('gameasset/chef3.png').convert_alpha()
chef_cooking = [chefcooking1_img,chefcooking2_img]
chef_index = 0
chef_img = chef_cooking[chef_index]

# game icon
pygame.display.set_icon(chefcooking1_img)

waiter_img = pygame.image.load('gameasset/waiter.png').convert_alpha()
npc1_img = pygame.image.load('gameasset/cashier.png').convert_alpha()
npc2_img = pygame.image.load('gameasset/cashier.png').convert_alpha()
npc3_img = pygame.image.load('gameasset/cashier.png').convert_alpha()
tablechair1_img = pygame.image.load('gameasset/tablechair.png').convert_alpha()
tablechair2_img = pygame.image.load('gameasset/tablechair.png').convert_alpha()
tablechair3_img = pygame.image.load('gameasset/tablechair.png').convert_alpha()
vignette_img = pygame.image.load('gameasset/vignette.png').convert_alpha()
casher_img = pygame.image.load('gameasset/cashercollision.png').convert_alpha()
cashiernpc_img = pygame.image.load('gameasset/cashier.png').convert_alpha()
cashiernpc_flip = pygame.transform.flip(cashiernpc_img, True, False)

#waiter
waiterstand_img = pygame.image.load('gameasset/waiter.png').convert_alpha()
waiterwalk1_img = pygame.image.load('gameasset/waiterwalk1.png').convert_alpha()
waiterwalk2_img = pygame.image.load('gameasset/waiterwalk2.png').convert_alpha()
waiter_walk = [waiterwalk1_img,waiterwalk2_img]
waiter_index = 0
waiter_img = waiter_walk[waiter_index]

#npcanimation
npcalien1_img = pygame.image.load('gameasset/npcanimationpack/npcalien1.png').convert_alpha()
npcalien2_img = pygame.image.load('gameasset/npcanimationpack/npcalien2.png').convert_alpha()
npcalien3_img = pygame.image.load('gameasset/npcanimationpack/npcalien3.png').convert_alpha()
npcalien4_img = pygame.image.load('gameasset/npcanimationpack/npcalien4.png').convert_alpha()
npcalien_walk = [npcalien2_img,npcalien3_img]
npcalien_index = 0
npcalien_img = npcalien_walk[npcalien_index]

npccat1_img = pygame.image.load('gameasset/npcanimationpack/npccat1.png').convert_alpha()
npccat2_img = pygame.image.load('gameasset/npcanimationpack/npccat2.png').convert_alpha()
npccat3_img = pygame.image.load('gameasset/npcanimationpack/npccat3.png').convert_alpha()
npccat_walk = [npccat2_img,npccat3_img]
npccat_index = 0
npccat_img = npccat_walk[npccat_index]

npcblob1_img = pygame.image.load('gameasset/npcanimationpack/npcblob1.png').convert_alpha()
npcblob2_img = pygame.image.load('gameasset/npcanimationpack/npcblob2.png').convert_alpha()
npcblob3_img = pygame.image.load('gameasset/npcanimationpack/npcblob3.png').convert_alpha()
npcblob_walk = [npcblob2_img,npcblob3_img]
npcblob_index = 0
npcblob_img = npcblob_walk[npcblob_index]

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
emptybox_img.set_alpha(0)

# chef ui buttons
xbutton_button = button.Button(1100, 70, xbutton_img, 1)
chicken_button = button.Button(440, 250, chicken_img, 1)
fish_button = button.Button(590, 250, fish_img, 1)
burger_button = button.Button(740, 250, burger_img, 1)
pizza_button = button.Button(890, 250, pizza_img, 1)
steak_button = button.Button(1040, 250, steak_img, 1)

#shopui2
shopui2background_img = pygame.image.load('gameasset/shopui2/shopuibackground.png').convert_alpha()
shopdecoration_img = pygame.image.load('gameasset/shopui2/shopdecoration.png').convert_alpha()
shopupgrade_img = pygame.image.load('gameasset/shopui2/shopupgrade.png').convert_alpha()

#shopui2 buttons
shopdecoration_button = button.Button(430, 270, shopdecoration_img, 1)
shopupgrade_button = button.Button(680, 270, shopupgrade_img, 1)
xshopui2_button = button.Button(810, 180, xbutton_img, 1)

#shop img
cheficon_img =  pygame.image.load('gameasset/upgrade shop remaster/chefupgrade.png').convert_alpha()
waitericon_img =  pygame.image.load('gameasset/upgrade shop remaster/waiterupgrade.png').convert_alpha()
star_img = pygame.image.load('gameasset/upgrade shop remaster/star.png').convert_alpha()
upgradebutton_img = pygame.image.load('gameasset/upgrade shop remaster/upgradebuy.png').convert_alpha()
starupgrade_img = pygame.image.load('gameasset/upgrade shop remaster/starupgraded.png').convert_alpha()
shopbackground_img = pygame.image.load('gameasset/upgrade shop remaster/upgradebackground.png').convert_alpha()

#pause img
pausebackground_img = pygame.image.load('gameasset/pause ui/pausebackground.png').convert_alpha()
music_img = pygame.image.load('gameasset/pause ui/music.png').convert_alpha()
continue_img = pygame.image.load('gameasset/pause ui/resume.png').convert_alpha()
pauseexit_img = pygame.image.load('gameasset/pause ui/exit.png').convert_alpha()
reset_img = pygame.image.load('gameasset/pause ui/reset.png').convert_alpha()
mute_img = pygame.image.load('gameasset/pause ui/musicmuted.png').convert_alpha()
pause_mute = button.Button(575, 90, music_img, 1)
pause_unmute =button.Button(575, 90, mute_img, 1)
pause_exit = button.Button(590,250, pauseexit_img,1)
pause_continue = button.Button(740,250, continue_img,1)
pause_reset = button.Button(440,250, reset_img,1)




# shop ui buttons 
xshopbutton_button = button.Button(1100, 30, xbutton_img, 1)
upgrade_button1 = button.Button(1050, 150, upgradebutton_img, 1)
upgrade_button2 = button.Button(1050,315, upgradebutton_img,1)
upgrade_button3 = button.Button(1050,475, upgradebutton_img,1)
upgrade_button4 = button.Button(1050, 150, upgradebutton_img, 1)
upgrade_button5 = button.Button(1050,315, upgradebutton_img,1)
upgrade_button6 = button.Button(1050,475, upgradebutton_img,1)

# decoration ui images
decorationuibackground_img = pygame.image.load('gameasset/decoration ui/decorationuibackground.png').convert_alpha()

piano_img = pygame.image.load('gameasset/decoration ui/piano.png').convert_alpha()
pianoui_img = pygame.image.load('gameasset/decoration ui/pianoui.png').convert_alpha()
buypiano_img = pygame.image.load('gameasset/decoration ui/decorationbuybutton.png').convert_alpha()


menudecoration_img = pygame.image.load('gameasset/decoration ui/menudecoration.png').convert_alpha()
menudecorationui_img = pygame.image.load('gameasset/decoration ui/menudecorationui.png').convert_alpha()
buymenu_img = pygame.image.load('gameasset/decoration ui/decorationbuybutton.png').convert_alpha()

carpet_img = pygame.image.load('gameasset/decoration ui/carpet.png').convert_alpha()
carpetui_img = pygame.image.load('gameasset/decoration ui/carpetui.png').convert_alpha()
buycarpet_img = pygame.image.load('gameasset/decoration ui/decorationbuybutton.png').convert_alpha()

flowers_img = pygame.image.load('gameasset/decoration ui/flowers.png').convert_alpha()
flowersui_img = pygame.image.load('gameasset/decoration ui/flowersui.png').convert_alpha()
buyflowers_img = pygame.image.load('gameasset/decoration ui/decorationbuybutton.png').convert_alpha()

# decoration ui buttons
buymenu_button = button.Button(430+45, 170+125, buymenu_img, 1)
buypiano_button = button.Button(635+45, 170+125, buypiano_img, 1)
buycarpet_button = button.Button(430+45, 400+125, buycarpet_img, 1)
buyflowers_button = button.Button(635+45, 400+125, buyflowers_img, 1)

# create button instances
title_button = button.Button(300, 100, title_img, 0.5)
start_button = button.Button(515, 350, start_img, 0.5)
credit_button = button.Button(515, 450, credit_img, 0.5)
exit_button = button.Button(515, 550, exit_img, 0.5)
pause_button = button.Button(20, 20, pause_img, 2/3)
shop_button  = button.Button(890, 510, shop_img, 2/3)

# click the chef and cat
fern_button = button.Button(498, 300, fern_img, 0.08)


# npc images
chatbubble_img = pygame.image.load('gameasset/chatbubbleremastered.png').convert_alpha()
chatbubble_resize = pygame.transform.scale(chatbubble_img, (int(chatbubble_img.get_width() * 1), int(chatbubble_img.get_height() * 1)))
wrong_img = pygame.image.load('gameasset/wrong.png').convert_alpha()
wrong_scaled = pygame.transform.scale(wrong_img, (int(wrong_img.get_width() * 0.05), int(wrong_img.get_height() * 0.05)))

# sound effects
cat_sfx = pygame.mixer.Sound('gameasset/catmeow.mp3')
music_sfx = pygame.mixer.Sound('gameasset/music2.mp3')
click_sfx = pygame.mixer.Sound('gameasset/click (2).mp3')
pageturn_sfx = pygame.mixer.Sound('gameasset/pageturn.mp3')
dispose_sfx = pygame.mixer.Sound('gameasset/dispose.mp3')

#customersleft image
customersleft_img = pygame.image.load('gameasset/customersleft.png').convert_alpha()

#HOW TO PLAY image
howtoplaybackground_img = pygame.image.load('gameasset/HowToPlay pack/howtoplaybackground.png').convert_alpha()
howtoplaybutton_img = pygame.image.load('gameasset/HowToPlay pack/howtoplaybutton.png').convert_alpha()
howtoplayclosebutton_img = pygame.image.load('gameasset/HowToPlay pack/howtoplayclosebutton.png').convert_alpha()
howtoplaynextbutton_img = pygame.image.load('gameasset/HowToPlay pack/howtoplaynextbutton.png').convert_alpha()
howtoplaypreviousbutton_img = pygame.image.load('gameasset/HowToPlay pack/howtoplaypreviousbutton.png').convert_alpha()

how1_img = pygame.image.load('gameasset/HowToPlay pack/how1.png').convert_alpha()
how2_img = pygame.image.load('gameasset/HowToPlay pack/how2.png').convert_alpha()
how3_img = pygame.image.load('gameasset/HowToPlay pack/how3.png').convert_alpha()
how4_img = pygame.image.load('gameasset/HowToPlay pack/how4.png').convert_alpha()
how5_img = pygame.image.load('gameasset/HowToPlay pack/how5.png').convert_alpha()
how6_img = pygame.image.load('gameasset/HowToPlay pack/how6.png').convert_alpha()
how7_img = pygame.image.load('gameasset/HowToPlay pack/how7.png').convert_alpha()
how8_img = pygame.image.load('gameasset/HowToPlay pack/how8.png').convert_alpha()

howtoplaybutton_button = button.Button(160, 20, howtoplaybutton_img, 1)
howtoplayclosebutton_button = button.Button(225, 520, howtoplayclosebutton_img, 1)
howtoplaynextbutton_button = button.Button(925, 500, howtoplaynextbutton_img, 1)
howtoplaypreviousbutton_button = button.Button(720, 500, howtoplaypreviousbutton_img, 1)

    
def npc(x, y):
    npcalien_width = int(npcalien_img.get_width() * 1)
    npcalien_height = int(npcalien_img.get_height() * 1)
    npcalien_resize= pygame.transform.scale(npcalien_img, (npcalien_width, npcalien_height))
    screen.blit(npcalien_resize, (x, y))

def npc1_animation(action):
    global npcalien_img, npcalien_index
    if action == "standing":
        npcalien_img = npcalien1_img
    if action == "walking":
        npcalien_index += 0.07
        if npcalien_index >= len(npcalien_walk):
            npcalien_index = 0
        npcalien_img = npcalien_walk[int(npcalien_index)]
    if action == "sitting":
        npcalien_img = npcalien4_img

def npc2(x, y):
    npccat_width = int(npccat_img.get_width() * 1)
    npccat_height = int(npccat_img.get_height() * 1)
    npccat_resize= pygame.transform.scale(npccat_img, (npccat_width, npccat_height))
    screen.blit(npccat_resize, (x, y))

def npc2_animation(action):
    global npccat_img, npccat_index
    if action == "standing":
        npccat_img = npccat1_img
    if action == "walking":
        npccat_index += 0.07
        if npccat_index >= len(npccat_walk):
            npccat_index = 0
        npccat_img = npccat_walk[int(npccat_index)]
    if action == "sitting":
        npccat_img = npccat1_img

def npc3(x, y):
    global npcblob_img, npcblob_index
    npcblob_width = int(npcblob_img.get_width() * 1)
    npcblob_height = int(npcblob_img.get_height() * 1)
    npcblob_resize= pygame.transform.scale(npcblob_img, (npcblob_width, npcblob_height))
    screen.blit(npcblob_resize, (x, y))

def npc3_animation(action):
    global npcblob_img, npcblob_index
    if action == "standing":
        npcblob_img = npcblob1_img
    if action == "walking":
        npcblob_index += 0.07
        if npcblob_index >= len(npcblob_walk):
            npcblob_index = 0
        npcblob_img = npcblob_walk[int(npcblob_index)]
    if action == "sitting":
        npcblob_img = npcblob1_img

def waiter(x, y, WaiterDirection):
    waiter_width = int(waiter_img.get_width() * 1)
    waiter_height = int(waiter_img.get_height() * 1)
    waiter_resize = pygame.transform.scale(waiter_img, (waiter_width, waiter_height))
    waiter_flip = pygame.transform.flip(waiter_resize, True, False)
    if WaiterDirection == 'right':
        screen.blit(waiter_resize, (x, y))
    if WaiterDirection == 'left':
        screen.blit(waiter_flip, (x, y))

def waiter_animation(keys):
    global waiter_img, waiter_index
    
    if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
        waiter_index += 0.1
        if waiter_index >= len(waiter_walk):
            waiter_index = 0
        waiter_img = waiter_walk[int(waiter_index)]

    else:
        waiter_img = waiterstand_img

def chef_animation(action):
    global chef_img, chef_index
    if action == "idle":
        chef_img = chefstanding_img
    if action == "cooking":
        chef_index += 0.1
        if chef_index >= len(chef_cooking):
            chef_index = 0
        chef_img = chef_cooking[int(chef_index)]


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

def foodserve(x, y, FoodOnTable):
    foodserve_width = int(FoodOnTable.get_width() *0.5)
    foodserve_height = int(FoodOnTable.get_height() * 0.5)
    foodserve_resize = pygame.transform.scale(FoodOnTable, (foodserve_width, foodserve_height))
    screen.blit(foodserve_resize, (x, y))

def customerplate1(x, y, CustomerFood):
    customerplate1_width = int(CustomerFood.get_width() *0.5)
    customerplate1_height = int(CustomerFood.get_height() *0.5)
    customerplate1_resize = pygame.transform.scale(CustomerFood, (customerplate1_width, customerplate1_height))
    screen.blit(customerplate1_resize, (x, y))

def customerplate2(x, y, CustomerFood22):
    customerplate2_width = int(CustomerFood22.get_width() *0.5)
    customerplate2_height = int(CustomerFood22.get_height() *0.5)
    customerplate2_resize = pygame.transform.scale(CustomerFood22, (customerplate2_width, customerplate2_height))
    screen.blit(customerplate2_resize, (x, y))

def customerplate3(x, y, CustomerFood3):
    customerplate3_width = int(CustomerFood3.get_width() *0.5)
    customerplate3_height = int(CustomerFood3.get_height() *0.5)
    customerplate3_resize = pygame.transform.scale(CustomerFood3, (customerplate3_width, customerplate3_height))
    screen.blit(customerplate3_resize, (x, y))


def foodnpcreq(x,y, randomfood):
    foodnpcreq_width = int(randomfood.get_width() *0.5)
    foodnpcreq_height = int(randomfood.get_height() *0.5)
    foodnpcreq_resize = pygame.transform.scale(randomfood, (foodnpcreq_width, foodnpcreq_height))
    screen.blit(foodnpcreq_resize, (x,y))

def foodnpcreq2(x,y, randomfood):
    foodnpcreq2_width = int(randomfood.get_width() *0.5)
    foodnpcreq2_height = int(randomfood.get_height() *0.5)
    foodnpcreq2_resize = pygame.transform.scale(randomfood, (foodnpcreq2_width, foodnpcreq2_height))
    screen.blit(foodnpcreq2_resize, (x,y))

def foodnpcreq3(x,y, randomfood):
    foodnpcreq3_width = int(randomfood.get_width() *0.5)
    foodnpcreq3_height = int(randomfood.get_height() *0.5)
    foodnpcreq3_resize = pygame.transform.scale(randomfood, (foodnpcreq3_width, foodnpcreq3_height))
    screen.blit(foodnpcreq3_resize, (x,y))

# def casher(x, y):
#     casher_width = int(casher_img.get_width() * 1)
#     casher_height = int(casher_img.get_height() * 1)
#     casher_resize = pygame.transform.scale(casher_img, (casher_width, casher_height))
#     screen.blit(casher_resize, (x, y))

def piano(x, y):
    piano_width = int(piano_img.get_width() * 1)
    piano_height = int(piano_img.get_height() * 1)
    piano_resize = pygame.transform.scale(piano_img, (piano_width, piano_height))
    screen.blit(piano_resize, (x, y))

def collision_detection(waiter_rect, table_rect):

    # print("waiter_rect:", waiter_rect)
    # print("table_rect:", table_rect)
    # print("Collision:", waiter_rect.colliderect(table_rect))


    # Check if two rectangles collide while taking into account the waiter's position
    return waiter_rect.colliderect(table_rect)

def easeOutSine(t):
    return math.sin(t * math.pi / 2)

def main_menu():

    highest_day = load_highest_day() 

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

        # Draw the highscore
        highest_day_font = pygame.font.Font('font/segoepr.ttf', 40)
        highest_day_surf = highest_day_font.render(f"Highest Day: {highest_day}", True, 'darkred')
        highest_day_rect = highest_day_surf.get_rect(bottomleft=(20, screen.get_height() - 20))
        screen.blit(highest_day_surf, highest_day_rect)

        if start_button.draw(screen):
            click_sfx.play()
            tutorial()



        if credit_button.draw(screen):
            click_sfx.play()
            credit_menu()

        if exit_button.draw(screen):

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

def tutorial():
    RunTutorial = True
    dialogueopacity = 0
    dialoguesequence = 0

    waiterdialogueX = 400
    waiteropacity = 0

    chefopacity = 0

    cashieropacity = 0

    ease_out_sine = lambda x: (1 - math.cos(x * math.pi / 2))
    easespeed = 20

    message = ""
    allowedtonext = False

    # intro music
    intromusic = ['gameasset/intro music.mp3', 'gameasset/intro music 2.mp3']
    intromusic_file = random.choice(intromusic)
    pygame.mixer.music.load(intromusic_file)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    
    while RunTutorial:
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
        
        message_font = pygame.font.Font('font/segoepr.ttf', 30)
        message_img = message_font.render((message), True, 'darkred')

        #animate dialoguechat
        if dialogueopacity <= 255 and dialoguesequence == 0:
            dialogueopacity += 8
            if dialogueopacity >= 255:
                dialoguesequence += 1
        
        # ease out movement
        
        
        # waiter chat
        if dialoguesequence == 1:
            allowedtonext = False
            # the amount that will add
            ease_value = easespeed*ease_out_sine(waiterdialogueX / 400) # starts with 500/500 = 1

            #waiter opacity
            if waiteropacity <= 255:
                waiteropacity += 5
            
            #waiter ease out movement
            if ease_value >= 1:
                waiterdialogueX -= ease_value
            if ease_value <= 1:
                message = "WAITER: Oh hello, welcome to the Restaurant Owner!"
                allowedtonext = True

        if dialoguesequence == 2:
            message = "WAITER: I believe that you are the new owner of this restaurant"
            allowedtonext = True

        if dialoguesequence == 3:
            message = "WAITER: I am the waiter, you can control me by pressing W,A,S,D"
            allowedtonext = True
            ease_value = 0
        
        if dialoguesequence == 4:
            allowedtonext = False
            message = ""
            waiteropacity = 150
            if chefopacity <= 255:
                chefopacity += 5
            
            if chefopacity >= 255 :
                message = "CHEF: Nice to meet you, I am the chef"
                allowedtonext = True

        if dialoguesequence == 5:
            message = "CHEF: You can click on me to cook some food"

        if dialoguesequence == 6 :
            allowedtonext = False
            message = ""
            chefopacity = 150

            if cashieropacity <= 255:
                cashieropacity += 5
            
            if cashieropacity >= 255 :
                message = "CASHIER: Wait... who are you?"
                allowedtonext = True

        if dialoguesequence == 7:
            chefopacity = 255
            cashieropacity = 150
            message = "CHEF: The owner"

        if dialoguesequence == 8:
            chefopacity = 150
            cashieropacity = 255
            message = "CASHIER: Oh, I'm sorry... I am the cashier"

        if dialoguesequence == 9:
            message = "CASHIER: I have no particular function in the game..."

        if dialoguesequence == 10:
            message = "CASHIER: But I am here to SUPERVISE you..."

        if dialoguesequence == 11:
            cashieropacity = 150
            waiteropacity = 255
            message = "WAITER: Also, if you accidently chose the wrong food"

        if dialoguesequence == 12:
            message = "WAITER: You can throw food away by pressing E near the trash"

        if dialoguesequence == 13:
            message = "WAITER: And press E to collect food on the counter table"

        if dialoguesequence == 14:
            cashieropacity = 255
            waiteropacity = 150
            message = "CASHIER: Blah blah blah, just do your best!"
        
        if dialoguesequence == 15:
            waiteropacity = 255
            chefopacity = 255
            message = "EVERYONE: Good luck, fellow owner!"

        # display images

        chefdialogue_img.set_alpha(int(chefopacity))
        screen.blit(chefdialogue_img, (800,10))

        waiterdialogue_img.set_alpha(int(waiteropacity))
        screen.blit(waiterdialogue_img, (waiterdialogueX+100,70))

        cashierdialogue_img.set_alpha(int(cashieropacity))
        screen.blit(cashierdialogue_img, (500,100))

        dialogue_img.set_alpha(int(dialogueopacity))
        screen.blit(dialogue_img, (68, 450))

        screen.blit(message_img, (90,470))

        # display skip and next button
        if dialogueopacity >= 255:
            if nextdialogue_button.draw(screen) and allowedtonext == True:
                if dialoguesequence <= 15-1:
                    click_sfx.play()
                    dialoguesequence += 1
                else:
                    click_sfx.play()
                    game_screen()
                    RunTutorial = False

            if skipdialogue_button.draw(screen):
                click_sfx.play()
                game_screen()
                RunTutorial = False


        # # quitting
        # if pause_button.draw(screen):
        #     click_sfx.play()
        #     pygame.mixer.music.stop()
        #     # insert pause code here
        #     RunTutorial = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RunTutorial = False
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(60)
    pass

def load_highest_day():
    try:
        with open('highest_day.txt', 'r') as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 1  # Return 1 if file doesn't exist or content is invalid

# Function to save the highest day to a file
def save_highest_day(day):
    with open('highest_day.txt', 'w') as file:
        file.write(str(day))


def game_screen():
    # money, day = load_game()
    global npc1_x_pos, npc1_img, npc1_y_pos, active_button
    run = True
    
    # stop the intro music
    pygame.mixer.music.stop()

    # load and play bg music
    background_music = 'gameasset/gameplay music.mp3'
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # default money and day value
    money = 150
    prev_money = money
    amountchanged = ""
    moneychangecolor = "darkred"
    moneychangeopacity = 256
    incomemultiplier = 0

    day = 1
    satisfy = day
    daytransition = False
    daytransitiontick = 0
    resetday = False
    
    highest_day = 1
    highest_day = load_highest_day()

    active_button = None 

    tablechair1X = 750
    tablechair1Y = 480

    tablechair2X = 750
    tablechair2Y = 280

    tablechair3X = 400
    tablechair3Y = 480

    WaiterDirection = "right"
    waiterX = 700
    waiterY =  150

    foodserveX = 490
    foodserveY = 240

    customerplate1X = 495
    customerplate1Y = 490

    customerplate2X = 845
    customerplate2Y = 490

    customerplate3X = 845
    customerplate3Y = 290

    npc1_x_pos = 1000
    npc1_y_pos = 100

    npc2_x_pos = 1000
    npc2_y_pos = 100

    npc3_x_pos = 1000
    npc3_y_pos = 100

    npc1reset = True
    npc2reset = True
    npc3reset = True    

    # pause ui
    runpauseUI = False

    # chef UI
    runchefUI = False
    rundecorationUI = False
    cooking = emptybox_img
    progress = 0
    FoodOnTable = emptybox_img
    waiterfood = emptybox_img
    CustomerFood = emptybox_img
    CustomerFood2 = emptybox_img
    CustomerFood3 = emptybox_img
    chefcookingtime = 0

    # shop ui 
     
    runShopUI = False
    waiter_speed = 2
    chef = star_img
    chef2 = star_img
    chef3 = star_img 
    waiter1 = star_img
    waiter2 = star_img
    waiter3 = star_img
    purchasechef1 = False
    purchasechef2 = False
    purchasechef3 = False
    purchasewaiter1 = False
    purchasewaiter2 = False
    purchasewaiter3 = False
    
     

    chefcookingtime = 1


    # shopui2
    runShopUI2 = False

    #decoration
    purchasedmenu = False
    purchasedpiano = False
    purchasedcarpet = False
    purchasedflowers = False

    # casher collision
    casherX = 472
    casherY = 46

    # deco collision
    pianoX = 680
    pianoY = 15

    #npc
    npcfoodrequest = False
    npcfoodrequest2 = False
    npcfoodrequest3 = False
    earnmoney = False
    wrongfood = False
    npcleave = False
    npcwaittime = 0
    npcqueuetime = 0
    npceatingtime = 0
    npcdisgustedwait = 0
    waitprogress = 0
    waitprogress2 = 0
    waitprogress3 = 0
    waitdelay = 0
    npcnumber = 0
    randomfood = emptybox_img
    foodchoice = [chicken_img, fish_img, burger_img, pizza_img, steak_img]
    npcappeartime1 = 0

    npcstop = False

    # HOW TO PLAY
    runhowtoplayUI = True
    howtoplaypicture = [how1_img,how2_img,how3_img,how4_img,how5_img,how6_img,how7_img,how8_img,]
    howtoplay_index = 0

    # The game won't start until the tutorial is closed for the first time
    howtoplaygameplaycooldown = False


    # rect object for waiter
    waiter_rect = pygame.Rect(waiterX, waiterY, waiter_img.get_width(), waiter_img.get_height()-100)
    # rect object for table and chair
    tablechair1_rect = pygame.Rect(tablechair1X, tablechair1Y, 252, 80)
    tablechair2_rect = pygame.Rect(tablechair2X, tablechair2Y, 252, 80)
    tablechair3_rect = pygame.Rect(tablechair3X, tablechair3Y, 252, 80)

    

    # food rect and surf
    foodtrigger_surf = pygame.image.load('gameasset/chef ui/emptybox.png').convert_alpha()
    foodtrigger_scaled = pygame.transform.scale(foodtrigger_surf, (foodtrigger_surf.get_width() * 0.5, foodtrigger_surf.get_height() * 0.5))
    foodtrigger_scaled.set_alpha(0)
    foodtrigger_rect = foodtrigger_scaled.get_rect(topleft = (550, 255))

    #trash
    trashtrigger_surf = pygame.image.load('gameasset/trash.png').convert_alpha()
    trashtrigger_rect = trashtrigger_surf.get_rect(topleft = (570, 80))

    # casher object
    casher_rect = pygame.Rect(casherX, casherY, 80, 350)

    # rect object for deco
    piano_rect = pygame.Rect(pianoX, pianoY, 160, 40)

    # days progression


    while run:
        # game screen code here
        screen.fill((255, 255, 255))
        screen.blit(bg_game_screen, (0, 0))

        # RESET DAY 
        if resetday == True:
            day += 1
            satisfy = day
            npcnumber = 0

            npc1_x_pos = 1000
            npc1_y_pos = 100
            npc2_x_pos = 1000
            npc2_y_pos = 100
            npc3_x_pos = 1000
            npc3_y_pos = 100

            npcfoodrequest = False
            npcfoodrequest2 = False
            npcfoodrequest3 = False

            earnmoney = False
            earnmoney2 = False
            earnmoney3 = False

            wrongfood = False
            wrongfood2 = False
            wrongfood3 = False

            npcleave = False
            npcleave2 = False
            npcleave3 = False

            npcwaittime= 0
            npcwaittime2 = 0
            npcwaittime3 = 0

            npcqueuetime = 0
            npcqueuetime2 = 0
            npcqueuetime3 = 0

            npceatingtime = 0
            npceatingtime2 = 0
            npceatingtime3 = 0

            waitprogress = 0
            waitprogress2 = 0
            waitprogress3 = 0

            waitdelay = 0
            waitdelay2 = 0
            waitdelay3 = 0

            npcnumber = 0

            npcdisgustedwait = 0
            npcdisgustedwait2 = 0
            npcdisgustedwait3 = 0

            randomfood = emptybox_img
            randomfood2 = emptybox_img
            randomfood3 = emptybox_img

            npcappeartime1 = 0
            npcappeartime2 = 0
            npcappeartime3 = 0

            npc1reset = True
            npc2reset = True
            npc3reset = True

            FoodOnTable = emptybox_img
            CustomerFood = emptybox_img
            CustomerFood2 = emptybox_img
            customerFood3 = emptybox_img

            npcstop = False

            resetday = False




# NPC 1 RESET --------------------------------------------------------------------------------------------------------------#
        if npc1reset == False and npcstop == False:

            npc1_x_pos = 1000
            npc1_y_pos = 100

            npcfoodrequest = False

            earnmoney = False

            wrongfood = False

            npcleave = False

            npcwaittime= 0

            npcqueuetime = 0

            npceatingtime = 0

            waitprogress = 0

            waitdelay = 0

            npcdisgustedwait = 0

            randomfood = emptybox_img

            npc1reset = True  

            npcappeartime1 = 0


# NPC 1 RESET --------------------------------------------------------------------------------------------------------------#

# NPC 2 RESET --------------------------------------------------------------------------------------------------------------#
        if npc2reset == False  and npcstop == False:

            npc2_x_pos = 1000
            npc2_y_pos = 100

            npcfoodrequest2 = False

            earnmoney2 = False

            wrongfood2 = False

            npcleave2 = False

            npcwaittime2 = 0

            npcqueuetime2 = 500

            npceatingtime2 = 0

            waitprogress2 = 0

            waitdelay2 = 0

            npcdisgustedwait2 = 0

            randomfood2 = emptybox_img

            npcappeartime2 = 500
            
            npc2reset = True  
# NPC 2 RESET --------------------------------------------------------------------------------------------------------------#

# NPC 3 RESET --------------------------------------------------------------------------------------------------------------#
        
        if npc3reset == False and npcstop == False:

            npc3_x_pos = 1000
            npc3_y_pos = 100

            npcfoodrequest3 = False

            earnmoney3 = False

            wrongfood3 = False

            npcleave3 = False

            npcwaittime3 = 0

            npcqueuetime3 = 1000

            npceatingtime3 = 0

            waitprogress3 = 0

            waitdelay3 = 0

            npcdisgustedwait3 = 0

            randomfood3 = emptybox_img

            npcappeartime3 = 1000
            
            npc3reset = True  

# NPC 3 RESET --------------------------------------------------------------------------------------------------------------#


        # if fern_button.draw(screen) and runchefUI == False and runShopUI2 == True and rundecorationUI == True:
        #     cat_sfx.play()


        # get the state of all keyboard keys
        keys = pygame.key.get_pressed()

        # update waiter position based on key presses
        waiter_animation(keys)
        if keys[pygame.K_w]:
            if waiterY > 0:
                waiterY -= waiter_speed
        if keys[pygame.K_s]:
            if waiterY < 520:
                waiterY += waiter_speed
        if keys[pygame.K_a]:
            WaiterDirection = 'right'
            if waiterX > 381:
                waiterX -= waiter_speed
        if keys[pygame.K_d]:
            WaiterDirection = 'left'
            if waiterX < 1045:
                waiterX += waiter_speed

        # update waiter Rect object position
        waiter_rect.bottomleft = (waiterX, waiterY+110)

        # rectangle draw testing
        # pygame.draw.rect(screen, 'red', waiter_rect, 2)

        # pygame.draw.rect(screen, 'red', tablechair1_rect, 2)
        # pygame.draw.rect(screen, 'red', tablechair2_rect, 2)
        # pygame.draw.rect(screen, 'red', tablechair3_rect, 2)



        # check for collision between waiter and table chair (1)
        if collision_detection(waiter_rect, tablechair1_rect):
        # If collision is detected, prevent waiter from moving in that direction
            if keys[pygame.K_w] and waiter_rect.top < tablechair1_rect.bottom:
                waiterY += waiter_speed
            if keys[pygame.K_s] and waiter_rect.bottom > tablechair1_rect.top:
                waiterY -= waiter_speed
            if keys[pygame.K_a] and waiter_rect.left < tablechair1_rect.right:
                waiterX += waiter_speed
            if keys[pygame.K_d] and waiter_rect.right > tablechair1_rect.left:
                waiterX -= waiter_speed

            if CustomerFood2 == emptybox_img and npcfoodrequest2 == True and npc2_x_pos == 950:
                CustomerFood2 = waiterfood
                waiterfood = emptybox_img
                cooking = emptybox_img


        # check for collision between waiter and table chair (2)
        if collision_detection(waiter_rect, tablechair2_rect):
        # If collision is detected, prevent waiter from moving in that direction
            if keys[pygame.K_w] and waiter_rect.top < tablechair2_rect.bottom:
                waiterY += waiter_speed
            if keys[pygame.K_s] and waiter_rect.bottom > tablechair2_rect.top:
                waiterY -= waiter_speed
            if keys[pygame.K_a] and waiter_rect.left < tablechair2_rect.right:
                waiterX += waiter_speed
            if keys[pygame.K_d] and waiter_rect.right > tablechair2_rect.left:
                waiterX -= waiter_speed
            if CustomerFood3 == emptybox_img and npcfoodrequest3 == True and npc3_x_pos == 950:
                CustomerFood3 = waiterfood
                waiterfood = emptybox_img
                cooking = emptybox_img

        # check for collision between waiter and table chair (3)
        if collision_detection(waiter_rect, tablechair3_rect):
        # If collision is detected, prevent waiter from moving in that direction
            if keys[pygame.K_w] and waiter_rect.top < tablechair3_rect.bottom:
                waiterY += waiter_speed
            if keys[pygame.K_s] and waiter_rect.bottom > tablechair3_rect.top:
                waiterY -= waiter_speed
            if keys[pygame.K_a] and waiter_rect.left < tablechair3_rect.right:
                waiterX += waiter_speed
            if keys[pygame.K_d] and waiter_rect.right > tablechair3_rect.left:
                waiterX -= waiter_speed
            
            if CustomerFood == emptybox_img and npcfoodrequest == True and npc1_x_pos == 595:
                CustomerFood = waiterfood
                waiterfood = emptybox_img
                cooking = emptybox_img

        # check for collision between waiter and counter
        if collision_detection(waiter_rect, casher_rect):
        # If collision is detected, prevent waiter from moving in that direction
            if keys[pygame.K_w] and waiter_rect.top < casher_rect.bottom:
                waiterY += waiter_speed
            if keys[pygame.K_s] and waiter_rect.bottom > casher_rect.top:
                waiterY -= waiter_speed
            if keys[pygame.K_a] and waiter_rect.left < casher_rect.right:
                waiterX += waiter_speed
            if keys[pygame.K_d] and waiter_rect.right > casher_rect.left:
                waiterX -= waiter_speed



        # game font variables such as day count and money count
        daycycle_font = pygame.font.Font('font/segoepr.ttf', 30)
        daycycle_surf = daycycle_font.render(str(day), True, 'darkred')
        daycycle_rect = daycycle_surf.get_rect(topleft=(490,620))

        customer_font = pygame.font.Font('font/segoepr.ttf', 45)
        customer_surf = customer_font.render(str(max(satisfy,0)), True, 'darkred')
        customer_rect = customer_surf.get_rect(topleft=(790,585))

        money_font = pygame.font.Font('font/segoepr.ttf', 40)
        money_surf = money_font.render(str(int(money)), True, 'darkred')
        money_rect = money_surf.get_rect(topleft=(165,598))

        moneychange_font = pygame.font.Font('font/segoepr.ttf', 40)
        moneychange_surf = moneychange_font.render(amountchanged, True, moneychangecolor)
        moneychange_surf.set_alpha(moneychangeopacity)
        moneychange_rect = moneychange_surf.get_rect(topleft=(165,540))

        # pressE_font = pygame.font.Font('font/segoepr.ttf', 20)
        # pressE_surf = pressE_font.render("Press E to pick the food", True, "darkred")

        pressE_surf = pygame.image.load('gameasset/pickfoodhint.png').convert_alpha()
        pressE_rect = pressE_surf.get_rect(topleft=(waiterX-40,waiterY-30))

        # pressSPACE_font = pygame.font.Font('font/segoepr.ttf', 20)
        # pressSPACE_surf = pressSPACE_font.render("Press SPACE to throw away food", True, "darkred")
        pressSPACE_surf = pygame.image.load('gameasset/disposefoodhint.png').convert_alpha()
        pressSPACE_rect = pressSPACE_surf.get_rect(topleft=(waiterX-40,waiterY+110))


        if day > highest_day:
            highest_day = day
            save_highest_day(highest_day)

        if money < 0 :  # Check if money is negative, display game over
            # game_over_font = pygame.font.Font('font/segoepr.ttf', 80)
            # game_over_surf = game_over_font.render("Game Over", True, 'red')
            game_over_img = pygame.image.load('gameasset/gameover.png').convert_alpha()
            game_over_rect = game_over_img.get_rect(center=(screen.get_width()//2, screen.get_height()//2))
            screen.blit(game_over_img, game_over_rect)


            highest_day_font = pygame.font.Font('font/segoepr.ttf', 40)
            highest_day_surf = highest_day_font.render(f"Highest Day: {highest_day}", True, 'darkred')
            highest_day_rect = highest_day_surf.get_rect(center=(screen.get_width()//2, screen.get_height()//2 + 80))

            
            screen.blit(highest_day_surf, highest_day_rect)
    
            pygame.display.update()
            pygame.time.delay(2000)
            main_menu()


        if pause_button.draw(screen):
            click_sfx.play()
            game_pause()
            
        chef_button = button.Button(200, 215, chef_img, 1)
        
        # Decoration bought items
        if purchasedmenu == True:
            screen.blit(menudecoration_img, (336,236))


        if purchasedpiano == True:
            screen.blit(piano_img, (680,15))
        # check for collision between waiter and piano
            if collision_detection(waiter_rect, piano_rect):
                # If collision is detected, prevent waiter from moving in that direction
                    if keys[pygame.K_w] and waiter_rect.top < piano_rect.bottom:
                        waiterY += waiter_speed
                    if keys[pygame.K_s] and waiter_rect.bottom > piano_rect.top:
                        waiterY -= waiter_speed
                    if keys[pygame.K_a] and waiter_rect.left < piano_rect.right:
                        waiterX += waiter_speed
                    if keys[pygame.K_d] and waiter_rect.right > piano_rect.left:
                        waiterX -= waiter_speed
        

        if purchasedcarpet == True:
            screen.blit(carpet_img, (400,270))

        if purchasedflowers == True:
            screen.blit(flowers_img, (1065,300))

        table1(tablechair1X,tablechair1Y)

        table2(tablechair2X,tablechair2Y)

        table3(tablechair3X,tablechair3Y)

        customerplate1(customerplate1X,customerplate1Y, CustomerFood)

        customerplate2(customerplate2X,customerplate2Y, CustomerFood2)

        customerplate3(customerplate3X,customerplate3Y, CustomerFood3)

        if day >= 1:
            npcappeartime1 += 1
            if npcappeartime1 >= 150:
                npc(npc1_x_pos, npc1_y_pos)

        if day >= 2:
            npcappeartime2 +=1
            if npcappeartime2 >= 600:
                npc2(npc2_x_pos,npc2_y_pos)
        
        if day >= 3:
            npcappeartime3 +=1
            if npcappeartime3 >= 1100:
                npc3(npc3_x_pos,npc3_y_pos)

        #table4(tablechair4X,tablechair4Y)
        
        
        # Chef UI ====================================== #
        
        # chef progress bar
        progressbar_font = pygame.font.Font('font/segoepr.ttf', 15)
        progressbar_surf = progressbar_font.render('.'*progress, False, (64,64,64))
        progressbar_rect = progressbar_surf.get_rect(midleft = (615,535))

        if chef_button.draw(screen):
            click_sfx.play()
            runchefUI = True
            runShopUI2 = False
            rundecorationUI = False
            runShopUI = False


        #trashcan=============================================#
        screen.blit(trashtrigger_surf, trashtrigger_rect,) # foodtrigger

        # food serve (part 1) ================================ #
        screen.blit(foodtrigger_scaled, foodtrigger_rect,) # foodtrigger
        foodserve(foodserveX,foodserveY,FoodOnTable)
        
        #hint to click E to get the food
        if foodtrigger_rect.colliderect(waiter_rect) and FoodOnTable != emptybox_img:
            screen.blit(pressE_surf,pressE_rect)

        #hint to click SPACE to throw away food
        if trashtrigger_rect.colliderect(waiter_rect) and waiterfood != emptybox_img:
            screen.blit(pressSPACE_surf,pressSPACE_rect)

        waiter(waiterX, waiterY, WaiterDirection)
        screen.blit(waiterfood, (waiterX - 35,waiterY - 105))
        # food serve ================================ #

        # cashier
        screen.blit(cashiernpc_flip, (425,90))



        # npc movement ================================== #
        waitbar_font = pygame.font.Font('font/segoepr.ttf', 5)
        waitbar_surf = waitbar_font.render('.'*waitprogress, False, (64,64,64))
        waitbar_rect = waitbar_surf.get_rect(midleft = (npc1_x_pos,npc1_y_pos - 120))

        waitbar_font2 = pygame.font.Font('font/segoepr.ttf', 5)
        waitbar_surf2 = waitbar_font2.render('.'*waitprogress2, False, (64,64,64))
        waitbar_rect2 = waitbar_surf2.get_rect(midleft = (npc2_x_pos,npc2_y_pos - 120))

        waitbar_font3 = pygame.font.Font('font/segoepr.ttf', 5)
        waitbar_surf3 = waitbar_font3.render('.'*waitprogress3, False, (64,64,64))
        waitbar_rect3 = waitbar_surf3.get_rect(midleft = (npc3_x_pos,npc3_y_pos - 120))
        
        if npcnumber == day:
            npcstop = True
            if int(max(satisfy,0)) == 0 and npcstop == True:
                npc1_x_pos = -1000
                npc2_x_pos = -1000
                npc3_x_pos = -1000
                npcfoodrequest = True
                npcfoodrequest2 = True
                npcfoodrequest3 = True

        if npcfoodrequest == False and howtoplaygameplaycooldown == True:
            npcqueuetime +=1
            npc1_animation("standing")
            if npcqueuetime >= 250:
                npc1_animation("walking")
                npc1_x_pos -= 1.5
                if npc1_x_pos <= 650:  
                    npc1_x_pos = 651
                    npc1_y_pos += 1.5

                    if npc1_y_pos >= 340: 
                        npc1_y_pos = 435
                        npc1_x_pos = 595
                        npc1_animation("sitting")
                        npcfoodrequest = True



        if npcfoodrequest == True and not npc1_x_pos == -1000 and not npc1_y_pos == -1000:
            npcwaittime += 1
            if npcwaittime >= 50 and randomfood == emptybox_img:
                randomfood = random.choice(foodchoice)

            if randomfood != emptybox_img:

                if  CustomerFood == emptybox_img:
                    screen.blit(waitbar_surf, waitbar_rect)
                    pygame.draw.rect(screen,'red',waitbar_rect)
                    screen.blit(chatbubble_resize, (npc1_x_pos,npc1_y_pos - 100))
                    foodnpcreq(npc1_x_pos + 33,npc1_y_pos - 90, randomfood)
                    waitdelay += 1
                    

                # increase letter wait bar
                # letter increase 1 (waitprogress) when waitdelay equals 4
                if waitdelay >= 10:
                    waitprogress += 1
                    waitdelay = 0
                
                # Customer gets the right food
                if  CustomerFood == randomfood and earnmoney == False and not npc1_x_pos == -1000:
                    npceatingtime += 1

                    if npceatingtime >= 100:
                        money += 100 + 100*incomemultiplier/100
                        npc1_x_pos = -1000
                        npcnumber += 1
                        CustomerFood = emptybox_img
                        satisfy -= 1
                        earnmoney = True

                        if day >= 4 and npc1_x_pos == -1000 and npcstop == False:
                            npc1reset = False
                                


                # Customer gets the wrong food
                if CustomerFood != randomfood and wrongfood == False and CustomerFood != emptybox_img and not npc1_x_pos == -1000:
                    npcdisgustedwait += 1
                    screen.blit(wrong_scaled, (npc1_x_pos + 5,npc1_y_pos - 40))

                    if npcdisgustedwait >= 100:
                        money -= 50
                        npc1_x_pos = -1000
                        CustomerFood = emptybox_img
                        wrongfood = True   
                    
                        if day >= 1 and npc1_x_pos == -1000:
                            npc1reset = False

                # Customer wait time runs out
                if waitprogress >= 135 and CustomerFood == emptybox_img and npcleave == False and not npc1_x_pos == -1000:
                    money -= 50
                    npc1_x_pos = -1000
                    npcleave = True
                    
                    if day >= 1 and  npc1_x_pos == -1000:
                        npc1reset = False
        #npc 2 ======================================#
        if day >= 2 and npcfoodrequest2 == False:
            npcqueuetime2 += 1
            npc2_animation("standing")
            if npcqueuetime2 >= 700:
                npc2_animation("walking")
                npc2_x_pos -= 1.5
                if npc2_x_pos <= 650:  
                    npc2_x_pos = 651
                    npc2_y_pos += 1.5

                    if npc2_y_pos >= 340: 
                        npc2_animation("sitting")
                        npc2_y_pos = 435
                        npc2_x_pos = 950
                        npcfoodrequest2 = True

        if npcfoodrequest2 == True and not npc2_x_pos == -1000 and not npc2_y_pos == -1000:
            npcwaittime2 += 1
            if npcwaittime2 >= 50 and randomfood2 == emptybox_img:
                randomfood2 = random.choice (foodchoice)

            if randomfood2 != emptybox_img:

                if  CustomerFood2 == emptybox_img:
                    screen.blit(waitbar_surf2, waitbar_rect2)
                    pygame.draw.rect(screen,'red',waitbar_rect2)
                    screen.blit(chatbubble_resize, (npc2_x_pos,npc2_y_pos - 100))
                    foodnpcreq2(npc2_x_pos + 33,npc2_y_pos - 90, randomfood2)
                    waitdelay2 += 1
                        

                # increase letter wait bar
                # letter increase 1 (waitprogress) when waitdelay equals 4
                if waitdelay2 >= 10:
                    waitprogress2 += 1
                    waitdelay2 = 0
                    
                # Customer gets the right food
                if  CustomerFood2 == randomfood2 and earnmoney2 == False and not npc2_x_pos == -1000:
                    npceatingtime2 += 1

                    if npceatingtime2 >= 100:
                        money += 100 + 100*incomemultiplier/100
                        npc2_x_pos = -1000
                        npcnumber += 1
                        CustomerFood2 = emptybox_img
                        satisfy -= 1
                        earnmoney2 = True

                        if day >= 5 and npc2_x_pos == -1000:
                            npc2reset = False
                    
                    # Customer gets the wrong food
                if CustomerFood2 != randomfood2 and wrongfood2 == False and CustomerFood2 != emptybox_img and not npc2_x_pos == -1000:
                    npcdisgustedwait2 += 1
                    screen.blit(wrong_scaled, (npc2_x_pos + 5,npc2_y_pos - 40))

                    if npcdisgustedwait2 >= 100:
                        money -= 50
                        npc2_x_pos = -1000
                        CustomerFood2 = emptybox_img
                        wrongfood2 = True

                        if npc2_x_pos == -1000:
                            npc2reset = False
                    
                # Customer wait time runs out
                if waitprogress2 >= 135 and CustomerFood2 == emptybox_img and npcleave2 == False and not npc2_x_pos == -1000:
                    money -= 50
                    npc2_x_pos = -1000
                    npcleave2 = True
                    
                    if npc2_x_pos == -1000:
                        npc2reset = False
        
    
        #npc 3 =================================================================================#
        if day >= 3 and npcfoodrequest3 == False:
            npcqueuetime3 += 1
            npc3_animation("standing")
            if npcqueuetime3 >= 1200:
                npc3_animation("walking")
                npc3_x_pos -= 1.5
                if npc3_x_pos <= 650:  
                    npc3_x_pos = 651
                    npc3_y_pos += 1.5

                    if npc3_y_pos >= 240: 
                        npc3_animation("sitting")
                        npc3_y_pos = 230
                        npc3_x_pos = 950
                        npcfoodrequest3 = True

        if npcfoodrequest3 == True and not npc3_x_pos == -1000 and not npc3_y_pos == -1000:
            npcwaittime3 += 1
            if npcwaittime3 >= 50 and randomfood3 == emptybox_img:
                randomfood3 = random.choice (foodchoice)

            if randomfood3 != emptybox_img:

                if  CustomerFood3 == emptybox_img:
                    screen.blit(waitbar_surf3, waitbar_rect3)
                    pygame.draw.rect(screen,'red',waitbar_rect3)
                    screen.blit(chatbubble_resize, (npc3_x_pos,npc3_y_pos - 100))
                    foodnpcreq2(npc3_x_pos + 33,npc3_y_pos - 90, randomfood3)
                    waitdelay3 += 1
                        

                # increase letter wait bar
                # letter increase 1 (waitprogress) when waitdelay equals 4
                if waitdelay3 >= 10:
                    waitprogress3 += 1
                    waitdelay3 = 0
                    
                # Customer gets the right food
                if  CustomerFood3 == randomfood3 and earnmoney3 == False and not npc3_x_pos == -1000:
                    npceatingtime3 += 1

                    if npceatingtime3 >= 100:
                        money += 100+100*incomemultiplier/100
                        npc3_x_pos = -1000
                        npcnumber += 1
                        CustomerFood3 = emptybox_img
                        satisfy -= 1
                        earnmoney3 = True
                        
                        if day >= 6 and npc3_x_pos == -1000:
                            npc3reset = False
                    
                    # Customer gets the wrong food
                if CustomerFood3 != randomfood3 and wrongfood3 == False and CustomerFood3 != emptybox_img and not npc3_x_pos == -1000:
                    npcdisgustedwait3 += 1
                    screen.blit(wrong_scaled, (npc3_x_pos + 5,npc3_y_pos - 40))

                    if npcdisgustedwait3 >= 100:
                        money -= 50
                        npc3_x_pos = -1000
                        CustomerFood3 = emptybox_img
                        wrongfood3 = True

                        if npc3_x_pos == -1000:
                            npc3reset = False
                    
                    # Customer wait time runs out
                if waitprogress3 >= 135 and CustomerFood3 == emptybox_img and npcleave3 == False and not npc3_x_pos == -1000:
                    money -= 50
                    npc3_x_pos = -1000
                    npcleave3 = True

                    if npc3_x_pos == -1000:
                        npc3reset = False
            

        # npc movement ==============================

        # GUI
        screen.blit(moneycounter_img, (30,530))
        screen.blit(daycounter_img, (380,615))
        screen.blit(daycycle_surf,daycycle_rect)
        screen.blit(money_surf,money_rect)
        screen.blit(moneychange_surf,moneychange_rect)
        screen.blit(customersleft_img, (580,586))
        screen.blit(customer_surf, customer_rect)

        # BLACK SCREEN TRANSITION
        if int(max(satisfy,0)) == 0:
            if nextday_button.draw(screen):
                    click_sfx.play()
                    daytransition = True
                    resetday = True

        # insert shop code here
        if rundecorationUI == False and runShopUI2 == False and runShopUI == False and runhowtoplayUI == False:
            if shop_button.draw(screen):
                click_sfx.play()
                runShopUI2 = True 
                runchefUI = False
                rundecorationUI = False
                runShopUI = False

        if runShopUI2 == True:
            screen.blit(shopui2background_img, (410,175))

            if xshopui2_button.draw(screen):
                click_sfx.play()
                runShopUI2 = False
            if shopdecoration_button.draw(screen):
                click_sfx.play()
                rundecorationUI = True
                runShopUI2 = False
            if shopupgrade_button.draw(screen):
                click_sfx.play()
                runShopUI = True
                runShopUI2 = False


        if runShopUI == True:

            
            screen.blit(shopbackground_img, (410,25))
            screen.blit(cheficon_img, (440,135))
            screen.blit(waitericon_img, (440,295))
            # screen.blit(cheficon_img, (440,450))
            screen.blit(chef, (610,155))
            screen.blit(chef2, (710,155))
            screen.blit(chef3, (810,155))
            screen.blit(waiter1, (610,315))
            screen.blit(waiter2, (710,315))
            screen.blit(waiter3, (810,315))
            
            
            if xshopbutton_button.draw(screen) :
                click_sfx.play()
                runShopUI = False

            
            if upgrade_button1.draw(screen):
               
                if money >= 150 and  purchasechef2 == True and purchasechef3 == False :
                    click_sfx.play()
                    chef3 = starupgrade_img
                    money -= 150 
                    chefcookingtime = 4
                    purchasechef3 = True

                if money >= 150 and purchasechef1 == True and purchasechef2 == False and purchasechef3 == False:
                    click_sfx.play()
                    chef2 = starupgrade_img
                    money -= 150
                    chefcookingtime = 3
                    purchasechef2 = True

                if money >= 150 and purchasechef1 == False and purchasechef2 == False and purchasechef3 == False:
                    click_sfx.play()
                    chef = starupgrade_img
                    money -= 150
                    chefcookingtime = 2
                    purchasechef1 = True 
                    
                
            if upgrade_button2.draw(screen):

                if money >= 250 and  purchasewaiter2 == True and purchasewaiter3 == False :
                    click_sfx.play()
                    waiter3 = starupgrade_img
                    money -= 250
                    waiter_speed = 6
                    purchasewaiter3 = True

                if money >= 250 and purchasewaiter1 == True and purchasewaiter2 == False and purchasewaiter3 == False :
                    click_sfx.play()
                    waiter2 = starupgrade_img
                    money -= 250
                    waiter_speed = 5
                    purchasewaiter2 = True

                if money >= 250 and purchasewaiter1 == False and purchasewaiter2 == False and purchasewaiter3 == False:
                    click_sfx.play()
                    waiter1 = starupgrade_img
                    money -= 250
                    waiter_speed = 4
                    purchasewaiter1 =True

                
        chef_animation("idle")
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
                money -= 18
                # if the player clicks on the food icon, it will be added to the cooking slot

            if fish_button.draw(screen) and cooking == emptybox_img:
                click_sfx.play()
                cooking = fish_img
                money -= 12

            if burger_button.draw(screen) and cooking == emptybox_img:
                click_sfx.play()
                cooking = burger_img
                money -= 30

            if pizza_button.draw(screen) and cooking == emptybox_img:
                click_sfx.play()
                cooking = pizza_img
                money -= 35
                
            if steak_button.draw(screen) and cooking == emptybox_img:
                click_sfx.play()
                cooking = steak_img
                money -= 60

            
        if cooking != emptybox_img:
            chef_animation("cooking")
            if progress <= 130:
                progress += chefcookingtime

                if chefcookingtime >= 5:
                    progress += chefcookingtime
                    chefcookingtime = 0       
            else:
                FoodOnTable = cooking
                cooking = emptybox_img
                progress = 0
                

            screen.blit(cooking, (450,480))
            screen.blit(progressbar_img, (605,515))
            screen.blit(progressbar_surf, progressbar_rect)
            pygame.draw.rect(screen,'red',progressbar_rect)
        # Chef UI ====================================== #

       
        # Decoration UI ================================= #
        if rundecorationUI == True:
            screen.blit(decorationuibackground_img, (410,65))


            screen.blit(menudecorationui_img, (430,170))
            screen.blit(pianoui_img, (635,170))
            screen.blit(carpetui_img, (430,400))
            screen.blit(flowersui_img, (635,400))

            if xbutton_button.draw(screen):
                click_sfx.play()
                rundecorationUI = False
            if purchasedmenu == False:
                if buymenu_button.draw(screen) and money >= 250:
                    click_sfx.play()
                    money -= 250
                    incomemultiplier += 5
                    purchasedmenu = True

            if purchasedpiano == False:    
                if buypiano_button.draw(screen) and money >= 500:
                    click_sfx.play()
                    money -= 500
                    incomemultiplier += 10
                    purchasedpiano = True
            
            if purchasedcarpet == False:
                if buycarpet_button.draw(screen) and money >= 1000:
                    click_sfx.play()
                    money -= 1000
                    incomemultiplier += 12
                    purchasedcarpet = True

            if purchasedflowers == False:
                if buyflowers_button.draw(screen) and money >= 375:
                    click_sfx.play()
                    money -= 375
                    incomemultiplier += 8
                    purchasedflowers = True

        # Decoration UI ================================= #

        # HOW TO PLAY
    
        if runhowtoplayUI == False and howtoplaybutton_button.draw(screen):
            click_sfx.play()
            runhowtoplayUI = True

        if runhowtoplayUI == True:
            screen.blit(howtoplaybackground_img, (200,50))
            
            if howtoplayclosebutton_button.draw(screen):
                click_sfx.play()
                howtoplaygameplaycooldown = True
                runhowtoplayUI = False
            if howtoplay_index <= 6 and howtoplaynextbutton_button.draw(screen):
                pageturn_sfx.play()
                howtoplay_index += 1
            if howtoplay_index >= 1 and howtoplaypreviousbutton_button.draw(screen):
                pageturn_sfx.play()
                howtoplay_index -= 1

            howtoplay = howtoplaypicture[howtoplay_index]
            screen.blit(howtoplay, (230,150))


        # food serve (part 2) ================================ #

        #hint to click E to get the food

        if foodtrigger_rect.colliderect(waiter_rect) and keys[pygame.K_e]:
            
            if waiterfood == emptybox_img:
                # Food that the waiter is carrying
                waiterfood = FoodOnTable

                # Food on top of counter
                FoodOnTable = emptybox_img

        # food serve ================================ #

        #hint to click E to dispose food
        if trashtrigger_rect.colliderect(waiter_rect) and keys[pygame.K_e]:
            if waiterfood != emptybox_img:
                dispose_sfx.play()
                # Food that the waiter is carrying
                waiterfood = emptybox_img

        # Day reset black =============================== #
        if daytransition == True:
            screen.fill((0,0,0))
            transition_font = pygame.font.Font('font/segoepr.ttf', 60)
            transition_surf = transition_font.render(f"Day {day}", True, 'white')
            transition_rect = money_surf.get_rect(center=(590,340))
            screen.blit(transition_surf, transition_rect)
            daytransitiontick += 1

            if daytransitiontick >= 50:
                daytransitiontick = 0
                daytransition = False
        # Day reset black =============================== #

        # detect if money is changed ==================== #
        if money!= prev_money:
            
            # decrease money
            if prev_money >= money:
                amountchanged = f"-{int(prev_money-money)}"
                moneychangecolor = "red"
                moneychangeopacity = 256
            
            # increase money
            if money >= prev_money:
                amountchanged = f"+{int(money-prev_money)}"
                moneychangecolor = "darkgreen"
                moneychangeopacity = 256
            prev_money = money
        if moneychangeopacity >= 0:
            moneychangeopacity -= 3
        # detect if money is changed ==================== #

        
        
        # vignette
        screen.blit(vignette_img, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # saveloadmanager.save_data() # <--- STOP HERE 7/5/24
                # save_game(money, day)   
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(60)


def game_pause ():
    
    global runpauseUI, active_button

    runpauseUI = True

    music_playing = True

    click_playing = True


    

    while runpauseUI:

        
        
        # Draw the shop background
        
        screen.blit(pausebackground_img, (410, 25))


        if pause_mute.draw(screen):
            click_sfx.play()
            
            if music_playing:
                mixer.music.stop()  # Stop background music if playing
                active_button = pause_unmute
            else:
              mixer.music.play(-1)  # Play background music if stopped
              active_button = pause_mute
            music_playing = not music_playing  # Toggle music state

        

        if pause_continue.draw(screen):
            click_sfx.play()
            return   

        if pause_exit.draw(screen):
            click_sfx.play()
            main_menu()

        if pause_reset.draw(screen):
            click_sfx.play()
            game_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    runpauseUI = False
                if event.key == pygame.K_ESCAPE:
                    runpauseUI = False

        if active_button:
            active_button.draw(screen)

        

        # Draw the shop background


        clock.tick(60)
        pygame.display.update()
    pass
             
    
def credit_menu():
    RunCredit = True
    while RunCredit :

        screen.fill((255, 255, 255))
        screen.blit(bg_credit_menu, (0, 0))

        if pause_button.draw(screen): 
            click_sfx.play()
            RunCredit = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RunCredit = False
        pygame.display.update()
            
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

main_menu()

pygame.quit()
