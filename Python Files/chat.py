import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 30
GRAVITY = 1
BIRD_SPEED = 5
JUMP_HEIGHT = -10
PIPE_WIDTH = 50
PIPE_HEIGHT = 300
GAP = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_image = pygame.image.load("bird.png")
background_image = pygame.image.load("background.png")
pipe_image = pygame.image.load("pipe.jpg")

# Resize images
bird_image = pygame.transform.scale(bird_image, (50, 50))
pipe_image = pygame.transform.scale(pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
background_image = pygame.transform.scale(background_image, (WIDTH,HEIGHT))

# Bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bird_image
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.velocity = 0

    def jump(self):
        self.velocity = JUMP_HEIGHT

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

# Pipe class
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pipe_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.height = random.randint(100, HEIGHT - GAP - 100)
        self.rect.y = 0

    def update(self):
        self.rect.x -= BIRD_SPEED

# Create sprite groups
all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()

# Create bird
bird = Bird()
all_sprites.add(bird)

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Create pipes
    if random.randint(1, 100) < 5:
        pipe = Pipe(WIDTH)
        pipes.add(pipe)
        all_sprites.add(pipe)

    # Update sprites
    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(bird, pipes, False)
    if hits:
        running = False

    # Remove off-screen pipes
    for pipe in pipes.copy():
        if pipe.rect.right < 0:
            pipes.remove(pipe)
            all_sprites.remove(pipe)

    # Draw background
    screen.blit(background_image, (0, 0))

    # Draw sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
