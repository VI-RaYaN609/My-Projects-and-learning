import pygame,sys,math
from random import choice,randint

WIDTH = 800
HEIGHT = 800
FPS = 60
TIMESTEMP = 30*24*3600
AU = 149.6e6 *1000
G = 6.67428e-11  # F = GMm/r2
SCALE = 1000/(4*AU)#100 pixel far from sun
mouse_line = []
start_pos = False
colors = [(255,255,255),(0,255,255),(255,255,0),(255,0,255),(255,0,0),(0,255,0),(0,0,255)]


class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,weight,color,x_vel,y_vel):
      super().__init__()
      self.x = x # 3* screen_pos /1000*AU
      self.y = y
      self.x_vel = x_vel
      self.y_vel = y_vel
      self.weight = weight
      self.color = color
      self.orbit = []

    def draw(self,x,y):
       pygame.draw.circle(screen,self.color,(x,y),12)
       if len(self.orbit) > 2: #drawing orbit
          if len(self.orbit)>150:
            self.orbit.pop(0)
          pygame.draw.lines(screen, self.color, False, self.orbit, 2)
       distance_text = FONT.render(f"{round(self.weight/(2*10**30), 1)}Suns", 1, (255,255,255))
       screen.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

    def force_calc(self,planet):
        distance_x =  planet.x - self.x
        distance_y =  planet.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)  #Distance between the two planets
        force = G*self.weight*planet.weight/distance**2
        angle = math.atan2(distance_y,distance_x) #tan-1(y/x)
        force_x = math.cos(angle)*force
        force_y = math.sin(angle)*force
        return force_x, force_y
    
    def planet_position_update(self):
        total_fx = total_fy = 0 # the sum of Fx and Fy from each planet with the current planet
        for planet in all_sprites.sprites():
            if self == planet :
                continue
            fx,fy = self.force_calc(planet)
            total_fx += fx
            total_fy += fy
        self.x_vel += (total_fx / self.weight)*TIMESTEMP# F = m*a => a = F/m
        self.y_vel += (total_fy / self.weight)*TIMESTEMP
        self.x += self.x_vel 
        self.y += self.y_vel 
        self.orbit.append((self.x* SCALE,self.y* SCALE))

    def update(self):
       x = self.x * SCALE   #convert real positions to 
       y = self.y * SCALE    #screen pixel positions
       if x <-500 or x>WIDTH+500 or y <-500 or y>HEIGHT+500:
          self.kill()
       self.planet_position_update()
       self.draw(x,y)

pygame.init()

FONT = pygame.font.SysFont("comicsans", 16)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Slingshot Effect")

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if not start_pos: 
            start_pos = pygame.mouse.get_pos()
            chosen = choice(colors)
          else :
            x,y =start_pos
            mx,my = pygame.mouse.get_pos()
            x_vel = (mx-x)*AU/10000
            y_vel = (my-y)*AU/10000
            planet = Object(4*AU*x/1000,4*AU*y/1000,randint(10**31,2*10**32),chosen,x_vel,y_vel)
            all_sprites.add(planet)
            start_pos = False


    screen.fill((0,0,0))
    if start_pos:
      pygame.draw.line(screen,(255,255,255),start_pos,pygame.mouse.get_pos())
      pygame.draw.circle(screen,chosen,start_pos,12)
    all_sprites.update()
    pygame.display.update()
    clock.tick(FPS)