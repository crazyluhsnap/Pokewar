import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Wars")

BG = pygame.transform.scale(pygame.image.load("forest.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VEL = 5
FONT = pygame.font.SysFont("comicsans", 30)
GAME_OVER_FONT = pygame.font.SysFont("comicsans", 50)
STAR_WIDTH = 25
STAR_HEIGHT = 30
STAR_VEL = 5

try:
    POKEMON_SPRITE = pygame.transform.scale(pygame.image.load("data:image/png;base64,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"), (PLAYER_WIDTH, PLAYER_HEIGHT))
    FALLING_SPRITE = pygame.transform.scale(pygame.image.load("drop.png"), (STAR_WIDTH, STAR_HEIGHT))
except pygame.error as e:
    print(f"Error loading sprite: {e}")
    pygame.quit()
    exit()

def draw(player_x, player_y, elapsed_time, stars, lost):
    WIN.blit(BG, (0, 0))
    if not lost:
        time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "black")
        WIN.blit(time_text, (10, 10))
        WIN.blit(POKEMON_SPRITE, (player_x, player_y))
        for star in stars:
            WIN.blit(FALLING_SPRITE, (star.x, star.y))
    else:
        lost_text = GAME_OVER_FONT.render("YOU LOST!!", 1, "red")
        WIN.blit(lost_text, (WIDTH // 2 - lost_text.get_width() // 2, HEIGHT // 2 - lost_text.get_height() // 2))
    pygame.display.update()

def main():
    run = True
    lost = False
    player_x = 200
    player_y = HEIGHT - PLAYER_HEIGHT
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0
    stars = []

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if not lost and star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    break
                if lost and event.key == pygame.K_r:
                    main()
                if lost and event.key == pygame.K_ESCAPE:
                    run = False
                    break

        keys = pygame.key.get_pressed()
        if not lost:
            if keys[pygame.K_LEFT] and player_x - PLAYER_VEL >= 0:
                player_x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player_x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
                player_x += PLAYER_VEL

        player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif not lost and star.colliderect(player_rect):
                lost = True
                break

        draw(player_x, player_y, elapsed_time, stars, lost)
    pygame.quit()

if __name__ == "__main__":
    main()
