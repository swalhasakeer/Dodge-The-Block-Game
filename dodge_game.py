import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🧍 Dodge the Blocks")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 7

# Enemy settings
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = 0
enemy_speed = 5

# Clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
score = 0

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Move enemy
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = 0
        enemy_x = random.randint(0, WIDTH - enemy_size)
        score += 1  # Player dodged successfully

    # Collision detection
    if (
        enemy_x < player_x + player_size and
        enemy_x + enemy_size > player_x and
        enemy_y < player_y + player_size and
        enemy_y + enemy_size > player_y
    ):
        print("💥 Game Over!")
        running = False

    # Draw player and enemy
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_size, enemy_size))

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update screen and tick clock
    pygame.display.update()
    clock.tick(30)

pygame.quit()
