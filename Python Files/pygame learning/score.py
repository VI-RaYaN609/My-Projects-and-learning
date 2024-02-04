import pygame,sys

FPS =60

pygame.init()
display = pygame.display.set_mode((1000,800))

intro_font = pygame.font.Font(None,45)
intro = intro_font.render("Press Enter to Play !! press Space To Jump(Hint :HOVER)",False,(255,255,255))

player_image = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\image.png").convert()
player_image = pygame.transform.scale(player_image,(150,150))
player_rect = player_image.get_rect(midbottom=(500,700))


snail = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\snail1.png").convert_alpha()
snail = pygame.transform.scale(snail,(100,75))
snail_rect = snail.get_rect(midbottom=(900,700))

ground_surface = pygame.Surface((1000,100))
ground_surface.fill((0,200,25))

looser_font = pygame.font.Font(None,150)
looser = looser_font.render("You LOST !!",True,(255,255,255))

def display_score():
    score = (pygame.time.get_ticks()-start_time)*2//1000
    score_font = pygame.font.Font(None,150)
    score_surf = score_font.render(f"{score}",False,(255,255,255))
    score_rect = score_surf.get_rect(center=(500,150))
    pygame.draw.rect(display,(25,155,50),score_rect)
    pygame.draw.rect(display,(25,155,50),score_rect,10)
    display.blit(score_surf,score_rect)

def jump():
    velocity = -16
    return velocity


lost = False
clock = pygame.time.Clock()
velocity = 0
space_heald = False
start_time = 0
score = 0
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom ==700:
                    velocity =jump()
                    space_heald= True
            if event.key == pygame.K_RETURN:
                lost = False
                start_time = pygame.time.get_ticks()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_heald= False
    
   

    
    #Sky and ground
    display.fill((0,150,250))
    display.blit(ground_surface,(0,700))
    display.blit(intro,(50,50))
    
    #Game Loop
    if not lost:
      
      player_rect.bottom += velocity
      if player_rect.bottom <= 700:
          velocity += 0.45
          if space_heald and velocity>0:
              velocity -=0.25
      if player_rect.bottom >= 700:
          player_rect.bottom=700
          velocity = 0

      #?snail Movement
      #if mouse is pointing on snail it wont move
      if not snail_rect.collidepoint(pygame.mouse.get_pos()): 
          snail_rect.x -= 4
          if snail_rect.right <= 0:snail_rect.x = 1000

      display.blit(snail,snail_rect)
      display.blit(player_image,player_rect)
      display_score()

      if player_rect.colliderect(snail_rect):
        lost = True
        snail_rect.x = 900
        player_rect.bottom = 700
    #Intro And lost screen
    else :
        display.blit(looser,(150,150))
    pygame.display.update()
    clock.tick(FPS)