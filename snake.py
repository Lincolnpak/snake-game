import pygame
from random import randrange

# Инициализация
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

GREEN = (0, 200, 64)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
x, y =  randrange(0, 700, 50), randrange(0, 700, 50)
apple = randrange(0, 700, 50), randrange(0, 700, 50)
dirs = {'W': True, 'S': True, 'A': True, 'D': True,}
snake = [(x, y)]
speed = 7
dx, dy = 0, 0
length = 1
score = 0
font_score = pygame.font.SysFont('Arial', 26, bold=True)

while True:
    screen.fill(BLACK)
    
    #drawing snake, apple
    [(pygame.draw.rect(screen, GREEN, (i, j, 50, 50))) for i, j in snake]
    pygame.draw.rect(screen, RED, (*apple, 50, 50))
    #show score
    render_score = font_score.render(f'Score: {score}', 1, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))
    #movement
    x += dx * 50
    y += dy * 50
    snake.append((x, y))
    snake = snake[-length:]
    #eating apple 
    if snake[-1] == apple:
        apple = randrange(0, 700, 50), randrange(0, 700, 50)
        length += 1
        speed += 1
        score += 1
    #game over
    if x < 0 or x > 700-50 or y < 0 or y > 700-50 or len(snake) != len(set(snake)):
        while True:
            render_end = font_score.render('GAME OVER', 1, pygame.Color('orange'))
            screen.blit(render_end, (300, 300))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    #control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True,}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True,}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False,}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True,}