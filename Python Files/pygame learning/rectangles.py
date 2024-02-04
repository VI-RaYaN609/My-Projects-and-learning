import pygame,sys

pygame.init()
display=pygame.display.set_mode((1000,800))
pygame.display.set_caption("Rectangles")

player_surface = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\image.png").convert()
player_rectangle = player_surface.get_rect(midbottom=(500,701))

ground_surface = pygame.Surface((1000,100))
ground_surface.fill((0,150,0))
ground_rect = ground_surface.get_rect(bottomleft=(0,800))

text_font = pygame.font.Font(None,50)
text = text_font.render("Press A-D to Move!!",False,(255,255,255))

clock = pygame.time.Clock()
running = True
D_down =False
A_down =False
while running:
    display.fill((0,150,250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                D_down=True
            if event.key == pygame.K_a:
                A_down=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                D_down =False
            if event.key == pygame.K_a:
                A_down =False
    if D_down:
        player_rectangle.x +=4
        # if player left screen from right it will be back on the left
        if player_rectangle.left >=1000: player_rectangle.right=0
    if A_down:
        player_rectangle.x -=4
        #if player left screen from left it will be back from the right
        if player_rectangle.right<=0: player_rectangle.left=1000

    display.blit(ground_surface,ground_rect)
    display.blit(player_surface,player_rectangle)
    display.blit(text,(340,100))

    pygame.display.update()
    clock.tick(60)