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
bg_game_screen = pygame.image.load('gameasset/background.png').convert_alpha()
bg_credit_menu = pygame.image.load('gameasset/credit.png').convert_alpha()
title_img = pygame.image.load('gameasset/gametitle.png').convert_alpha()
shoppic_img = pygame.image.load('gameasset/shop.jpg').convert_alpha()
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
npc1_img = pygame.image.load('gameasset/casher.png').convert_alpha()
tablechair1_img = pygame.image.load('gameasset/tablechair.png').convert_alpha()
tablechair2_img = pygame.image.load('gameasset/tablechair.png').convert_alpha()
tablechair3_img = pygame.image.load('gameasset/tablechair.png').convert_alpha()

# Rchair1_img = pygame.image.load('gameasset/Rchair.png').convert_alpha()
# Lchair1_img = pygame.image.load('gameasset/Lchair.png').convert_alpha()
# table_img = pygame.image.load('gameasset/table.png').convert_alpha()

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

# decoration ui images
decorationbutton_img = pygame.image.load('gameasset/decoration ui/decorationbutton.png').convert_alpha()
decorationuibackground_img = pygame.image.load('gameasset/decoration ui/decorationuibackground.png').convert_alpha()
buymenu_img = pygame.image.load('gameasset/decoration ui/decorationbuybutton.png').convert_alpha()
buypiano_img = pygame.image.load('gameasset/decoration ui/decorationbuybutton.png').convert_alpha()
menudecorationui_img = pygame.image.load('gameasset/decoration ui/menudecorationui.png').convert_alpha()
pianoui_img = pygame.image.load('gameasset/decoration ui/pianoui.png').convert_alpha()
menudecoration_img = pygame.image.load('gameasset/decoration ui/menudecoration.png').convert_alpha()
piano_img = pygame.image.load('gameasset/decoration ui/piano.png').convert_alpha()

# decoration ui buttons
decorationbutton_button = button.Button(600, 600, decorationbutton_img, 1)
buymenu_button = button.Button(475, 400, buymenu_img, 1)
buypiano_button = button.Button(680, 400, buypiano_img, 1)


#shop img
cheficon_img =  pygame.image.load('gameasset\ShopUI\ShopUI\cheficon.png').convert_alpha()
chefborder_img = pygame.image.load('gameasset\ShopUI\ShopUI\shopcolumn.png').convert_alpha()
star_img = pygame.image.load('gameasset\ShopUI\ShopUI\star.png').convert_alpha()
upgradebutton_img = pygame.image.load('gameasset/ShopUI/ShopUI/upgrade.png').convert_alpha()
starupgrade_img = pygame.image.load('gameasset\ShopUI\ShopUI\starupgraded.png').convert_alpha()
shopbackground_img = pygame.image.load('gameasset\ShopUI\ShopUI\shopbackground.png').convert_alpha()


# shop ui buttons 
xshopbutton_button = button.Button(1100, 30, xbutton_img, 1)
upgrade_button1 = button.Button(1050, 150, upgradebutton_img, 1)
upgrade_button2 = button.Button(1050,315, upgradebutton_img,1)
upgrade_button3 = button.Button(1050,475, upgradebutton_img,1)


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

def waiter(x, y, WaiterDirection):
    waiter_width = int(waiter_img.get_width() * 1)
    waiter_height = int(waiter_img.get_height() * 1)
    waiter_resize = pygame.transform.scale(waiter_img, (waiter_width, waiter_height))
    waiter_flip = pygame.transform.flip(waiter_resize, True, False)
    if WaiterDirection == 'right':
        screen.blit(waiter_resize, (x, y))
    if WaiterDirection == 'left':
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


def collision_detection(waiter_rect, table_rect):

    # print("waiter_rect:", waiter_rect)
    # print("table_rect:", table_rect)
    # print("Collision:", waiter_rect.colliderect(table_rect))


    # Check if two rectangles collide while taking into account the waiter's position
    return waiter_rect.colliderect(table_rect)


#jdbcdvkdjvlkdjvjlv



def main_menu():
    
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
            game_screen()



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

def game_screen():

    global npc1_x_pos, npc1_img, npc1_y_pos, money
    run = True

    # default money and day value
    money = 0
    day = 1

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

    chef = star_img
    chef2 = star_img
    chef3 = star_img
    waiter1 = star_img

    cooking_speed_multiplier = 1
    
   
    waiter_speed = 3


    runShopUI = False

    


    runchefUI = False
    rundecorationUI = False
    cooking = emptybox_img
    progress = 0
    FoodOnTable = emptybox_img
    waiterfood = emptybox_img
    CustomerFood = emptybox_img

    #decoration
    purchasedmenu = False
    purchasedpiano = False

    # rect object for waiter
    waiter_rect = pygame.Rect(waiterX, waiterY, waiter_img.get_width(), waiter_img.get_height())
    # rect object for table and chair
    tablechair1_rect = pygame.Rect(tablechair1X, tablechair1Y, 252, 80)
    tablechair2_rect = pygame.Rect(tablechair2X, tablechair2Y, 252, 80)
    tablechair3_rect = pygame.Rect(tablechair3X, tablechair3Y, 252, 80)

    # food rect and surf
    foodtrigger_surf = pygame.image.load('gameasset/chef ui/emptybox.png').convert_alpha()
    foodtrigger_scaled = pygame.transform.scale(foodtrigger_surf, (foodtrigger_surf.get_width() // 2, foodtrigger_surf.get_height() // 2))
    foodtrigger_scaled.set_alpha(0)
    foodtrigger_rect = foodtrigger_scaled.get_rect(topleft = (550, 205))


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
        waiter_rect.topleft = (waiterX, waiterY)


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
            
            if CustomerFood == emptybox_img:
                CustomerFood = waiterfood
                waiterfood = emptybox_img
                cooking = emptybox_img


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
            print('game paused')
            # insert pause code here
            run = False


        

        # insert shop code here

        screen.blit(moneycounter_img, (30,530))
        screen.blit(daycounter_img, (380,615))
        screen.blit(daycycle_surf,daycycle_rect)
        screen.blit(money_surf,money_rect)
    
        # testing, add 12 money every 1 frame
        # money += 0
        

        table1(tablechair1X,tablechair1Y)

        table2(tablechair2X,tablechair2Y)

        table3(tablechair3X,tablechair3Y)

        customerplate1(customerplate1X,customerplate1Y, CustomerFood)

        npc(npc1_x_pos, npc1_y_pos)

        # Decoration bought items
        if purchasedmenu == True:
            screen.blit(menudecoration_img, (336,236))

        if purchasedpiano == True:
            screen.blit(piano_img, (680,15))


        #table4(tablechair4X,tablechair4Y)
        

        # Chef UI ====================================== #
        
        # chef progress bar
        progressbar_font = pygame.font.Font('font/segoepr.ttf', 15)
        progressbar_surf = progressbar_font.render('.'*progress, False, (64,64,64))
        progressbar_rect = progressbar_surf.get_rect(midleft = (615,535))

        if chef_button.draw(screen):
            click_sfx.play()
            runchefUI = True

        if decorationbutton_button.draw(screen):
            click_sfx.play()
            rundecorationUI = True
        # food serve (part 1) ================================ #
        screen.blit(foodtrigger_scaled, foodtrigger_rect,) # foodtrigger
        foodserve(foodserveX,foodserveY,FoodOnTable)
        waiter(waiterX, waiterY, WaiterDirection)
        screen.blit(waiterfood, (waiterX - 35,waiterY - 105))
        # food serve ================================ #

        

        if shop_button.draw(screen):
            click_sfx.play()
            runShopUI = True 

        if runShopUI == True:

            
            screen.blit(shopbackground_img, (410,25))
            screen.blit(chefborder_img, (435,125))
            screen.blit(cheficon_img, (450,135))
            screen.blit(chefborder_img, (435,285))
            screen.blit(cheficon_img, (450,295))
            screen.blit(chefborder_img, (435,445))
            screen.blit(cheficon_img, (450,455))
            screen.blit(chef, (610,155))
            #screen.blit(chef3, (810,155))
            screen.blit(chef2, (610,315))
            screen.blit(waiter1, (610,475))
            
            
            if xshopbutton_button.draw(screen) :
                click_sfx.play()
                runShopUI = False

            if upgrade_button1.draw(screen) and chef == star_img and money>= 100 :
                 click_sfx.play()
                 chef = starupgrade_img
                 money -= 100
                 cooking_speed_multiplier = 2


            if upgrade_button2.draw(screen) and chef2 == star_img and money>= 100:
                 click_sfx.play()
                 chef2 = starupgrade_img
                 money -= 100
                 waiter_speed = 6
                 
            if upgrade_button3.draw(screen) and waiter1 == star_img and money >= 100 :
                 click_sfx.play()
                 waiter1 = starupgrade_img
                 money -= 100

        if cooking!= emptybox_img and progress >= 130:
        # Award coins to the player when food is successfully served
            money += 100  # Adjust the amount of coins as needed
        # Optionally, limit the maximum amount of money
        if money > 10000:
            money = 10000  # Adjust the maximum money value as needed


        if cooking != emptybox_img:
                if progress <= 130:
                    progress += cooking_speed_multiplier
                    
                    
                else:
                    FoodOnTable = cooking
                    cooking = emptybox_img
                    progress = 0

            
            

 

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
                    progress += cooking_speed_multiplier
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

            if xbutton_button.draw(screen):
                click_sfx.play()
                rundecorationUI = False
            if buymenu_button.draw(screen) and money >= 100 and purchasedmenu == False:
                click_sfx.play()
                money -= 100
                purchasedmenu = True
                


            if buypiano_button.draw(screen) and money >= 200 and purchasedpiano == False:
                click_sfx.play()
                money -= 200
                purchasedpiano = True


            screen.blit(menudecorationui_img, (430,170))
            screen.blit(pianoui_img, (635,170))
            
        # CHECK MOUSE POSITION
        # mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)

        # Decoration UI ================================= #


        # food serve (part 2) ================================ #

        if foodtrigger_rect.colliderect(waiter_rect):
            if waiterfood == emptybox_img:
                waiterfood = FoodOnTable
                FoodOnTable = emptybox_img

        # food serve ================================ #

    # Define a function to handle the upgrade process



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # saveloadmanager.save_data() # <--- STOP HERE 7/5/24 
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)





    

def credit_menu():
    RunCredit = True
    while RunCredit :

        screen.fill((255, 255, 255))
        screen.blit(bg_credit_menu, (0, 0))

        if pause_button.draw(screen):
            click_sfx.play()
            print('game paused')
            # insert pause code here
            RunCredit = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RunCredit = False
        pygame.display.update()


# def credits_menu():
   # run = True
   # while run:
        # credits menu code here
     #   pass

# call the main menu
main_menu()

pygame.quit()