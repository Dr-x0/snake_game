import pygame
import random

# إعدادات اللعبة
pygame.init()
black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
white = (255, 255, 255)

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

snake_block = 20
clock = pygame.time.Clock()

# رسم الثعبان باستخدام دوائر
def draw_snake(snake):
    for segment in snake:
        pygame.draw.circle(screen, green, (segment[0] + snake_block // 2, segment[1] + snake_block // 2), snake_block // 2)

# إعداد اللعبة
def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake = []
    length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            screen.fill(blue)
            font = pygame.font.SysFont("bahnschrift", 25)
            mesg = font.render("You Lost! Press C-Play Again or Q-Quit", True, red)
            screen.blit(mesg, [screen_width / 6, screen_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        pygame.draw.rect(screen, white, [foodx, foody, snake_block, snake_block])
        draw_snake(snake)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(15)

    pygame.quit()
    quit()

gameLoop()
