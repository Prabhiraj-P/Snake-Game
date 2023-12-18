import pygame
import random

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((700, 520))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 36)

def rand_vect():
    return (pygame.Vector2(random.choice(range(screen.get_width())), random.choice(range(screen.get_height()))))

x = screen.get_width()
r2l = True

def game(running, r2l, x):
    speed=5
    x = screen.get_width() // 2
    y = screen.get_height() // 2
    while running:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False

        # Fill the screen with a color to wipe away anything from the last frame
         screen.fill("purple")



        #ve = pygame.Vector2(x, screen.get_height() // 2)
        #circle_pos=rand_vect()
         keys = pygame.key.get_pressed()

    # Check for specific keys
         if keys[pygame.K_LEFT]:
            x -= speed
         if keys[pygame.K_RIGHT]:
            x += speed
         if keys[pygame.K_UP]:
            y -= speed
         if keys[pygame.K_DOWN]:
            y += speed
        
        pygame.draw.circle(screen, "red", (x,y) , 10)

        pygame.time.delay(10)  # Adjust the delay for a smoother animation
    

      # Flip the display to put your work on the screen
        pygame.display.flip()

    # Control the frame rate
        clock.tick(60)

    pygame.quit()

game(running, r2l, x)
