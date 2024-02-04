import pygame,sys

WIDTH = 1000
HEIGHT = 800
FPS = 60

#setting pygame
pygame.init()

#! DISPLAY SETTINGS
#creating display 
display = pygame.display.set_mode((WIDTH,HEIGHT))
#setting window name 
pygame.display.set_caption("Hello World")
#setting window icon 
#pygame.display.set_icon()

#this set up the clock so you can choose the frame rate(the maximum times the while loop can run)
clock = pygame.time.Clock()


#!setting surfaces

#?color surface 
surface_width = 300
surface_height = 300
surface_position = ((WIDTH-surface_width)//2,(HEIGHT-surface_height)//2) #?position is center of window
surface = pygame.Surface((surface_width,surface_height)) 

#surface color
surface.fill((0,0,0))

#?image surface 
image_surface = pygame.image.load("C:\\Users\\VI RaYaN\\Desktop\\VS Code\\ILYES GAY GAME\\image.png")
#converting image (help a lot with performance)
image_surface.convert()
#scaling image 
image_surface = pygame.transform.scale(image_surface,(150,150))
#position of image
image_surface_position = ((WIDTH-150)//2,(HEIGHT-150)//2)

#?text surface
text_size = 50 
text_font = pygame.font.Font(None,text_size) #*(font type,font size) none is default
text_position = ((WIDTH-text_size*3)//2,50)
Text = 'hello world'
text_surface = text_font.render(Text,False,(255,255,255))     #*(text,AntiAliasing,color)


#you need a infinite while loop so the game window dont close 
keydown=False
mousedown=False
running = True

while running :
    #this for loop will run thought all event happening in the window by the user
    for event in pygame.event.get():
        #this will make sure that  the window close if you hit X button
        if event.type == pygame.QUIT:
            pygame.quit()
            #this will stop the code so you dont get errors
            sys.exit()
        #!keybord input 
        #? Keyboard Key pressed    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Text="Space Pressed!!"
                text_surface2 = text_font.render(Text,False,(255,255,255))
                keydown=True
            if event.key == pygame.K_w :
                Text="W Pressed !!! WWWW"
                text_surface2 = text_font.render(Text,False,(255,255,255))
                keydown = True

        #? Keyboard Key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                keydown=False
            if event.key == pygame.K_w:
                keydown = False

        #!Mouse input
        #?Mouse buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            Text="Mouse Held"
            text_surface2 = text_font.render(Text,False,(255,255,255))
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
        if event.type == pygame.MOUSEWHEEL:
            pass

        #?Mouse motion
        if event.type == pygame.MOUSEMOTION:
            pass

    #!rendering surfaces :
    #!Background need to be rendered first(first in code) so it wont be on top of other assets
    #this will fill the display with a color you choose by RGB Values
    display.fill((0,150,250))   #you can have a variable holding the RGB Values

    #? rendering other surfaces
    display.blit(surface ,surface_position)

    display.blit(image_surface ,image_surface_position)
    
    display.blit(text_surface,text_position)
    if keydown or mousedown:
        display.blit(text_surface2 ,(400,500))

    
    #setting up frame rate
    clock.tick(FPS)
    #updating Display
    pygame.display.update()
