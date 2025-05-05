from pygame import *
import pygame
from pygame.locals import *
import sys

pygame.init()

clock = pygame.time.Clock()

font = pygame.font.Font("Pixeltype.ttf", 50)

screen = pygame.display.set_mode((500, 450))
pygame.display.set_caption("Thieves vs Chefs")

ground = pygame.Surface((500, 150))
ground.fill("#FFDCCC")

food1 = pygame.image.load(r"C:\Users\HP USER\OneDrive\Desktop\theif vs chefs\Ghostpixxells_pixelfood\07_bread.png").convert_alpha()

food2 = pygame.image.load(r"C:\Users\HP USER\OneDrive\Desktop\theif vs chefs\Ghostpixxells_pixelfood\05_apple_pie.png").convert_alpha()

food3 = pygame.image.load(r"C:\Users\HP USER\OneDrive\Desktop\theif vs chefs\Ghostpixxells_pixelfood\11_bun.png").convert_alpha()
food3_rect = food3.get_rect(midbottom = (350, 100))

player = pygame.image.load(r"C:\Users\HP USER\OneDrive\Desktop\theif vs chefs\Sprout Lands - Sprites - Basic pack\Sprout Lands - Sprites - Basic pack\Objects\Free_Chicken_House.png").convert_alpha()
player_rect = player.get_rect(midleft = (0, 340))

score = 0

text = font.render(f"Score: {score}", False, "#FFDCCC")

player_x_location = 0
player_y_location = 340

m_right = False
m_left = False

m_up = False
m_down = False


while True:

    screen.fill("#FBF3B9")

    if m_right == True:
        player_rect.right +=4

    if m_left ==True:
        player_rect.left -=4
    
    if m_up == True:
        player_rect.top -=4
    
    if m_down == True:
        player_rect.bottom +=4

    screen.blit(text, (200, 0))
    
    #since we struggle with coordinates think of it like this:
    # ((200, 0))
    #200 pixels rom the left(width)
    #0 pixels from the top(height)

    screen.blit(ground, (0, 350))

    screen.blit(food1, (450, 200))

    screen.blit(food2, (200, 150))

    screen.blit(food3, food3_rect)

    screen.blit(player, player_rect)

    if player_rect.colliderect(food3_rect):
        score +=1

    if player_rect.left > 450: player_rect.left = 450
    if player_rect.left < -2: player_rect.left = 0

    if player_rect.bottom > 380: player_rect.bottom = 380
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                m_up = True
            if event.key == K_DOWN:
                m_down = True
            if event.key == K_RIGHT:
                m_right = True
                #print("going riht")
            if event.key == K_LEFT:
                m_left = True
        
        if event.type == KEYUP:
            if event.key == K_UP:
                m_up = False
            if event.key == K_DOWN:
                m_down = False
            if event.key == K_RIGHT:
                m_right = False
                print("going riht")
            if event.key == K_LEFT:
                m_left = False

    clock.tick(60)

    display.update()

#1403
#workout
# 1) 13:48
