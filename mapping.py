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

def handle_collisions(block_rect, table_rects, casher_rect):
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

# Main game loop
def game_loop():
    block_x = 100
    block_y = 300
    block_width = 30
    block_height = 30
    block_speed = 5

    # Get the background surface and rectangles from the map function
    bg_surf, casher_rect, table_rects = map()

    # Dictionary to track keys being pressed
    keys_pressed = {}

    run = True
    while run:
        screen.fill((255, 255, 255))

        # Draw the background surface
        screen.blit(bg_surf, (0, 0))

        # Draw the block
        pygame.draw.rect(screen, (0, 0, 0), (block_x, block_y, block_width, block_height))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                keys_pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                keys_pressed[event.key] = False

        # Update block position based on keys being pressed
        if keys_pressed.get(pygame.K_w):
            block_y -= block_speed
            if handle_collisions(pygame.Rect(block_x, block_y, block_width, block_height), table_rects, casher_rect):
                block_y += block_speed
        if keys_pressed.get(pygame.K_s):
            block_y += block_speed
            if handle_collisions(pygame.Rect(block_x, block_y, block_width, block_height), table_rects, casher_rect):
                block_y -= block_speed
        if keys_pressed.get(pygame.K_a):
            block_x -= block_speed
            if handle_collisions(pygame.Rect(block_x, block_y, block_width, block_height), table_rects, casher_rect):
                block_x += block_speed
        if keys_pressed.get(pygame.K_d):
            block_x += block_speed
            if handle_collisions(pygame.Rect(block_x, block_y, block_width, block_height), table_rects, casher_rect):
                block_x -= block_speed

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Call the game loop
game_loop()
