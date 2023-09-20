import pygame
import time
import random
from pygame.locals import *
pygame.init()
dis = pygame.display.set_mode((1000 , 500))
pygame.display.set_caption('pacmanpy')
clock = pygame.time.Clock()
dis.fill([0 , 0 , 15])
color1 = [255 , 195 , 67]
color2 = [255 , 122 , 243]
color3 = [127 , 255 , 255]
color4 = [255 , 93 , 93]
pacman_color = [255 , 255 , 0]
badcolor = [2 , 2 , 176]
foodcolor = [199 , 199 , 199]
vcolor = [0 , 0 , 80 ]
bgcolor = [0 , 0 , 15]
pygame.display.update()
i1 = pygame.image.load('1.jpg')
dis.blit(i1 , (0 , 0))
pygame.display.update()
time.sleep(3)
i2 = pygame.image.load('2.jpg')
dis.blit(i2 , (0 , 0))
pygame.display.update()
time.sleep(3)
i3 = pygame.image.load('3.jpg')
dis.blit(i3 , (0 , 0))
pygame.display.update()
time.sleep(3)
i4 = pygame.image.load('4.jpg')
dis.blit(i4 , (0 , 0))
pygame.display.update()
time.sleep(3)
i5 = pygame.image.load('5.jpg')
dis.blit(i5 , (0 , 0))
pygame.display.update()
time.sleep(3)
i6 = pygame.image.load('6.jpg')
dis.blit(i6 , (0 , 0))
pygame.display.update()
time.sleep(3)
i7 = pygame.image.load('7.jpg')
dis.blit(i7 , (0 , 0))
pygame.display.update()
time.sleep(1)
i8 = pygame.image.load('8.jpg')
dis.blit(i8 , (0 , 0))
pygame.display.update()
time.sleep(1)
i9 = pygame.image.load('9.jpg')
dis.blit(i9 , (0 , 0))
pygame.display.update()
time.sleep(1)
i10 = pygame.image.load('10.jpg')
dis.blit(i10 , (0 , 0))
pygame.display.update()
time.sleep(1)
i11 = pygame.image.load('11.jpg')
dis.blit(i11 , (0 , 0))
pygame.display.update()
time.sleep(1)
i12 = pygame.image.load('12.jpg')
dis.blit(i12 , (0 , 0))
pygame.display.update()
time.sleep(1)
i13 = pygame.image.load('13.jpg')
dis.blit(i13 , (0 , 0))
pygame.display.update()
time.sleep(1)
i14 = pygame.image.load('14.jpg')
dis.blit(i14 , (0 , 0))
pygame.display.update()
time.sleep(1)
i15 = pygame.image.load('15.jpg')
dis.blit(i15 , (0 , 0))
pygame.display.update()
time.sleep(1)
i16 = pygame.image.load('16.jpg')
dis.blit(i16 , (0 , 0))
pygame.display.update()
time.sleep(1)
i17 = pygame.image.load('17.jpg')
dis.blit(i17 , (0 , 0))
pygame.display.update()
time.sleep(1)
i18 = pygame.image.load('18.jpg')
dis.blit(i18 , (0 , 0))
pygame.display.update()
time.sleep(1)
i19 = pygame.image.load('19.jpg')
dis.blit(i19 , (0 , 0))
pygame.display.update()
time.sleep(1)
i20 = pygame.image.load('20.jpg')
dis.blit(i20 , (0 , 0))
pygame.display.update()
time.sleep(1)
i21 = pygame.image.load('21.jpg')
dis.blit(i21 , (0 , 0))
pygame.display.update()
time.sleep(1)
i22 = pygame.image.load('22.jpg')
dis.blit(i22 , (0 , 0))
pygame.display.update()
time.sleep(1)
i23 = pygame.image.load('23.jpg')
dis.blit(i23 , (0 , 0))
pygame.display.update()
time.sleep(3)
i24 = pygame.image.load('24.jpg')
dis.blit(i24 , (0 , 0))
pygame.display.update()
time.sleep(3)
i25 = pygame.image.load('25.jpg')
dis.blit(i25 , (0 , 0))
pygame.display.update()
time.sleep(3)
i26 = pygame.image.load('26.jpg')
dis.blit(i26 , (0 , 0))
pygame.display.update()
time.sleep(7)
x = 500
x_change = 0
y = 450
y_change = 0
x1 =500
x1_change = 0
y1 = 250
y1_change = 0
x2 = 500
x2_change = 0
y2 = 250
y2_change = 0
x3 = 500
x3_change = 0
y3 = 250
y3_change = 0
x4 = 500
x4_change = 0
y4 = 250
y4_change = 0
a = [[100,450] , [300,450] , [700,450] , [900,450] , [100,350] , [300,350] , [500,350] , [700,350] , [900,350] , [100,250] , [300,250] , [500,250] , [700,250] , [900,250] , [100,150] , [300,150] , [500,150] , [700,150] , [900,150] , [100,50] , [300,50] , [500,50] , [700,50] , [900,50] , [100000000 , 2000000000]]
b = [[200,400],[800,400] ,[200,100],[800,100],[20000000,20000]]
for game2 in range (3):
    game = True
    while game :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -50
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 50
                elif event.key == pygame.K_LEFT:
                    x_change = -50
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 50
                    y_change = 0
        if 50 <= x + x_change <= 950:
            x += x_change
        if 50 <= y + y_change <= 450:
            y += y_change
        c = [x , y]
        c1 = [x1 , y1]
        c2 = [x2 , y2]
        c3 = [x3 ,y3]
        c4 = [x4 , y4]
        pygame.display.update()
        dis.fill([0 , 0 , 15])
        player = pygame.draw.circle(dis , pacman_color , c , 20 , 20 )
        pygame.display.update()
        g1 = pygame.draw.rect(dis , color1 , [x1 , y1 , 30 , 30])
        g2 = pygame.draw.rect(dis , color2 , [x2 , y2 , 30 , 30])
        g3 = pygame.draw.rect(dis , color3 , [x3 , y3 , 30 , 30])
        g4 = pygame.draw.rect(dis , color4 , [x4 , y4 , 30 , 30])
        pygame.display.update()
        pygame.draw.rect(dis , vcolor , [30 , 20 , 940 , 10])
        pygame.draw.rect(dis , vcolor , [30 , 470 , 940 , 10])
        pygame.draw.rect(dis , vcolor , [20 , 20 , 10 , 460 ])
        pygame.draw.rect(dis , vcolor , [970 , 20 , 10 , 460 ])
        pygame.display.update()
        for i in a:
            pygame.draw.circle(dis , foodcolor , i , 5 , 5)
            if c == i:
                a.remove(i)
        pygame.display.update()
        for m in b:
            pygame.draw.circle(dis , foodcolor , m , 10 , 10)
            if c == m:
                b.remove(m)
                color1 = [2 , 2 , 176]
                color2 = [2 , 2 , 176]
                color3 = [2 , 2 , 176]
                color4 = [2 , 2 , 176]
                if c == c1 :
                    del (g1)
                if c == c2 :
                    del (g2)
                if c == c3 :
                    del (g3)
                if c == c4 :
                    del (g4)
                # time.sleep(10)
                color1 = [255 , 195 , 67]
                color2 = [255 , 122 , 243]
                color3 = [127 , 255 , 255]
                color4 = [255 , 93 , 93]
        a1 = random.choice(['y1_change' , 'x1_change'])
        b1 = random.choice(['+' , '-'])
        if a1 == 'x1_change':
            if b1 == '-':
                x1_change = -50
                y1_change = 0
            elif b1 == '+':
                x1_change = 50
                y1_change = 0
        elif a1 == 'y1_change':
            if b1 == '-':
                x1_change = 0
                y1_change = -50
            elif b1 == '+':
                x1_change = 0
                y1_change = 50
        a2 = random.choice(['y2_change' , 'x2_change'])
        b2 = random.choice(['+' , '-'])
        if a2 == 'x2_change':
            if b2 == '-':
                x2_change = -50
                y2_change = 0
            elif b2 == '+':
                x2_change = 50
                y2_change = 0
        elif a2 == 'y2_change':
            if b2 == '-':
                x2_change = 0
                y2_change = -50
            elif b2 == '+':
                x2_change = 0
                y2_change = 50
        a3 = random.choice(['y3_change' , 'x3_change'])
        b3 = random.choice(['+' , '-'])
        if a == 'x3_change':
            if b3 == '-':
                x3_change = -50
                y3_change = 0
            elif b3 == '+':
                x_change = 50
                y_change = 0
        elif a3 == 'y3_change':
            if b3 == '-':
                x3_change = 0
                y3_change = -50
            elif b3 == '+':
                x3_change = 0
                y3_change = 50
        a4 = random.choice(['y4_change' , 'x4_change'])
        b4 = random.choice(['+' , '-'])
        if a4 == 'x4_change':
            if b4 == '-':
                x4_change = -50
                y4_change = 0
            elif b4 == '+':
                x4_change = 50
                y4_change = 0
        elif a4 == 'y4_change':
            if b4 == '-':
                x4_change = 0
                y4_change = -50
            elif b == '+':
                x4_change = 0
                y4_change = 50
        if 50 <= x1 + x1_change <= 950:
            x1 += x1_change
        if 50 <= y1 + y1_change <= 450:
            y1 += y1_change
        if 50 <= x2 + x2_change <= 950:
            x2 += x2_change
        if 50 <= y2 + y2_change <= 450:
            y2 += y2_change
        if 50 <= x3 + x3_change <= 950:
            x += x3_change
        if 50 <= y3 + y3_change <= 450:
            y3 += y3_change
        if 50 <= x4 + x4_change <= 950:
            x4 += x4_change
        if 50 <= y4 + y4_change <= 450:
            y4 += y4_change   
        if c == c1 or c == c2 or c == c3 or c == c4 :
            game = False
        if a == [[100000000 , 2000000000]] and b == [[20000000,20000]] :
            i1 = pygame.image.load('27.jpg')
            dis.blit(i1 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i2 = pygame.image.load('28.jpg')
            dis.blit(i2 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i3 = pygame.image.load('29.jpg')
            dis.blit(i3 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i4 = pygame.image.load('30.jpg')
            dis.blit(i4 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i5 = pygame.image.load('31.jpg')
            dis.blit(i5 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i6 = pygame.image.load('32.jpg')
            dis.blit(i6 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i7 = pygame.image.load('33.jpg')
            dis.blit(i7 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i8 = pygame.image.load('34.jpg')
            dis.blit(i8 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i9 = pygame.image.load('35.jpg')
            dis.blit(i9 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i10 = pygame.image.load('36.jpg')
            dis.blit(i10 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i11 = pygame.image.load('37.jpg')
            dis.blit(i11 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i12 = pygame.image.load('38.jpg')
            dis.blit(i12 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i13 = pygame.image.load('39.jpg')
            dis.blit(i13 , (0 , 0))
            time.sleep(1)
            i14 = pygame.image.load('40.jpg')
            dis.blit(i14 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i15 = pygame.image.load('41.jpg')
            dis.blit(i15 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i16 = pygame.image.load('42.jpg')
            dis.blit(i16 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i17 = pygame.image.load('43.jpg')
            dis.blit(i17 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i18 = pygame.image.load('44.jpg')
            dis.blit(i18 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i19 = pygame.image.load('45.jpg')
            dis.blit(i19 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i20 = pygame.image.load('46.jpg')
            dis.blit(i20 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i21 = pygame.image.load('47.jpg')
            dis.blit(i21 , (0 , 0))
            pygame.display.update()
            time.sleep(1)
            i22 = pygame.image.load('48.jpg')
            dis.blit(i22 , (0 , 0))
            pygame.display.update()
            pygame.mixer.music.load('13.mp3')
            pygame.mixer.music.play()
            time.sleep(53)
        pygame.display.update()
        clock.tick(4)
pygame.quit()
quit()
