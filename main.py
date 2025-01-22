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
    POKEMON_SPRITE = pygame.transform.scale(pygame.image.load("char1.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
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
