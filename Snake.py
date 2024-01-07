import pygame
import random
import sys

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((700, 520))
clock = pygame.time.Clock()
# wall properties
width=screen.get_width()
height=screen.get_height()
wall_thick=20

#Tail properties
snake_tail_list=[]

def rand_vect():
    return pygame.Vector2(random.choice(range(wall_thick, screen.get_width()-wall_thick)), random.choice(range(wall_thick, screen.get_height() - wall_thick)))


def tail(x,y):
    if len(snake_tail_list)<1:
        snake_tail_list.append((x,y))
    for i  in range(len(snake_tail_list)):
        x=snake_tail_list[i][0]
        y=snake_tail_list[i][1]
        pygame.draw.circle(screen, (0, 255, 0), (x,y), 10)
    

def border(screen, pygame):
    pygame.draw.rect(screen, 'blue', (0, 0, wall_thick, height)) #border on left
    pygame.draw.rect(screen, 'green', (width-wall_thick, 0, wall_thick, height)) #border on right
    pygame.draw.rect(screen, 'red', (0, 0, width, 20)) #border at top
    pygame.draw.rect(screen,'yellow', (0, height-wall_thick, width, 20 ) ) #Bottom
 
def get_direction(x,y, direction, speed):
    if direction =='-x':
        return (x-speed,y)
    elif direction =='+x':
        return (x+speed,y)
    elif direction =='-y':
        return (x,y-speed)
    else:
        return (x,y+speed)


def game_over(x,y):
    if x <= wall_thick or x >= width-wall_thick or y>=height-wall_thick or y<= wall_thick:
        screen.fill("purple")
        font = pygame.font.Font(None, 36)
        text_surface = font.render("GAME OVER", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.delay(10000)  # Add a delay to display the "GAME OVER" message for a few seconds
        pygame.quit()
        sys.exit()


def game():
    running = True
    speed = 3
    score=str(0)
    x = screen.get_width() // 2
    y = screen.get_height() // 2
    food_pos = rand_vect()
    snake_pos=[]
    direction='-x'
    font=pygame.font.Font(None, 36)
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            direction='-x'
        if keys[pygame.K_RIGHT]:
            direction='+x'
        if keys[pygame.K_UP]:
            direction='-y'
        if keys[pygame.K_DOWN]:
            direction='+y'

        if pygame.Rect(x, y, 20, 20).colliderect(pygame.Rect(food_pos.x, food_pos.y, 10, 10)):
            snake_tail_list.insert(0,(x,y))
            print(snake_tail_list)
            score=str( int(score)+1)
            food_pos = rand_vect()


        screen.fill("purple")
        x,y=get_direction(x,y,direction,speed)

        #snake(x,y)
        border(screen, pygame)
        tail(x,y)
        game_over(x,y) #chek if its game over
        pygame.draw.circle(screen, "red", (food_pos.x, food_pos.y), 10)
        
        text_surface=font.render(score, True, (255, 255, 255))
        text_rect=text_surface.get_rect(center=(screen.get_width() // 20, 50))
        screen.blit(text_surface, text_rect)
        
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()
    sys.exit()

game()
