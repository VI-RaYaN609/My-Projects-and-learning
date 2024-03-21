import pygame,sys,math

AU = 149.6e6 *1000
G = 6.67428e-11  # F = GMm/r2
Scale_meter = 250
SCALE = Scale_meter / AU #100 pixel far from sun
TIMESTEMP = 3600*24 # 1 day

class Planet(pygame.sprite.Sprite):
    def __init__(self,x,y,y_vel,name,weight,radius_pixel,color,isStar):
        super().__init__()
        self.name = name
        self.weight = weight
        self.radius_pixle = radius_pixel
        self.color = color  
        self.isStar = isStar
        self.distance_to_sun = 0
        self.orbit = []

        self.x = x  #AU
        self.y = y  #AU
        self.x_vel = 0
        self.y_vel = y_vel
        
    
    def force_calc(self,planet):
        distance_x = planet.x - self.x
        distance_y = planet.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)  #Distance between the two planets
        if planet.isStar: self.distance_to_sun = distance

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
        self.x_vel += (total_fx / self.weight) * TIMESTEMP # F = m*a => a = F/m
        self.y_vel += (total_fy / self.weight) * TIMESTEMP
        self.x += self.x_vel * TIMESTEMP
        self.y += self.y_vel * TIMESTEMP
        self.orbit.append((self.x,self.y))

    def update(self):
        self.draw2()
        self.planet_position_update()
    
    def draw2(self):
        x = self.x * SCALE + 500
        y = self.y * SCALE + 500
        pygame.draw.circle(screen, self.color, (x, y), self.radius_pixle)
        if len(self.orbit) > 2:
            if len(self.orbit)>250:
                self.orbit.pop(0)
            updated_points = []
            for point in self.orbit: 
                x,y = point 
                x = x * SCALE + 500  
                y = y*SCALE + 500
                updated_points.append((x,y))
            pygame.draw.lines(screen, self.color, False, updated_points, 2)
        if not self.isStar:
            text = font.render("{:.5f} AU".format(self.distance_to_sun/AU),False,(255,255,255))
            screen.blit(text,(x,y))

pygame.init()

#Planets
Sun = Planet(0,0,0,"Sun",2*10**30,30,(255,255,0),True)
Earth = Planet(-1*AU,0,29.783*1000,"Earth",5.972*10**24,12,(0,150,250),False)
Mars = Planet(-1.524*AU,0,24.077*1000,"Mars",6.4*10**23,8,(188,39,50),False)
venus = Planet(0.723*AU,0,-35.02*1000,"venus",4.8*10**24,10,(255,255,255),False)
mercury = Planet(0.387*AU,0,-47.4*1000,"mercury",3.30*10**23,10,(80,78,81),False)
 

all_planets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_planets.add(Earth,Mars,venus,mercury)
all_sprites.add(Sun,Earth,Mars,venus,mercury)

font =   pygame.font.Font(None,45)

screen = pygame.display.set_mode((1000,1000))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0,0,0))

    all_planets.update()
    Sun.draw2()
    Sun.update()

    pygame.display.update()
    clock.tick(60)