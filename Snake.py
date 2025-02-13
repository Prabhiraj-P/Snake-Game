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
    return pygame.Vector2(random.choice(range(wall_thick+20, screen.get_width()-wall_thick-20)), random.choice(range(wall_thick+20, screen.get_height() - wall_thick-20)))


def tail(x,y, direction):
    global snake_tail_list
    if direction =='-x':
            x=x
    elif direction =='+x':
         x=x
    elif direction =='-y':
        y=y
    else:
        y=y
    if len(snake_tail_list)>0:
        snake_tail_list.insert(0,(x,y))
        snake_tail_list=snake_tail_list[:-1]
        for i  in range(len(snake_tail_list)):
            tail_x, tail_y =snake_tail_list[i]
            if i%2==0:
                pygame.draw.circle(screen,'green', (tail_x,tail_y), 5)
            else:
                pygame.draw.circle(screen,'yellow', (tail_x,tail_y), 5)
    else:
        snake_tail_list.insert(0,(x+10,y))


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
    speed = 1
    num=0
    score=str(0)
    x = screen.get_width() // 2
    y = screen.get_height() // 2
    food_pos = rand_vect()
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
            # print(snake_tail_list)
            score=str( int(score)+1)
            food_pos = rand_vect()
            
        screen.fill("purple")
        tail(x , y, direction)
        #print(snake_tail_list)    
       
        x,y = get_direction(x,y,direction,speed)

        #snake(x,y)
        border(screen, pygame)
        game_over(x,y) #chek if its game over
        if num %50!=0:
            pygame.draw.circle(screen, "red", (food_pos.x, food_pos.y), 6)
        else:
             pygame.draw.circle(screen, "purple", (food_pos.x, food_pos.y), 6)
        num+=1
        text_surface=font.render(score, True, (255, 255, 255))
        text_rect=text_surface.get_rect(center=(screen.get_width() // 20, 50))
        screen.blit(text_surface, text_rect)
        
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()
    sys.exit()

game()
