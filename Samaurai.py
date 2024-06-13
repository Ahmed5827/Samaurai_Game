import pygame
from sys import exit
from random import *

pygame.mixer.init(34100, -16,2,2048)
pygame.init()


slash_sound = pygame.mixer.Sound('s8.mp3')
background_music = pygame.mixer.Sound("background music.mp3")
#https://www.youtube.com/watch?v=AY9MnQ4x3zk

screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("SAMURAI JACK : the midnight chaos : Beta")
clock = pygame.time.Clock()

fond=pygame.font.Font(None,50)

lost= fond.render("The monsters envaded the dejon !! type r to retry", True ,"red")
death=fond.render("YOU DIED !! type r to retry", True ,"red")
win=fond.render("YOU won !! type r to retry", True ,"red")


text=fond.render("Score:", True ,"red")
score_rect= text.get_rect(center=(1000,165))

#setting the icon
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)

# i used the methode (.convert_alpha()) to convert the images to somthing pygame can easely work with
#in short to make the game faster

# calling the images
sky = pygame.image.load("sky.png").convert_alpha()
ground= pygame.image.load("platforme.png").convert_alpha()
SAMURAI = pygame.image.load("player1.png").convert_alpha()
goul = pygame.image.load("enemy1.png").convert_alpha()
slash = pygame.image.load("slash.png").convert_alpha()
denjon = pygame.image.load("denjon.png").convert_alpha()
#put the samaurai AKA player in a rectangle so it will be much easier to manipulate it and detect collisions

SAMURAI_rect=SAMURAI.get_rect(center=(180,600))
# slash_rect=slash.get_rect(center=(SAMURAI_rect.x,SAMURAI_rect.y))
goul_rect=goul.get_rect(center=(1200,630))
denjon_rect = denjon.get_rect(center=(100,660))

#fill with colors
#screen.fill("white")

active=True
cont=True

slash_fram = 0  # number of frames the slash will appear in
i=0
background_music.play(-1)
while active:
    
    #close the game
    ch=str(i)
    score=fond.render(ch, True ,"red")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    key=(pygame.key.get_pressed())
    if cont:
        screen.blit(sky,(0,0))
        screen.blit(text,score_rect)
        screen.blit(ground, (0,135))
        
        screen.blit(score , (1100,150))
        screen.blit(SAMURAI,SAMURAI_rect)
        screen.blit(goul, goul_rect)
        screen.blit(denjon, denjon_rect)

   # when pressed add 40 frams to slash appearing the addition only works when theres no slash on the screen
        if key[pygame.K_SPACE] and slash_fram==0:
            slash_fram=40
            slash_sound.play()

                
        if key[pygame.K_RIGHT]:
                SAMURAI_rect.x +=5
        if key[pygame.K_LEFT]:
            SAMURAI_rect.x -=2
        if key[pygame.K_DOWN]:
            SAMURAI_rect.y +=3
        if key[pygame.K_UP]:
            SAMURAI_rect.y -=3
        if SAMURAI_rect.colliderect(goul_rect) :
            screen.blit(death , (80,150))
            i=0
            cont = False
        elif goul_rect.colliderect(denjon_rect) :
            screen.blit(lost , (40,140))
            i=0
            cont = False
        elif goul_rect.colliderect(denjon_rect) and SAMURAI_rect.colliderect(goul_rect):
            screen.blit(death , (80,150))
            i=0
            cont = False            

    if key[pygame.K_r] and cont ==False:

        cont=True
        SAMURAI_rect.x = 165
        goul_rect.x = 1300
        
    if SAMURAI_rect.y <=600:
        SAMURAI_rect.y=600

    if SAMURAI_rect.y >=687:
        SAMURAI_rect.y=687

    if SAMURAI_rect.x<=200:
        SAMURAI_rect.x=200
 #when slash fram is equal to  40 means i have to create an instanst of slash at the exact position as the samuray
    if slash_fram == 40:
        slash_rect = slash.get_rect(center=(SAMURAI_rect.x, SAMURAI_rect.y+25))
  # while th frams are not done we move the slash forward and with each movement we decrease the number of frams left untel it reach the end
    
    if slash_fram >0:
        slash_rect.x += 10
        slash_fram -= 2

        screen.blit(slash, slash_rect)
        if slash_rect.colliderect(goul_rect):
            slash_rect = slash.get_rect(center=(4000, 4000))
            screen.blit(sky,(0,0))
            screen.blit(text,score_rect)
            screen.blit(ground, (0,135))
        
            screen.blit(score , (1100,150))

            screen.blit(SAMURAI,SAMURAI_rect)
            screen.blit(denjon, denjon_rect)
            goul_rect.x=1200
            goul_rect.y=randint(550,700)
            i+=1

    goul_rect.x -=10
    

    if SAMURAI_rect.x >1160 :   SAMURAI_rect.x=1160


    pygame.display.update()
    #run the game on 60 FPS MAX
    clock.tick(60)