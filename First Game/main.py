import pygame,sys
from random import randint

WIDTH = 1000
HEIGHT = 800
FPS = 60
KEYS=set()
start = True
Game = False
lost = False
pipe_pos = True
Mute = True
volumes = set()
start_time = 0
Alive_time = 0
High_score = 0
Mortal = True

class Bird(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image_right = pygame.image.load("First Game/Images/bird.png").convert_alpha()
        self.image_right = pygame.transform.scale(self.image_right,(50,50))
        self.image_left = pygame.transform.flip(self.image_right,True,False)
        self.image = self.image_right
        self.rect = self.image.get_rect(center=(100,HEIGHT//2))
        self.gravity = 0
        self.score = 0
        self.difficulty = 350
        self.y = 0
        #surfaces
        self.score_surf = time_font.render(str(self.score),False,(0, 186, 103))
        self.score_rect = self.score_surf.get_rect(center=(WIDTH//2,150))


    def jump(self):
       if self.rect.y > -5: self.gravity = 15
       else : self.gravity = 0

    def gravity_app(self):
        self.gravity -= 1
        self.rect.y -= self.gravity

    def movement(self):
        if pygame.K_a in KEYS:
            self.image = self.image_left
            self.rect.x += -4
        elif pygame.K_d in KEYS:
            self.image = self.image_right
            self.rect.x += 4

    def collisions(self) :
      global start,High_score
      if pygame.sprite.spritecollide(bird,pipes,False)or self.rect.y >= HEIGHT+20:
           if start : High_score = self.score
           elif High_score < self.score: High_score = self.score
           time = time_alive(start_time)

           self.High_score_surf = HightScore_font.render("Highest Score :"+str(High_score),False,(245, 54, 194))
           self.time_surf = time_font.render("Time alive :"+str(time/1000)+" s",False,(68, 4, 140))
           self.lost_score_surf = time_font.render("Current Score :"+str(self.score),False,(191, 6, 30))
           start = False
           if Mortal : return False
      return True
    
    def score_display(self):
        if pygame.sprite.spritecollide(bird,score_pipes,True):
            self.score += 1
            self.score_surf = time_font.render(str(self.score),False,(0, 186, 103))
        screen.blit(self.score_surf,self.score_rect)

    def update(self):
        global Game
        self.gravity_app()
        self.movement()
        Game = self.collisions()
        
class Pipe(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image_bottom = pygame.image.load("First Game/Images/Mario_pipe.png")
        self.image_bottom = pygame.transform.scale(self.image_bottom,(50,150))
        self.image_top = pygame.transform.rotate(self.image_bottom,180)
        self.image = self.image_bottom

    def create(self,pipe_pos):
        if pipe_pos: 
            self.image = self.image_top
            self.height = randint(150,350)
            self.image= pygame.transform.scale(self.image,(50,350)) 
            self.rect = self.image.get_rect(midtop=(WIDTH,1200))
            self.rect.top = 0 
            self.rect.x = WIDTH + randint(100,500)
            return False 
        else: 
            self.image = self.image_bottom
            self.height = randint(150,350)
            self.image = pygame.transform.scale(self.image,(50,350)) 
            self.rect = self.image.get_rect(midtop=(WIDTH,1200))
            self.rect.x = WIDTH + randint(100,500)
            self.rect.bottom = HEIGHT
            return True

    def create_score(self,x): # This will create a invisible surface on top of the surface so it count for score
        self.image = pygame.transform.scale(self.image,(1,HEIGHT)) # this is a vertical line 
        self.rect = self.image.get_rect(topleft=(x,0))
    
    def update(self):
        self.rect.x -= 4
        if self.rect.right <0 :
            self.kill()


def New_Game():
    global score_pipes,start_time,Game,pipes,all_sprites,bird,KEYS,start
    start = False
    Game = True
    KEYS = set()
    bird = Bird()
    pipes = pygame.sprite.Group()
    score_pipes = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(bird)
    start_time = pygame.time.get_ticks()

def exit_game(start,High_score):
    global Game
    Game = False 
    if start: High_score =bird.score 
    elif bird.score > High_score : High_score = bird.score
    bird.time_surf = time_font.render("Time alive :"+str(time_alive(start_time)/1000)+" s",False,(68, 4, 140))
    bird.lost_score_surf = time_font.render("Current Score :"+str(bird.score),False,(191, 6, 30))
    bird.High_score_surf = HightScore_font.render("Highest Score :"+str(High_score),False,(245, 54, 194))
    return High_score

def time_alive(start_time):
    return pygame.time.get_ticks()-start_time

def time_render(surf):
    screen.blit(surf,surf.get_rect(center=(WIDTH//2,60)))

def score_render(surf):
    screen.blit(surf,surf.get_rect(center=(WIDTH//2,600)))

def High_score_render(surf):
     screen.blit(surf,surf.get_rect(center=(WIDTH//2,750)))


pygame.init()
pygame.mixer.init()

Music = pygame.mixer.Sound("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\Python Files\\pygame learning\\Sounds\\IlyesMoan.mp3")
Music.set_volume(0)

volumes.add(Music)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FlappyBird")

Sound_surf = pygame.image.load("First Game\\Images\\sound.png").convert_alpha()
Mute_surf = pygame.image.load("First Game\\Images\\Mute.png").convert_alpha()
Sound_surf = pygame.transform.scale(Sound_surf,(40,40))
Mute_surf = pygame.transform.scale(Mute_surf,(40,40))

Sound_rect = Sound_surf.get_rect(topright=(WIDTH-15,11))
Sound_state = Mute_surf

#sky
sky_surface = pygame.image.load("First Game\\Images\\sky.jpg").convert()
sky_surface=  pygame.transform.scale(sky_surface,(WIDTH,HEIGHT))
sky_rect = sky_surface.get_rect(center=(WIDTH//2,HEIGHT//2))

Sound_back_surf = pygame.surface.Surface((50,50))
Sound_back_surf.fill((255,255,255))
Sound_back_rect = Sound_back_surf.get_rect(topright=(WIDTH-10,10))

X_surf = pygame.image.load("First Game/Images/X_image.png").convert_alpha()
X_surf = pygame.transform.scale(X_surf,(40,40))
X_rect = X_surf.get_rect(topleft=(10,10))


#!Lost elements
background_lost = pygame.image.load("First Game/Images/Flappy_Pixel_art.jpg").convert()
background_lost = pygame.transform.scale(background_lost,(WIDTH,HEIGHT))
background_lost_rect = background_lost.get_rect(center=(WIDTH//2,HEIGHT//2))

play_button = pygame.image.load("First Game/Images/Play_button_noBG.png").convert_alpha()
play_button = pygame.transform.scale(play_button,(350,150))
play_rect = play_button.get_rect(center=(WIDTH//2,(HEIGHT//2)-200))

time_font = pygame.font.Font('First Game\\Font\\Pixeltype.ttf',50)
HightScore_font = pygame.font.Font('First Game\\Font\\Pixeltype.ttf',60)

#!Timers
timer_pipe = pygame.USEREVENT +1
pygame.time.set_timer(timer_pipe,1200)

#Clock
clock = pygame.time.Clock()

while True :
    Music.play(-1)
    for event in pygame.event.get():
        #?quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #?Muting/Unmuting Music
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Sound_rect.collidepoint(pygame.mouse.get_pos()):
                if Mute : 
                  Mute = False 
                  Sound_state = Sound_surf 
                  for volume in volumes: volume.set_volume(0.5)
                else : 
                  Mute = True 
                  Sound_state = Mute_surf 
                  for volume in volumes: volume.set_volume(0)
        
        #?start/lost screen Events
        if not Game:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(pygame.mouse.get_pos()):
                    New_Game()
        
        #?Game Events
        else :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    bird.jump()
                if event.key == pygame.K_d or pygame.K_a:
                    KEYS.add(event.key)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or pygame.K_a:
                    if event.key in KEYS:
                      KEYS.remove(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if X_rect.collidepoint(pygame.mouse.get_pos()):
                    High_score = exit_game(start,High_score)
            #?Timers
            if event.type == timer_pipe:
                pipe =Pipe()
                pipe_pos = pipe.create(pipe_pos)
                good_pipe = True
                if pipes.sprites():
                    for pip in pipes.sprites():
                        if -bird.difficulty <pip.rect.x -pipe.rect.x < bird.difficulty :
                            pipe.kill()
                            good_pipe = False
                if good_pipe:
                    pipes.add(pipe)
                    all_sprites.add(pipe)
                    score_pipe = Pipe()
                    score_pipes.add(score_pipe)
                    score_pipe.create_score(pipe.rect.right)
                    random = randint(0,100)      
                    if random>=75:
                        pipe2 = Pipe()
                        pipe_pos = pipe2.create(pipe_pos)
                        if pipe_pos:
                           pipe2.image= pygame.transform.scale(pipe2.image,(50,pipe.height+200)) 
                        else :
                            if pipe.height -200 <0:
                                pipe.height += 50 
                            pipe2.image= pygame.transform.scale(pipe2.image,(50,pipe.height-200)) 
                        pipe2.rect.x = pipe.rect.x
                        pipes.add(pipe2)
                        all_sprites.add(pipe2)
                else :
                 pipe = None
                
    if Game : 

         #Sprites Update
         score_pipes.update()
         all_sprites.update()
    
         #DISPLAYING ITEMS
         screen.blit(sky_surface,sky_rect)
         screen.blit(X_surf,X_rect)
         #Sprites Display
         all_sprites.draw(screen)
         bird.score_display() #Display score in game

    else :
        screen.blit(background_lost,background_lost_rect)
        screen.blit(play_button,play_rect)
        if not start:
          High_score_render(bird.High_score_surf)
          time_render(bird.time_surf)
          score_render(bird.lost_score_surf)
    
    #? stuff that always happen
    screen.blit(Sound_back_surf,Sound_back_rect)
    screen.blit(Sound_state,Sound_rect)
    pygame.display.update()
    clock.tick(FPS)