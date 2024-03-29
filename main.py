import random
import pygame
import clock
pygame.init()

black = (0,0,0)
color = (3, 252, 148)
red = (117, 0, 0)

dis_witch =600
dis_height = 600
display = pygame.display.set_mode((dis_witch,dis_height))
pygame.display.set_caption("THAT'S_A_SNAKE")
clock = pygame.time.Clock()
snake_block =10
snake_speed= 10
font_text = pygame.font.SysFont('Arial',26,bold=True)
score_font = pygame.font.SysFont('Arial',24,bold=True)
def Your_score(score):
    value = score_font.render("Your score "+ str(score), True,color)
    display.blit(value,[20,20])

def message(color, msg):
    mesg = font_text.render(msg,True,color)
    display.blit(mesg,[dis_witch/2 - 100,dis_height/2-100])
def game_loop():
    game_over = False
    game_close = False

    x1 = dis_witch/2
    y1 = dis_height/2
    x_change = 0
    y_change= 0
    snake_list = []
    snake_length = 1
    foodx = round(random.randint(0,dis_witch - snake_block) /10.0) * 10.0
    foody = round(random.randint(0,dis_height - snake_block)/10.0) * 10.0

    while not game_over:
        while game_close == True:
            display.fill(black)
            message(color, "GAME WAS INTERRUPTED")
            Your_score(snake_length -1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_over = True
                        game_close= False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    x_change= - snake_block
                    y_change = 0
                if event.key == pygame.K_a:
                        x_change = - snake_block
                        y_change = 0
                if event.key == pygame.K_s:
                        x_change =  snake_block
                        y_change = 0
                if event.key == pygame.K_d:
                        x_change = snake_block
                        y_change = 0
            if event.type == pygame.quit:
                    game_over = True
        if x1< 0 or x1 >= dis_witch or y1<0 or y1 >= dis_height:
                game_close= True

        x1+=x_change
        y1+=y_change
        display.fill(black)

        pygame.draw.rect(display, color, [foodx,foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        if len(snake_list) >snake_length:
            del snake_list[0]
        for x in snake_list:
                pygame.draw.rect(display, color, [foodx,foody, snake_block, snake_block])

        Your_score(snake_length -1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,dis_witch-snake_block)/10.0)*10.0
            foody = round(random.randrange(0, dis_witch - snake_block) / 10.0) * 10.0
            snake_length +=1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
game_loop()