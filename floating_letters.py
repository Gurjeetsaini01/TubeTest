import os
os.environ["SDL_VIDEODRIVER"] = "dummy"  # Headless mode

import pygame
import random

# Initialize Pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]

class FloatingLetter:
    def __init__(self):
        self.letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.x = random.randint(0, SCREEN_WIDTH - 50)
        self.y = random.randint(0, SCREEN_HEIGHT - 50)
        self.color = random.choice(COLORS)
        self.size = random.randint(24, 72)
        self.font = pygame.font.Font(None, self.size)

    def draw(self, surface):
        text_surface = self.font.render(self.letter, True, self.color)
        surface.blit(text_surface, (self.x, self.y))

# Create letters
letters = [FloatingLetter() for _ in range(10)]

# Draw one frame
screen.fill(BLACK)
for letter in letters:
    letter.draw(screen)

# Save image
pygame.image.save(screen, "output.png")

print("Saved output.png successfully!")

pygame.quit()
