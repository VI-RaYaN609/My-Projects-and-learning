import pygame,sys

WIDTH = 1000
HEIGHT = 800
FPS = 60
GRAVITY = 5

SpaceHeld = False

pygame.init()

#Setting the display 
display = pygame.display.set_mode((WIDTH,HEIGHT)) 

#setting the clock 
clock = pygame.time.Clock()

#Loading Images
player_image = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\image.png")

#Scaling Images
player_image = pygame.transform.scale(player_image,(300,300))

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #player velocity
        self.velocity = 5
        #player image
        self.image = player_image

        #you need rect to draw the player and not getting error when running 
        #if you comment this line below you get an error
        self.rect = self.image.get_rect()

        #setting image in center of screen
        self.rect.center = (WIDTH//2,HEIGHT//2)


    def update(self):
        #write anything that want to happen (jumping moving ...)
        self.velocity += GRAVITY

    def jump(self):
        #image cordonates
        self.rect.y -=50
        self.velocity=-50

#setting all sprites
all_sprites = pygame.sprite.Group()
Player = player()

#adding Player to sprites
all_sprites.add(Player)


running = True

while running :
    #background 
    #colored background 
    display.fill((0,0,0))

    #image background :
    #display.blit(Image,(0,0))
    
    #player falling 
    if Player.rect.y<=HEIGHT-300:
         Player.rect.y += Player.velocity/20

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SpaceHeld = True
                Player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                SpaceHeld = False
    #if SpaceHeld:
        #Player.jump()

    #updating all sprites
    all_sprites.update()

    #drawing all sprites
    all_sprites.draw(display)

    #updating display
    pygame.display.update()

    #setting frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()