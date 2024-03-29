import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 40
ENEMY_SIZE = 50
FPS = 75

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Enemies")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 50)

# Function to display text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

# Function to draw the player
def draw_player(player):
    pygame.draw.rect(screen, WHITE, player)

# Function to draw enemies
def draw_enemies(enemies):
    for enemy in enemies:
        pygame.draw.rect(screen, enemy.color, enemy.rect)

# Function to generate enemies
def generate_enemy():
    x = random.randint(0, WIDTH - ENEMY_SIZE)
    y = -ENEMY_SIZE
    return pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)

# Class for different enemy shapes
class Enemy:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.x_speed = 0
        self.y_speed = 5  # Initial speed

    def move(self):
        self.rect.move_ip(self.x_speed, self.y_speed)

# Function to create different enemy shapes
def create_enemies():
    enemies = []
    for _ in range(3):  # You can adjust the number of different shapes
        x = random.randint(0, WIDTH - ENEMY_SIZE)
        y = -ENEMY_SIZE
        size = ENEMY_SIZE
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        enemies.append(Enemy(x, y, size, color))
    return enemies

# Function to get the player's name using Pygame's input box
def get_player_name():
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                    text = ''  # Clear the text box when clicked
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((0, 0, 0))
        draw_player(player)
        draw_enemies(enemies)

        draw_text("Enter your name:", font, WHITE, WIDTH // 2, HEIGHT // 2)

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(FPS)

# Function to get player's choice for play again using Pygame's input box
def get_play_again_choice():
    play_again_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 100, 300, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_box.collidepoint(event.pos):
                    active = not active
                    text = ''  # Clear the text box when clicked
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text.lower() == 'y':
                            return True
                        elif text.lower() == 'n':
                            return False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((0, 0, 0))
        draw_player(player)
        draw_enemies(enemies)
        draw_text("Game Over!!", title_font, RED, WIDTH // 2, HEIGHT // 2 - 100)
        draw_text(f"Your final score: {score}", font, WHITE, WIDTH // 2, HEIGHT // 2 - 50)

        txt_surface = font.render("Play again? (Y/N): " + text, True, color)
        width = max(300, txt_surface.get_width() + 10)
        play_again_box.w = width
        screen.blit(txt_surface, (play_again_box.x + 5, play_again_box.y + 5))
        pygame.draw.rect(screen, color, play_again_box, 2)

        pygame.display.flip()
        clock.tick(FPS)
        
# Function to display messages on the screen
def display_message(message, color, y_offset):
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH // 2, HEIGHT // 2 + y_offset)
    screen.blit(text_surface, text_rect)

# Function to display high scores in the game window
def display_high_scores():
    screen.fill((0, 0, 0))
    draw_text("HIGH SCORES:", title_font, RED, WIDTH // 2, 50)

    y_position = 100
    for name, hs in high_scores:
        draw_text(f"{name}: {hs}", font, WHITE, WIDTH // 2, y_position)
        y_position += 36

    pygame.display.flip()
    pygame.time.delay(5000)  # Display high scores for 5 seconds

# Function to reset game variables
def reset_game():
    global player, enemies, score, enemy_speed
    player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE - 10, PLAYER_SIZE, PLAYER_SIZE)
    enemies = create_enemies()
    score = 0
    enemy_speed = 5  # Initial speed

# Initialize game variables
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE - 10, PLAYER_SIZE, PLAYER_SIZE)
enemies = create_enemies()
score = 0
high_scores = []
enemy_speed = 5  # Initial speed
player_name = get_player_name()

# Load high scores from file
try:
    with open("highscores.txt", "r") as file:
        for line in file:
            name, score_str = line.strip().split(":")
            high_scores.append((name, int(score_str)))
except FileNotFoundError:
    pass


# Display the player's name at the beginning
draw_text(f"Player: {player_name}", font, WHITE, 10, 10)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(5, 0)

    # Generate enemies
    if random.random() < 0.03:
        enemies.extend(create_enemies())

    # Move enemies with updated speed
    for enemy in enemies:
        enemy.move()

    # Check for collisions
    for enemy in enemies:
        if player.colliderect(enemy.rect):
            print("Game Over!")
            draw_text("Game Over!!", title_font, RED, WIDTH // 2, HEIGHT // 2 - 100)
            draw_text(f"Your final score is: {score}", font, WHITE, WIDTH // 2, HEIGHT // 2 - 50)
            # Update high score
            if score > 0:
                # player_name = get_player_name()

                # Check if the name already exists in high scores
                while any(name == player_name for name, _ in high_scores):
                    display_message("Name already exists. Please choose a different name...", RED, 100)
                    pygame.display.flip()
                    pygame.time.delay(2000)  # Display the message for 2 seconds
                    player_name = get_player_name()

                high_scores.append((player_name, score))
                high_scores.sort(key=lambda x: x[1], reverse=True)

                # Ensure maximum of 12 entries
                if len(high_scores) > 12:
                    high_scores.pop()

                with open("highscores.txt", "w") as file:
                    for name, hs in high_scores:
                        file.write(f"{name}: {hs}\n")

            # Display high scores
            display_high_scores()

            # Ask if the player wants to play again
            play_again_choice = get_play_again_choice()
            if play_again_choice:
                reset_game()
            else:
                pygame.quit()
                sys.exit()


    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw player and enemies
    draw_player(player)
    draw_enemies(enemies)

    # Update the score
    score += 1
    
    # Display the player's name
    player_text = font.render(f"{player_name}", True, WHITE)
    screen.blit(player_text, (10, 10))

  # Display the score at the top-right corner
    score_text = font.render(f"Score: {score}", True, RED)
    score_rect = score_text.get_rect()
    score_rect.topright = (WIDTH - 20, 20)
    screen.blit(score_text, score_rect)

    # Increase enemy speed based on score
    if score % 100 == 0:  # Increase speed every 100 points
        for enemy in enemies:
            enemy.y_speed += 1

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)