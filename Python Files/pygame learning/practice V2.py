import pygame ,sys ,random

pygame.init()
pygame.mixer.init()

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
bird = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\image.png").convert_alpha()
bird = pygame.transform.scale(bird,(70,70))
bird_rect = bird.get_rect(midtop=(50,50))


poop = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\images\\bird poop .png").convert_alpha()
poop = pygame.transform.scale(poop,(50,50))

sound_button_surface = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\images\\sound.png").convert_alpha()
sound_button_surface = pygame.transform.scale(sound_button_surface,(50,50))
sound_button_rect = sound_button_surface.get_rect(midright=(WIDTH-10,35))
Mute = False

player = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\snail1.png").convert_alpha()
player = pygame.transform.scale(player,(100,80))
player_rect = player.get_rect(midbottom=(WIDTH//2,701))

ground = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\images\\ground.png")
ground = pygame.transform.scale(ground,(WIDTH+100,100))
ground_rect = ground.get_rect(bottomleft=(0,HEIGHT))

#!lost elements
pride = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\download.png")
pride = pygame.transform.scale(pride,(WIDTH,HEIGHT))
pride_rect = pride.get_rect(center = (WIDTH//2,HEIGHT//2))

lost_background_image = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\images\\Ilyes_forest.png").convert()
lost_background_image = pygame.transform.scale(lost_background_image,(WIDTH-200,HEIGHT-200))
lost_background_rect = lost_background_image.get_rect(center = (WIDTH//2,HEIGHT//2))

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
score = 0


#? SOUNDS
pooping_sound = pygame.mixer.Sound("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\Sounds\\IlyesMoan.mp3")
pooping_sound.set_volume(0.5)


#Clock
clock = pygame.time.Clock()

#timers
poop_timer = pygame.USEREVENT + 1
difficulty_timer = pygame.USEREVENT + 2
rotate_timer = pygame.USEREVENT + 3
score_timer = pygame.USEREVENT + 4
difficulty = 3000
pygame.time.set_timer(poop_timer,difficulty)
pygame.time.set_timer(difficulty_timer,10000)
pygame.time.set_timer(rotate_timer ,250)
pygame.time.set_timer(score_timer,1000)

#!functions

def Mute_sound_func():
   global Mute,sound_button_surface
   if sound_button_rect.collidepoint(pygame.mouse.get_pos()):
      if Mute:
           for element in sounds:
               element.set_volume(0.5)
           sound_button_surface = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\images\\sound.png").convert_alpha()
           Mute = False
      else : 
           for element in sounds:
               element.set_volume(0)
           sound_button_surface = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\images\\Mute.png").convert_alpha()
           Mute = True
      sound_button_surface = pygame.transform.scale(sound_button_surface,(50,50))



Game = False 
lost = False

KEYDOWN = set()
poops = list()
sounds = set()           #This contain all sounds so you can use it to mute or unmute

angle = 0
velocity = 0
angl = 0
ADMIN_MODE = True
x_random = 15
sounds.add(pooping_sound)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==pygame.MOUSEBUTTONDOWN :
            if play_box_rect.collidepoint(pygame.mouse.get_pos()) and not Game and not lost:
                Game = True ; start_time = pygame.time.get_ticks()

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

            #! KEY PRESSED
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Game = False
                
                #MOVING RIGHT
                if event.key == pygame.K_RIGHT:
                    player = pygame.transform.flip(player,True,False)
                    if player_rect.right < 1000:
                        player_rect.x += 10
                    KEYDOWN.add(event.key)
                if event.key == pygame.K_d:
                    player = pygame.transform.flip(player,True,False)
                    if player_rect.right <1000:
                        player_rect.x += 10
                    KEYDOWN.add(event.key)
                
                #MOVING LEFT
                if event.key == pygame.K_LEFT:
                    if player_rect.left > 0:
                       player_rect.x += -10
                    KEYDOWN.add(event.key)
                if event.key == pygame.K_a:
                    if player_rect.left > 0:
                       player_rect.x += -10
                    KEYDOWN.add(event.key)
                
                #JUMPING
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 700:
                       velocity = -12
                    KEYDOWN.add(event.key)
                if event.key == pygame.K_UP:
                    if player_rect.bottom == 700:
                       velocity = -12
                    KEYDOWN.add(pygame.K_SPACE)
                if event.key == pygame.K_w:
                    if player_rect.bottom == 700:
                        velocity = -12
                    KEYDOWN.add(pygame.K_SPACE)
                
            #! KEY RELEASE
            if event.type == pygame.KEYUP:

                #MOVING RIGHT
                if event.key == pygame.K_RIGHT:
                    player = pygame.transform.flip(player,True,False)
                    if event.key in KEYDOWN: 
                     KEYDOWN.remove(event.key)
                if event.key == pygame.K_d:
                    player = pygame.transform.flip(player,True,False)
                    if event.key in KEYDOWN: 
                     KEYDOWN.remove(event.key)

                #MOVING LEFT
                if event.key == pygame.K_LEFT:
                    if event.key in KEYDOWN:
                     KEYDOWN.remove(event.key)
                if event.key == pygame.K_a:
                    if event.key in KEYDOWN:
                        KEYDOWN.remove(event.key)
                
                #JUMPING
                if event.key == pygame.K_SPACE:
                    if event.key in KEYDOWN:
                        KEYDOWN.remove(event.key)
                        angle = 0
                if event.key == pygame.K_UP:
                    if pygame.K_SPACE in KEYDOWN:
                        KEYDOWN.remove(pygame.K_SPACE)
                        angle = 0
                if event.key == pygame.K_w:
                    if pygame.K_SPACE in KEYDOWN:
                        KEYDOWN.remove(pygame.K_SPACE)
                        angle =0           


            #!MOUSE BUTTON DOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mute_sound_func()


            #!TIMERS
            if event.type == difficulty_timer :
                if difficulty > 750:
                   difficulty -= 300
                   pygame.time.set_timer(poop_timer,difficulty)
                else :
                    if x_random >0:
                        x_random -5
                print(difficulty)

            if event.type == poop_timer:
                x= random.randint(x_random,100)
                if x >=50:
                  poops.append(poop.get_rect(midtop=(bird_rect.right-50,bird_rect.y+50)))
                  pooping_sound.play()

            if event.type == score_timer:
                #score += 1
                #score_surface = score_font.render(str(score),False,(255,255,255))
                pass


        score =str ((pygame.time.get_ticks()-start_time)//1000)
        score_surface = score_font.render(score,False,(255,255,255))

        if player_rect.bottom >=700:
            angle = 0

        rotated_player = pygame.transform.rotate(player,angle)
        #player movement        
        #?Jump
        
        # Y movement
        player_rect.bottom += velocity
        
        if player_rect.bottom <= 700:
            # Gravity
             velocity += 0.5
             if pygame.K_SPACE in KEYDOWN and velocity>0:  
                #gliding
                 velocity -=0.25
                 if player_rect.bottom < 700 :
                     angle += 10
        if player_rect.bottom >= 700:
             player_rect.bottom=700
             velocity = 0

        #?Movements left and right
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
            if player_rect.colliderect(poop_rect) and not ADMIN_MODE:
               lost = True ; Game = False;KEYDOWN.clear();pooping_sound.stop()


        #ground movement
        ground_rect.x -= 1.25
        if ground_rect.x <= -100:
            ground_rect.x = 0

        #!displaying items

        display.fill((0,150,250))
        display.blit(sound_button_surface,sound_button_rect)
        display.blit(score_surface,score_rect)
        display.blit(bird,bird_rect)
        for poop_rect in poops :
            display.blit(poop,poop_rect)
        display.blit(ground,ground_rect)
        display.blit(rotated_player,player_rect)
        

        pygame.display.update()
        clock.tick(60)

    while lost :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Mouse collide X
                Mute_sound_func()
                
                if exit_x_rect.collidepoint(pygame.mouse.get_pos()):
                    lost = False
                    player_rect = player.get_rect(midbottom=(WIDTH//2,701))
                    bird_rect = bird.get_rect(midtop=(50,50))
                    poops = list()
                    start_time = pygame.time.get_ticks()
                    angle = 0
                    difficulty = 3000 #ms
                    break
        display.blit(pride,pride_rect)
        display.blit(sound_button_surface,sound_button_rect)
        display.blit(lost_background_image,lost_background_rect)
        display.blit(lost_text,lost_text_rect)
        display.blit(exit_x,exit_x_rect)
        

        pygame.display.update()
        clock.tick(60)
    