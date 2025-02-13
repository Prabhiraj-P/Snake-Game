import pygame
import random
import sys


# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((1000, 620))
clock = pygame.time.Clock()
width = screen.get_width()
height = screen.get_height()

snake = []

# random position
def rand_pos():
    return random.choice(range(20, 680)), random.choice(range(20, 500))

# border
def draw_border(screen, pygame):
    colors = ['blue', 'green', 'red', 'yellow']
    pygame.draw.rect(screen,'yellow' , (0, 0, 10, height))  # border on left
    pygame.draw.rect(screen, 'yellow', (width - 10, 0, 10, height))  # border on right
    pygame.draw.rect(screen, 'yellow', (0, 0, width, 10))  # border at top
    pygame.draw.rect(screen, 'yellow', (0, height - 10, width, 10))  # Bottom

# snake grow
def snake_tail(snake):
    for i in range(len(snake)):
        if i == 0:
            pygame.draw.circle(screen, 'red', snake[i], 12)
        else:
            pygame.draw.circle(screen, 'green', snake[i], 8)



def snake_direction(direction, snake):

    x = snake[0][0]
    y =snake[0][1]

    if direction =='-x':
        x = x-1
            
    if direction =='+x':
        x = x+1
            
    if direction =='-y':
        y = y-1

    if direction =='+y':
        y = y +1
    
    return (x,y)
            



#game over 
def game_over(snake):
    x= snake[0][0]
    y=  snake[0][1]
    if x <= 10 or x >= width-10 or y>=height- 10 or y<=10 or (x,y) in snake[1:]:
        screen.fill("purple")
        font = pygame.font.Font(None, 36)
        text_surface = font.render("GAME OVER", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.delay(10000)  # Add a delay to display the "GAME OVER" message for a few seconds
        pygame.quit()
        sys.exit()



def game(snake):
    running = True
    snake.append(rand_pos())
    print(snake)
    score = 0
    food_pos = rand_pos()
    
    direction='-x'
    while running:
        screen.fill('black')
        snake_tail(snake)
        draw_border(screen, pygame)
        pygame.draw.circle(screen, random.choice(['yellow','black']), food_pos, random.choice(range(10, 20)))
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            direction='-x'
        if keys[pygame.K_RIGHT]:
            direction='+x'
        if keys[pygame.K_UP]:
            direction='-y'
        if keys[pygame.K_DOWN]:
            direction='+y'
        
        
        if pygame.Rect(snake[0][0], snake[0][1], 20, 20).colliderect(pygame.Rect(food_pos[0], food_pos[1], 10, 10)):

            if direction    =='-x':
                snake.insert(0,(snake[-1][0]-200,snake[-1][1]))
            if direction    =='+x':
                snake.insert(0,(snake[-1][0]+200,snake[-1][1]))
            if direction    =='-y':     
                snake.insert(0,(snake[-1][0],snake[-1][1]-200))
            if direction    =='+y':
                snake.insert(0,(snake[-1][0],snake[-1][1]+200))

            # snake.insert(0,(snake[0][0],snake[0][1]))
            # print(snake_tail_list)
            score=str( int(score)+1)
            food_pos = rand_pos()

        game_over(snake)
        new_cor = snake_direction(direction,  snake)
        snake.insert(0,new_cor)
        if len(snake)>1:
         snake = snake[:-1]
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(50)
        
    pygame.display.flip()


game(snake)