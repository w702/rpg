import pygame
from pygame.locals import*
import sys, random
import pygame.mixer

rect=Rect(0,0,640,480)
GS=32	#一ますのサイズ
tate=15
yoko=20
x,y=10,1
a,b=0,0
idx=0
maxhp=100
myhp=100
power=10
potion=0

#map一覧
map=       [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,2],
	        [2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2],]

map1=      [[2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2],
	        [2,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],]

map2=      [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
	        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],]

#画像の読み込み
def image(filename):
    image=pygame.image.load(filename).convert_alpha()
    return image

#mapの描画
def draw_map(screen):
    if map[y][x] == 4:
        return False
    p = random.randint(2, 17)
    q = random.randint(2, 13)
    if map[q][p] == 0:
        map[q][p] = random.choice([4,5,5,5,5,5,5,5,5,5,5,5,5])

    for i in range(tate):	#縦回繰り返す
        for ix in range(yoko):
            if map[i][ix]==0:
                screen.blit(MapImg,(ix*GS,i*GS))
            if map[i][ix]==1:
                screen.blit(MapImg1,(ix*GS,i*GS))
            if map[i][ix]==2:
                screen.blit(MapImg2,(ix*GS,i*GS))
            if map[i][ix]==4:
                screen.blit(MapImg4,(ix*GS,i*GS))
            if map[i][ix]==5:
                screen.blit(MapImg,(ix*GS,i*GS))

#map1の描画
def draw_map1(screen):
    if map1[y][x] == 1:
        return False
    if map1[y][x] == 4:
        return False
    p = random.randint(2, 17)
    q = random.randint(2, 13)
    if map1[q][p] == 0:
        map1[q][p] = random.choice([4,5,5,5,5,5,5,5,5,5,5,5,5])
    for a in range(tate):	#縦回繰り返す
        for b in range(yoko):
            if map1[a][b]==0:
                screen.blit(MapImg,(b*GS,a*GS))
            if map1[a][b]==1:
                screen.blit(MapImg1,(b*GS,a*GS))
            if map1[a][b]==2:
                screen.blit(MapImg2,(b*GS,a*GS))
            if map1[a][b]==3:
                screen.blit(MapImg3,(b*GS,a*GS))
            if map1[a][b]==4:
                screen.blit(MapImg4,(b*GS,a*GS))
            if map1[a][b]==5:
                screen.blit(MapImg,(b*GS,a*GS))

#map2の描画
def draw_map2(screen):
    if map1[y][x] == 1:
        return False
    if map2[y][x] == 4:
        return False
    p = random.randint(2, 17)
    q = random.randint(2, 13)
    if map2[q][p] == 0:
        map2[q][p] = random.choice([4,5,5,5,5,5,5,5,5,5,5,5,5])
    for a in range(tate):	#縦回繰り返す
        for b in range(yoko):
            if map2[a][b]==0:
                screen.blit(MapImg,(b*GS,a*GS))
            if map2[a][b]==1:
                screen.blit(MapImg1,(b*GS,a*GS))
            if map2[a][b]==2:
                screen.blit(MapImg2,(b*GS,a*GS))
            if map2[a][b]==3:
                screen.blit(MapImg3,(b*GS,a*GS))
            if map2[a][b]==4:
                screen.blit(MapImg4,(b*GS,a*GS))
            if map2[a][b]==5:
                screen.blit(MapImg,(b*GS,a*GS))

#壁の上と画面外にいけないようにする
def is_movable(x, y):
    if x < 0 or x > 19 or y < 0 or y > 14:
        return False
    if map[y][x] == 2: 
        return False
    return True

pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("マップを作成")
font = pygame.font.Font(None, 55) 

def drawtext():
    myhp1 = font.render("myhp:"+ str(myhp), True, (255,255,255))   
    screen.blit(myhp1, [450, 350])
    mypower = font.render("power:"+str(power), True, (255,255,255))   
    screen.blit(mypower, [450, 400])
    po = font.render("potion:"+str(potion), True, (255,255,255))   
    screen.blit(po, [450, 450])


#画像一覧
Img=image("image/cha.png")
MapImg=image("image/grass.png")
MapImg1=image("image/next.png")
MapImg2=image("image/kabe.png")
MapImg3=image("image/next.png")
MapImg4=image("image/water.png")
MapImg5=image("image/taitoru5.png")
MapImg6=image("image/enemy0.png")

#主人公の描画
def drawgrass(screen):
    if map[y][x] == 4:
        return False
    if map1[y][x] == 4:
        return False
    if map2[y][x] == 4:
        return False
    screen.blit(Img,(x*GS,y*GS))

#音楽一覧
se = [pygame.mixer.Sound("sound/boss.mp3")]

#メイン処理
while True:
    drawtext()
    se[0].play()
    if idx==0:
        draw_map(screen)
        drawgrass(screen)
        pygame.display.update()
        if map[y][x] == 1:
            pygame.init()
            x=10
            y=2
            idx=1
        if map[y][x] == 4:
            pygame.init()
            screen.blit(MapImg5,(0,0))
            screen.blit(MapImg6,(260,210))
            text = font.render("ENEMY0", True, (255,255,255))   
            screen.blit(text, [245, 100])
            hp = font.render("HP:"+str(maxhp), True, (255,255,255))   
            screen.blit(hp, [245, 400])
            for i in range(3):
                COMMAND = ["[A]ttack", "[P]otion", "[R]un"]
                text = font.render(COMMAND[i],True, (255, 255, 255))
                screen.blit(text, [5, 150+i*60])
            
            for event in pygame.event.get():
                if event.type==QUIT:
                    sys.exit()
                if event.type == KEYDOWN:  # キーを押したとき
                    if event.key == K_r:
                        map[y][x]=0
                        draw_map(screen)
                        drawgrass(screen)
                        pygame.display.update()
                    if event.key == K_a:
                        dmg=power*2 + random.randint(3, 12)
                        maxhp -= dmg
                        myhp -= random.randint(10, 30)
                        pygame.display.update()
                        if maxhp <= 0:
                            map[y][x]=5
                            draw_map(screen)
                            drawgrass(screen)
                            pygame.display.update()
                            maxhp = 100
                            myhp += 10
                            power += 3
                            potion += 2
                        if myhp <= 0:
                            pygame.quit()
                            sys.exit()
                    if potion > 0:
                        if event.key == K_p:
                            myhp += 50
                            myhp -= random.randint(10, 30)
                            if myhp <= 0:
                                pygame.quit()
                                sys.exit()
                            potion -=1

    if idx==1:
        draw_map1(screen)
        drawgrass(screen)
        pygame.display.update()
        if map1[y][x] == 1:
            pygame.init()
            x=10
            y=12
            idx=0
        if map1[y][x] == 3:
            pygame.init()
            x=2
            y=7
            idx=2
        if map1[y][x] == 4:
            pygame.init()
            screen.blit(MapImg5,(0,0))
            screen.blit(MapImg6,(260,210))
            text = font.render("ENEMY0", True, (255,255,255))   
            screen.blit(text, [245, 100])
            hp = font.render("HP:"+str(maxhp), True, (255,255,255))   
            screen.blit(hp, [245, 400])
            for i in range(3):
                COMMAND = ["[A]ttack", "[P]otion", "[R]un"]
                text = font.render(COMMAND[i],True, (255, 255, 255))
                screen.blit(text, [5, 150+i*60])
            
            for event in pygame.event.get():
                if event.type==QUIT:
                    sys.exit()
                if event.type == KEYDOWN:  # キーを押したとき
                    if event.key == K_r:
                        map1[y][x]=0
                        draw_map1(screen)
                        drawgrass(screen)
                        pygame.display.update()
                    if event.key == K_a:
                        dmg=power*2 + random.randint(3, 12)
                        maxhp -= dmg
                        myhp -= random.randint(10, 30)
                        pygame.display.update()
                        if maxhp <= 0:
                            map1[y][x]=5
                            draw_map1(screen)
                            drawgrass(screen)
                            pygame.display.update()
                            maxhp = 100
                            myhp += 10
                            power += 3
                            potion += 2
                        if myhp <= 0:
                            pygame.quit()
                            sys.exit()
                    if potion > 0:
                        if event.key == K_p:
                            myhp += 50
                            myhp -= random.randint(10, 30)
                            if myhp <= 0:
                                pygame.quit()
                                sys.exit()
                            potion -=1

    if idx==2:
        draw_map2(screen)
        drawgrass(screen)
        pygame.display.update()
        if map2[y][x] == 3:
            pygame.init()
            x=17
            y=7
            idx=1
        if map2[y][x] == 4:
            pygame.init()
            screen.blit(MapImg5,(0,0))
            screen.blit(MapImg6,(260,210))
            text = font.render("ENEMY0", True, (255,255,255))   
            screen.blit(text, [245, 100])
            hp = font.render("HP:"+str(maxhp), True, (255,255,255))   
            screen.blit(hp, [245, 400])
            for i in range(3):
                COMMAND = ["[A]ttack", "[P]otion", "[R]un"]
                text = font.render(COMMAND[i],True, (255, 255, 255))
                screen.blit(text, [5, 150+i*60])
            
            for event in pygame.event.get():
                if event.type==QUIT:
                    sys.exit()
                if event.type == KEYDOWN:  # キーを押したとき
                    if event.key == K_r:
                        map2[y][x]=0
                        draw_map2(screen)
                        drawgrass(screen)
                        pygame.display.update()
                    if event.key == K_a:
                        dmg=power*2 + random.randint(3, 12)
                        maxhp -= dmg
                        myhp -= random.randint(10, 30)
                        pygame.display.update()
                        if maxhp <= 0:
                            map2[y][x]=5
                            draw_map2(screen)
                            drawgrass(screen)
                            pygame.display.update()
                            maxhp = 100
                            myhp += 10
                            power += 3
                            potion += 2
                        if myhp <= 0:
                            pygame.quit()
                            sys.exit()
                    if potion > 0:
                        if event.key == K_p:
                            myhp += 50
                            myhp -= random.randint(10, 30)
                            if myhp <= 0:
                                pygame.quit()
                                sys.exit()
                            potion -= 1
        
    #キーイベント
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()

        if event.type == KEYDOWN and event.key == K_DOWN:
            if is_movable(x, y+1):
                y += 1
        if event.type == KEYDOWN and event.key == K_LEFT:
            if is_movable(x-1, y):
                x -= 1
        if event.type == KEYDOWN and event.key == K_RIGHT:
            if is_movable(x+1, y):
                x += 1
        if event.type == KEYDOWN and event.key == K_UP:
            if is_movable(x, y-1):
                y -= 1
