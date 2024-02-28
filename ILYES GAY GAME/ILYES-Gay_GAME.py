import pygame 

angle = 0
WIDTH = 1000
HEIGHT = 800
FPS = 30

pygame.init()
display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("ILYES GAY")
clock = pygame.time.Clock()
running = True 

player_image = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\image.png")
player_image = pygame.transform.scale(player_image,(300,300))

background_image = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\download.png")
background_image = pygame.transform.scale(background_image,(WIDTH,HEIGHT))

heart_image = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\heart.png")
heart_image = pygame.transform.scale(heart_image,(75,75))
X=False
hx=WIDTH
hy=HEIGHT
while running :
    if hx<15:
        hx=WIDTH
    if hy<15:
        hy=HEIGHT
    hx-=15
    hy-=15

    display.blit(background_image,(0,0))

    display.blit(heart_image,(WIDTH//2,hy))
    display.blit(heart_image,(WIDTH//2,WIDTH-hy))
    display.blit(heart_image,(hx,HEIGHT//2))
    display.blit(heart_image,(HEIGHT-hx,HEIGHT//2))
    display.blit(heart_image,(hx,hy))
    display.blit(heart_image,(WIDTH-hx,HEIGHT-hy))

    image = pygame.transform.rotate(player_image,angle)

    display.blit(image,((WIDTH-300)//2,(HEIGHT-300)//2))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                X = True
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_SPACE:
                X =False   
    if X :
       angle +=5
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()