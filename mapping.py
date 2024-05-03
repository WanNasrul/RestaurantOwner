import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# map setup

    

def collisions(block_rect, table_rects, casher_rects):
    for table_rect in table_rects:
        if block_rect.colliderect(table_rect):
            print("Block collided with a table!")
            if block_rect.left < table_rect.right and block_rect.right > table_rect.left:
                if block_rect.top < table_rect.bottom and block_rect.bottom > table_rect.top:
                    return True
    if block_rect.colliderect(casher_rects):
        print("Collide with casher!")
        if block_rect.left < casher_rects.right and block_rect.right > casher_rects.left:
            if block_rect.top < casher_rects.bottom and block_rect.bottom > casher_rects.top:
                return True
    return False

