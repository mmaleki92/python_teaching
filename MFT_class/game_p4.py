import pygame
import random
from pygame.locals import Rect
pygame.init()
disp=pygame.display.set_mode((900,500))

red=(255,0,0)
black=(0,0,0)
c=(0,90,0)
c1=(200,190,190)
c2=(170,30,70)
c3=(0,100,150)
c4=(255,0,0)

a = 20

x=420
y=250

xenem=420
yenem=400

xblock=50
yblock=50

xch=0
ych=0
cl = pygame.time.Clock()

game=True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT:
                xch=-.1
                ych=0
            elif ev.key == pygame.K_RIGHT:
                xch=.1
                ych=0
            elif ev.key == pygame.K_UP:
                xch=0
                ych=-.1
            elif ev.key == pygame.K_DOWN:
                xch=0
                ych=.1
    disp.fill(c1)
    
    x += xch
    y += ych
    x = x%880
    y = y%480

    p1 = Rect([x, y, a, a])
    p2 = Rect([xenem, yenem, 30, 30])
    p3 = Rect([xblock, yblock , 30 , 30])
    c = pygame.Rect.colliderect(p1, p2)
    d = pygame.Rect.colliderect(p1, p3)
    if c:
        xenem=random.randrange(20,880,10)
        yenem=random.randrange(20,480,10)
        xblock=random.randrange(20,880,10)
        yblock=random.randrange(20,480,10)
    if d:
        a += 20
    
    pygame.display.set_caption('move the Red and catch the Blue!')
    pygame.draw.rect(disp,c2,[x,y,a,a])
    
    pygame.draw.rect(disp,c3,[xenem,yenem,30,30])

    pygame.draw.rect(disp,c4,[xblock,yblock,30,30])

    pygame.draw.rect(disp,c,[0,0,900,20])
    pygame.draw.rect(disp,c,[0,480,900,20])
    pygame.draw.rect(disp,c,[0,0,20,500])
    pygame.draw.rect(disp,c,[880,0,20,500])

    pygame.display.update()
    cl.tick(1500)
                
pygame.quit()   
