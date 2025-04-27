import pygame
import sys
from pygame.locals import *
from PIL import Image



pygame.init()

screen = pygame.display.set_mode((450, 500))
pygame.display.set_caption("Frog Lands")



pygame.display.set_icon = pygame.image.load('download.jpeg')
fps = pygame.time.Clock()

font = pygame.font.Font('Pixeltype.ttf', 50)

 

b_o = pygame.Surface((450, 100))
b_o.fill('#6F826A')

k_o = font.render("score: 0", False, "#F0F1C5", None)

house_surface = pygame.image.load('Sprout Lands - Sprites - Basic pack\Sprout Lands - Sprites - Basic pack\Objects\Free_Chicken_House.png').convert_alpha()

house_x_poisition = 0
house_y_poisition = 250


moving_right = False
moving_left = False

player = pygame.image.load('Pixel Adventure 1\Free\Main Characters\Pink Man\Fall (32x32).png').convert_alpha()
player_Rect = player.get_rect(topleft = (80, 465))

enemy1 = pygame.image.load(r'C:\Users\HP USER\OneDrive\Desktop\pygamuuu\Ghostpixxells_pixelfood\29_cookies_dish.png').convert_alpha()
enemy1_rect = enemy1.get_rect(bottomright = (80, 140))


while True:

    


    screen.fill("#E1EEBC")
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                print("moving right")
                moving_right = True
            if event.key == K_LEFT:
                print("moving left")
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    screen.blit(b_o, (0, 0))
    screen.blit(k_o, (160, 17))
    house_x_poisition +=1
    if house_x_poisition > 480: house_x_poisition = 0
    screen.blit(house_surface, (house_x_poisition, 250))
    
# 2 big pepper
#4 rodo
#two big tomatoes
#1 white onion with garlic

    if player_Rect.right > 500: player_Rect.right = 0

    player_Rect.right +=1
    screen.blit(player, player_Rect)

    screen.blit(enemy1, enemy1_rect)


    pygame.display.update()
    fps.tick(60)