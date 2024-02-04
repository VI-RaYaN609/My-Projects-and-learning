import pygame,sys

WHITE =(255,255,255)

pygame.init()
display = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Surfaces")

#empty surface
surface_height = 200
surface_width =200
surface = pygame.Surface((surface_width,surface_height))
surface.fill((255,0,50))

#image surface 
image = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\image.png")
image = pygame.transform.scale(image,(200,200))

#text surface 
text_font = pygame.font.Font(None,50)  #*(Font name , Font size {pixel})
text = text_font.render("...Put Text Here...",False,WHITE)  #*(Text,AntiAliasing,Color)

clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #!Background need to be before any other surface         
    display.fill((0,150,250))
     
    #?Rendering Surfaces
    display.blit(surface,(500,400))
    display.blit(image,(300,200))
    display.blit(text,(350,50))

    pygame.display.update()
    clock.tick(60)