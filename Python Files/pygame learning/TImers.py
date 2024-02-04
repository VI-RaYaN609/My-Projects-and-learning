import pygame ,sys

pygame.init()
display=  pygame.display.set_mode((1000,800))

#! Timer
obstacles_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacles_timer,1500)  #*1500 ms

clock = pygame.time.Clock()
game = False
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                game=True
        if event.type==obstacles_timer:
            print("1,5 seconds passed")
    if game:
         pass
    else:
        pass

    display.fill((0,150,250))
    clock.tick(60)
    pygame.display.update()