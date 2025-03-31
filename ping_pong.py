import pygame
import sys

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SPEED = 5
PADDLE_SPEED = 20
COMPUTER_PADDLE_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
DARK_BLUE = (0, 0, 139)
DARK_GREEN = (0, 100, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Ball and Paddles
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
paddle1 = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball_speed_x, ball_speed_y = BALL_SPEED, BALL_SPEED
paddle1_speed, paddle2_speed = 0, COMPUTER_PADDLE_SPEED
score1, score2 = 0, 0

# Font settings
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Game loop
def game_loop():
    global ball_speed_x, ball_speed_y, paddle1_speed, paddle2_speed, score1, score2

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle1_speed = -PADDLE_SPEED
                elif event.key == pygame.K_s:
                    paddle1_speed = PADDLE_SPEED
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle1_speed = 0

        paddle1.y += paddle1_speed

        # Computer paddle logic
        if paddle2.centery < ball.centery:
            paddle2.y += COMPUTER_PADDLE_SPEED
        elif paddle2.centery > ball.centery:
            paddle2.y -= COMPUTER_PADDLE_SPEED

        if paddle1.top < 0:
            paddle1.top = 0
        if paddle1.bottom > HEIGHT:
            paddle1.bottom = HEIGHT
        if paddle2.top < 0:
            paddle2.top = 0
        if paddle2.bottom > HEIGHT:
            paddle2.bottom = HEIGHT

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y = -ball_speed_y
        if ball.left <= 0:
            score2 += 1
            ball.x = WIDTH // 2 - BALL_SIZE // 2
            ball.y = HEIGHT // 2 - BALL_SIZE // 2
            ball_speed_x = -ball_speed_x
        if ball.right >= WIDTH:
            score1 += 1
            ball.x = WIDTH // 2 - BALL_SIZE // 2
            ball.y = HEIGHT // 2 - BALL_SIZE // 2
            ball_speed_x = -ball_speed_x

        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed_x = -ball_speed_x

        screen.fill(BLACK)
        pygame.draw.rect(screen, DARK_BLUE, paddle1)
        pygame.draw.rect(screen, DARK_GREEN, paddle2)
        pygame.draw.ellipse(screen, RED, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        text1 = font.render(str(score1), True, WHITE)
        screen.blit(text1, (WIDTH // 4, 50))
        text2 = font.render(str(score2), True, WHITE)
        screen.blit(text2, (WIDTH * 3 // 4, 50))

        pygame.display.flip()
        clock.tick(60)

def show_start_screen():
    screen.fill(BLACK)
    title = font.render("Ping Pong Game", True, WHITE)
    instruction = small_font.render("Press any key to start", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    wait_for_key()

def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

if __name__ == "__main__":
    show_start_screen()
    game_loop()