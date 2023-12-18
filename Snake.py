import pygame
import random
import sys

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((700, 520))
clock = pygame.time.Clock()

def rand_vect():
    return pygame.Vector2(random.choice(range(screen.get_width())), random.choice(range(screen.get_height())))

def game():
    running = True
    speed = 5
    x = screen.get_width() // 2
    y = screen.get_height() // 2
    food_pos = rand_vect()
    snake_pos=[]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed

        if pygame.Rect(x, y, 20, 20).colliderect(pygame.Rect(food_pos.x, food_pos.y, 10, 10)):
            food_pos = rand_vect()

        screen.fill("purple")
        pygame.draw.circle(screen, "green", (x, y), 10)
        pygame.draw.circle(screen, "red", (food_pos.x, food_pos.y), 10)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

game()
