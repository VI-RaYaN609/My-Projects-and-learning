import pygame,sys,random
from pygame.locals  import *


grey =(25,25,25)
black =(0,0,0)
white =(255,255,255)
green =(0,255,0)
fps=30
width = 800
height = 600
velocity = 0
acceleration = 0
gravity = 1
x=100
y=500
player_jump=25
background_color= grey
#while True :
#    userinput = input("Do you want the program to run in dark mode ? Y/N :")
#    if userinput.lower() in ["y","n","yes","no",""]:
#       break
#    else :
#       print("Enter Y or N")
#
#if userinput.lower() in ["y","yes"]:
#   background_color = grey
#elif userinput.lower() in ["n","no"]:
#   background_color = white
#else :
#  background_color = grey

pygame.init()




#creating display

display = pygame.display.set_mode((width,height))

display.fill(background_color)

pygame.display.set_caption("Flappy Bird")

#loading images

player_image     = pygame.image.load("image.png")
item_image       = pygame.image.load("image.png")
background_image = pygame.image.load("image.png")

#Images rezising

player_image     =pygame.transform.scale(player_image,(50,50))
item_image       =pygame.transform.scale(item_image,(25,25))
background_image =pygame.transform.scale(background_image,(width,height))


while True :
    pygame.draw.rect(display,green,(x,y,50,50))
    y+=gravity
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if y <600:
                    y-=player_jump
    pygame.display.update()
    clock =pygame.time.Clock()
    clock.tick(fps)
               