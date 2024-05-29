import pygame

#'self' is like a temporary name that can be used for any file


#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        #starts with each button not clicked
        self.clicked = False

    def draw(self, surface):    
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked condition
        #is the mouse cursor oclliding with the rectangle of the button
        if self.rect.collidepoint(pos):
        #     if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        #         self.clicked = True 
        #         action = True
        # if pygame.mouse.get_pressed()[0] == 0:
        #     self.clicked = False

            for event in pygame.event.get():    
                if event.type == pygame.MOUSEBUTTONUP and self.clicked == False:
                    self.clicked = True
                    action = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.clicked = False


        #draw button on screen
        surface.blit(self.image, (self.rect.x, self. rect.y))

        return action