import pygame
import sys
from datetime import datetime

# Hello this is a test

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the display surface
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Real Time and Date Display")

# Font settings
font = pygame.font.Font(None, 36)

def display_real_time_and_date():
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    time_text = font.render("Time: " + current_time, True, WHITE)
    date_text = font.render("Date: " + current_date, True, WHITE)

    # Get the text surface and rect
    time_text_rect = time_text.get_rect(midtop=(WINDOW_WIDTH // 2, 50))
    date_text_rect = date_text.get_rect(midtop=(WINDOW_WIDTH // 2, 100))

    # Blit the text onto the screen
    screen.blit(time_text, time_text_rect)
    screen.blit(date_text, date_text_rect)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill(BLACK)

    # Display real-time and date
    display_real_time_and_date()

    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
