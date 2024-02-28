import pygame ,sys ,random

pygame.init()

WIDTH = 1000
HEIGHT = 800

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("hello")

#!intro elements
play_text_font = pygame.font.Font("Python Files\\pygame learning\\Fonts\\Pixeltype.ttf",50)
play_text=play_text_font.render("Play !!",False,(255,255,255))
play_text_rect = play_text.get_rect(center=(WIDTH//2,HEIGHT//2))

play_box = pygame.Surface((150,100))
play_box.fill((122, 0, 92))
play_box_rect = play_box.get_rect(center=(WIDTH//2,HEIGHT//2))

#!game elements
bird = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\images\\bird.png").convert_alpha()
bird = pygame.transform.scale(bird,(50,50))
bird_rect = bird.get_rect(midtop=(50,50))


poop = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\images\\bird poop .png").convert_alpha()
poop = pygame.transform.scale(poop,(50,50))


player = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\image.png").convert()
player = pygame.transform.scale(player,(100,100))
player_rect = player.get_rect(midbottom=(WIDTH//2,701))

ground = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\images\\ground.png")
ground = pygame.transform.scale(ground,(WIDTH+100,100))
ground_rect = ground.get_rect(bottomleft=(0,HEIGHT))

#!lost elements
lost_text_font = pygame.font.Font("Python Files\\pygame learning\\Fonts\\Pixeltype.ttf",100)
lost_text = lost_text_font.render("Looser !!",True,(255,255,255))
lost_text_rect = lost_text.get_rect(center=(WIDTH//2,HEIGHT//2))

exit_x = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\images\\X image.jpg").convert_alpha()
exit_x = pygame.transform.scale(exit_x,(75,75))
exit_x_rect = exit_x.get_rect(topleft=(25,15))

#!Score 
score_font = pygame.font.Font(None,80)
score_surface = score_font.render("0",False,(255,255,255))
score_rect = score_surface.get_rect(midtop=(WIDTH//2,100))
start_time = 0
score = 0

#Clock
clock = pygame.time.Clock()

#timers
poop_timer = pygame.USEREVENT + 1
poop_timer2 = pygame.USEREVENT + 2
rotate_timer = pygame.USEREVENT + 3
pygame.time.set_timer(poop_timer,1500)
pygame.time.set_timer(poop_timer2,2250)
pygame.time.set_timer(rotate_timer ,250)

Game = False 
lost = False
mousedown = False
KEYDOWN = set()
poops = list()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==pygame.MOUSEBUTTONDOWN :
            if play_box_rect.collidepoint(pygame.mouse.get_pos()) and not Game and not lost:
                Game = True

    if not Game and not lost :
        display.fill((0,150,250))
        display.blit(play_box,play_box_rect)
        display.blit(play_text,play_text_rect)
        

        pygame.display.update()
        clock.tick(60)
    #Game Loop
    while Game :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Game = False
                if event.key == pygame.K_RIGHT:
                    if player_rect.right < 1000:
                        player_rect.x += 10
                    KEYDOWN.add(event.key)
                if event.key == pygame.K_d:
                    if player_rect.right <1000:
                        player_rect.x += 10
                    KEYDOWN.add(event.key)
                if event.key == pygame.K_LEFT:
                    if player_rect.left > 0:
                       player_rect.x += -10
                    KEYDOWN.add(event.key)
                if event.key == pygame.K_a:
                    if player_rect.left > 0:
                       player_rect.x += -10
                    KEYDOWN.add(event.key)
         
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    if event.key in KEYDOWN: 
                     KEYDOWN.remove(event.key)
                if event.key == pygame.K_d:
                    if event.key in KEYDOWN: 
                     KEYDOWN.remove(event.key)
                if event.key == pygame.K_LEFT:
                    if event.key in KEYDOWN:
                     KEYDOWN.remove(event.key)
                if event.key == pygame.K_a:
                    if event.key in KEYDOWN:
                        KEYDOWN.remove(event.key)

            if event.type == poop_timer:
                x= random.randint(0,100)
                if x>=25:
                  poops.append(poop.get_rect(midtop=(bird_rect.x,bird_rect.y +4)))
        
        score =str ((pygame.time.get_ticks()-start_time)//1000)
        score_surface = score_font.render(score,False,(255,255,255))
        #player movement            
        if pygame.K_RIGHT  in KEYDOWN:
            if player_rect.right < 1000:
               player_rect.x += 8
        if pygame.K_d  in KEYDOWN:
            if player_rect.right < 1000:
               player_rect.x += 8
        if pygame.K_LEFT  in KEYDOWN:
            if player_rect.left > 0:
               player_rect.x += -8
        if pygame.K_a  in KEYDOWN:
            if player_rect.left > 0:
               player_rect.x += -8
        
        #bird movement
        if bird_rect.left == 1000 :
            bird_rect.right = 0
        bird_rect.x +=5
        
        
        #poop movement
        for poop_rect in poops:
            if poop_rect.y <=0:
                poops.remove(poop_rect)
            poop_rect.y += 4 
        #collisions 
            if player_rect.colliderect(poop_rect):
               lost = True ; Game = False;KEYDOWN.clear()
               
        #ground movement
        ground_rect.x -= 1.25
        if ground_rect.x <= -100:
            ground_rect.x = 0

        #displaying items
        display.fill((0,150,250))
        display.blit(score_surface,score_rect)
        display.blit(bird,bird_rect)
        for poop_rect in poops :
            display.blit(poop,poop_rect)
        display.blit(ground,ground_rect)
        display.blit(player,player_rect)
        

        pygame.display.update()
        clock.tick(60)

    while lost :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_x_rect.collidepoint(pygame.mouse.get_pos()):
                    lost = False
                    player_rect = player.get_rect(midbottom=(WIDTH//2,701))
                    bird_rect = bird.get_rect(midtop=(50,50))
                    poops = list()
                    start_time = pygame.time.get_ticks()
                    break
         
        display.fill((255,125,50))
        display.blit(lost_text,lost_text_rect)
        display.blit(exit_x,exit_x_rect)
        

        pygame.display.update()
        clock.tick(60)
    