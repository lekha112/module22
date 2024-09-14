import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Text Display")

# Fonts
font1 = pygame.font.SysFont('Arial', 48)
font2 = pygame.font.SysFont('Comic Sans MS', 36)
font3 = pygame.font.SysFont('Courier', 32)

# Text to display
text1 = font1.render("Hello, Pygame!", True, BLACK)
text2 = font2.render("Welcome to Pygame!", True, BLACK)
text3 = font3.render("Enjoy Coding!", True, BLACK)

# Function to display the text
def display_text():
    screen.fill(WHITE)  # Fill the screen with white background
    # Blit text on the screen
    screen.blit(text1, (100, 100))
    screen.blit(text2, (100, 200))
    screen.blit(text3, (100, 300))
    pygame.display.update()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Display the text
    display_text()
