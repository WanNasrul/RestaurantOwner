import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# map setup
def map():
    bg_surf = pygame.image.load('gameasset/background.png').convert() 
    Rchair_surf = pygame.image.load('gameasset/Rchair.png').convert_alpha()
    Lchair_surf = pygame.image.load('gameasset/Lchair.png').convert_alpha()
    table_surf = pygame.image.load('gameasset/table.png').convert_alpha()
    casher_surf = pygame.image.load('gameasset/casher.png').convert_alpha()
    casher_surf = pygame.transform.flip(casher_surf, True, False)

    casherpos = (430, 20)

    TablePos = [
        (450, 450),
        (850, 450),
        (830, 300),
    ]

    RchairPos = [
        (393, 450),
        (788, 450),
        (770, 300),
    ]

    LchairPos = [
        (668, 450),
        (1070, 450),
        (1045, 300),
    ]

    for pos in RchairPos:
        bg_surf.blit(Rchair_surf, pos)
    
    for pos in LchairPos:
        bg_surf.blit(Lchair_surf, pos)

    for pos in TablePos:
        bg_surf.blit(table_surf, pos)  # Blit the table chair sprite onto the background surface

    bg_surf.blit(casher_surf, casherpos)

    # Create Rect objects for collision detection
    table_rects = [pygame.Rect(pos, table_surf.get_size()) for pos in TablePos]
    casher_rect = casher_surf.get_rect(topleft=casherpos)

    return bg_surf, casher_rect, table_rects

def collisions(block_rect, table_rects, casher_rect):
    for table_rect in table_rects:
        if block_rect.colliderect(table_rect):
            print("Block collided with a table!")
            if block_rect.left < table_rect.right and block_rect.right > table_rect.left:
                if block_rect.top < table_rect.bottom and block_rect.bottom > table_rect.top:
                    return True
    if block_rect.colliderect(casher_rect):
        print("Collide with casher!")
        if block_rect.left < casher_rect.right and block_rect.right > casher_rect.left:
            if block_rect.top < casher_rect.bottom and block_rect.bottom > casher_rect.top:
                return True
    return False