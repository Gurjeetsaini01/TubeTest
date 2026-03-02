import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Floating Letters")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Font
font = pygame.font.Font(None, 48)

class FloatingLetter:
    def __init__(self):
        self.letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.vx = random.uniform(-3, 3)  # Horizontal velocity
        self.vy = random.uniform(-3, 3)  # Vertical velocity
        self.color = random.choice(COLORS)
        self.size = random.randint(24, 72)
        self.font = pygame.font.Font(None, self.size)
    
    def update(self):
        # Move the letter
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off walls
        if self.x <= 0 or self.x >= SCREEN_WIDTH:
            self.vx = -self.vx
        if self.y <= 0 or self.y >= SCREEN_HEIGHT:
            self.vy = -self.vy
        
        # Keep within bounds
        self.x = max(0, min(self.x, SCREEN_WIDTH))
        self.y = max(0, min(self.y, SCREEN_HEIGHT))
    
    def draw(self, surface):
        text_surface = self.font.render(self.letter, True, self.color)
        surface.blit(text_surface, (self.x, self.y))

# Main game loop
letters = [FloatingLetter() for _ in range(10)]  # Create 10 floating letters

running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Add a new random letter
                letters.append(FloatingLetter())
            elif event.key == pygame.K_c:
                # Clear all letters
                letters.clear()
    
    # Update
    for letter in letters:
        letter.update()
    
    # Draw
    screen.fill(BLACK)
    for letter in letters:
        letter.draw(screen)
    
    pygame.display.flip()

pygame.quit()
sys.exit()