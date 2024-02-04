import pygame ,sys

pygame.init()

display = pygame.display.set_mode((1000,800))

clock = pygame.time.Clock()

timer = pygame.USEREVENT +1
pygame.time.set_timer(timer,1000)

counter = 0
fps = 0
while True :
    counter += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == timer:
           fps = counter;counter = 0
           pygame.display.set_caption(str(fps))

        