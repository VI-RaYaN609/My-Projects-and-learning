import pygame ,sys

WIDTH=1000
HEIGHT=800
FPS= 60
GRAVITY = 1
angle = 0
pygame.init()

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Animations ")

#convertingg image is good for performance
player_image = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\image.png").convert()
player_image = pygame.transform.scale(player_image,(150,150))

clock = pygame.time.Clock()

text = pygame.font.Font(None,50)
surface = text.render("Hello Press Space to jump\n Hold to go up\n arrows to rotate",False,(0,0,0))

arrowleftheld = False
arrowrightheld = False
spaceheld=False
y=(HEIGHT-150)//2
velocity= 0
running = True

while running:
    display.fill((0,150,250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if y>0 :
                    velocity = -15
                spaceheld = True
            if event.key == pygame.K_LEFT:
                arrowleftheld=True
            if event.key == pygame.K_RIGHT:
                arrowrightheld=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                spaceheld =False
            if event.key == pygame.K_LEFT:
                arrowleftheld=False
            if event.key == pygame.K_RIGHT:  
                arrowrightheld=False  
    if spaceheld:
        if velocity>0: 
           velocity = 0
        if   y<HEIGHT and y>0:
            y -= 5*60//FPS
    if arrowrightheld:
        angle +=5
    if arrowleftheld:
        angle -=5

    rotated_image = pygame.transform.rotate(player_image, angle)

    if y<0:
        velocity = 0
    if velocity <=50:
        velocity +=GRAVITY*60//FPS 
    if y <= HEIGHT-155:
        y += velocity
    if y>HEIGHT:
        y=HEIGHT-155
    
    display.blit(rotated_image,((WIDTH-150)//2,y))
    display.blit(surface,(50,50))

    pygame.display.update()
    clock.tick(FPS)