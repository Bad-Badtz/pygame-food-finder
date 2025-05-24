import pygame
from pygame import *
from pygame.locals import *
import sys


pygame.init()

font = pygame.font.Font("PixelAE-Bold.ttf", 50)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 450))

new_size = (500, 450)
image = pygame.image.load(r"C:\Users\oluwa\OneDrive\Desktop\chefvsthief\background.png")
background = pygame.transform.scale(image, new_size)

bench_size = (150,150)
bench = pygame.image.load("table.png")
table = pygame.transform.scale(bench, bench_size)
pygame.Surface.set_colorkey(table, (255,255,255))

flower_size = (150, 150)
flower = pygame.image.load("vase.png")
vase = pygame.transform.scale(flower, flower_size)
pygame.Surface.set_colorkey(vase, (255, 255, 255))

user_size = (100,100)
user = pygame.image.load("player.png")
player = pygame.transform.scale(user, user_size)

items_found = 0
text = font.render(f"{items_found}/5", False, "#FFDCCC")

player_x_pos = 0
player_y_pos = 350
#2035
move_right = False
move_left = False
jump = False 

while True:
    if move_right == True:
        player_x_pos +=4
    if move_left ==True:
        player_x_pos -=4
    if jump == True:
        player_y_pos -=4
       # player_y_pos +=2

    if player_y_pos < 350:
        player_y_pos +=2

    screen.fill("#4B352A")
    screen.blit(background, (0,0))
    screen.blit(table, (200, 200))
    screen.blit(vase, (2, 200))
    screen.blit(player, (player_x_pos,player_y_pos))

    screen.blit(text, (200,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                move_right = True
            if event.key == K_LEFT:
                move_left = True
            if event.key == K_SPACE:
                jump = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                move_right = False
            if event.key == K_LEFT:
                move_left = False
            if event.key == K_SPACE:
                jump = False
        
    clock.tick(60)
    pygame.display.update()