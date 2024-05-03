import pygame
import sys
from button import Button



# initialize pygame
pygame.init()
class mainmenu ():
    def __init__(self):
        self.run = True
        #self.button = Button()
        # create display window
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.gamecanvas = pygame.Surface((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        pygame.display.set_caption('Restaurant Owner!')

        # load images
        self.bg_main_menu = pygame.image.load('gameasset/backgroundmainmenu.png')
        self.bg_game_screen = pygame.image.load('gameasset/background.png')
        self.title_img = pygame.image.load('gameasset/gametitle.png').convert_alpha()
        self.start_img = pygame.image.load('gameasset/playbutton.png').convert_alpha()
        self.credit_img = pygame.image.load('gameasset/creditbutton.png').convert_alpha()
        self.exit_img = pygame.image.load('gameasset/quitbutton.png').convert_alpha()

        # create button instances
        self.title_button = Button(300, 100, self.title_img, 0.5)
        self.start_button = Button(515, 350, self.start_img, 0.5)
        self.credit_button = Button(515, 450, self.credit_img, 0.5)
        self.exit_button = Button(515, 550, self.exit_img, 0.5)

    def render(self):
        while self.run == True:

            self.screen.blit((self.bg_main_menu))
            self.start_button.blit((515, 350, self.start_img, 0.5))
            self.credit_button.blit = Button((515, 450, self.credit_img, 0.5))
            self.exit_button.blit = Button((515, 550, self.exit_img, 0.5))

    def main_menu(self):
        while self.run:
            self.screen.fill((255, 235, 216))
            self.screen.blit(self.bg_main_menu, (0, 0))
            self.title_button.draw(self.screen)

            if self.button.clicked == True:
                self.start_button.rend
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    exit()
            pygame.display.update()

    def game_screen(self):
        run = True
        while run:
            self.map()
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.bg_surf, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.play = False
                    sys.exit()

    def map(self):

        self.bg_surf = pygame.image.load('gameasset/background.png').convert() 
        self.Rchair_surf = pygame.image.load('gameasset/Rchair.png').convert_alpha()
        self.Lchair_surf = pygame.image.load('gameasset/Lchair.png').convert_alpha()
        self.table_surf = pygame.image.load('gameasset/table.png').convert_alpha()
        self.casher_surf = pygame.image.load('gameasset/casher.png').convert_alpha()
        self.casher_surf = pygame.transform.flip(self. casher_surf, True, False)

        self.casherpos = (430, 20)

        self.TablePos = [
            (450, 450),
            (850, 450),
            (830, 300),
        ]

        self.RchairPos = [
            (393, 450),
            (788, 450),
            (770, 300),
        ]

        self.LchairPos = [
            (668, 450),
            (1070, 450),
            (1045, 300),
        ]

        for pos in self.RchairPos:
            self.bg_surf.blit(self.Rchair_surf, pos)
        
        for pos in self.LchairPos:
            self.bg_surf.blit(self.Lchair_surf, pos)

        for pos in self.TablePos:
            self.bg_surf.blit(self.table_surf, pos)  # Blit the table chair sprite onto the background surface

        self.bg_surf.blit(self.casher_surf, self.casherpos)

        # Create Rect objects for collision detection
        table_rects = [pygame.Rect(pos, self.table_surf.get_size()) for pos in self.TablePos]
        casher_rect = self.casher_surf.get_rect(topleft=self.casherpos)

        return self.bg_surf, casher_rect, table_rects

    # def credits_menu():
    # run = True
    # while run:
            # credits menu code here
        #   pass

    # call the main menu

if __name__ == "__main__":
    main = mainmenu()
    while main.run:
        main.main_menu()