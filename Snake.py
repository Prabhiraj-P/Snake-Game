import pygame
import random
import sys

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((700, 520))
clock = pygame.time.Clock()

def rand_vect():
    return pygame.Vector2(random.choice(range(screen.get_width())), random.choice(range(screen.get_height())))


snak_pos=[(screen.get_width//2,screen.get_height//2), (screen.get_width//2,screen.get_height//2),(screen.get_width//2,screen.get_height//2)]

def snake(x,y):
   
    print(snak_pos)
    for num_ in range(len(snak_pos)-1):
        snak_pos[num_+1]=snak_pos[num_]
    snak_pos[0]=(x,9)
    for num_ in range(3):
        pygame.draw.circle(screen, "green", snak_pos[num_], 10)
    


def game():
    running = True
    speed = 5
    score=str(0)
    x = screen.get_width() // 2
    y = screen.get_height() // 2
    food_pos = rand_vect()
    snake_pos=[]
    font=pygame.font.Font(None, 36)
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
            score=str( int(score)+1)
            food_pos = rand_vect()

        screen.fill("purple")

        snake(x,y)
        pygame.draw.circle(screen, "red", (food_pos.x, food_pos.y), 10)
        
        text_surface=font.render(score, True, (255, 255, 255))
        text_rect=text_surface.get_rect(center=(screen.get_width() // 20, 50))
        screen.blit(text_surface, text_rect)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

game()
