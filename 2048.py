import pygame
import random
import copy

WIDTH=600
HEIGHT=600
Chance2=0.8
Chance4=1-Chance2
Game_Over=False
WHITE=(255,255,255)
UP=0
RIGHT=1
DOWN=2
LEFT=3

ColourDic={
    1:(255,153,204),
    2:(153,153,255),
    3:(153,255,255),
    4:(153,255,153),
    5:(204,255,153),
    6:(255,255,153),
    7:(255,204,253),
    8:(255,153,153),
    9:(255,102,102),
    10:(255,0,0),
    11:(153,0,0),
    12:(102,0,0)
}
pygame.font.init()

text=pygame.font.Font(None,40).render("hahaha",False,(0,0,0))
Board=[]
for x in range(4):
    Board.append([0,0,0,0])

def Addnum(Board,Chance2,Chance4):
    emptyList=[]
    for r in range(len(Board)):
        for c in range(len(Board[0])):
            if Board[r][c]==0:
                emptyList.append([r,c])
    ranpos=emptyList[random.randint(0,len(emptyList)-1)]
    i=random.random()
    if i<=Chance2:
        ranIn=1
    else:
        ranIn=2
    Board[ranpos[0]][ranpos[1]]=ranIn
    print(Board)

def drawBlock(Board):
    for r in range(len(Board)):
        for c in range(len(Board[0])):
            if Board[r][c] is not 0:
                index=Board[r][c]
                rect=pygame.Rect(c*int(WIDTH/4),r*int(HEIGHT/4),int(WIDTH/4),int(HEIGHT/4))
                text=str(2**Board[r][c])
                num=pygame.font.Font(None,80).render(text,True,(255,255,255))
                
                block=pygame.Surface((int(WIDTH/4),int(HEIGHT/4)))
                block.fill(ColourDic[index])
                SCREEN.blit(block,rect)
                SCREEN.blit(num,rect)
                
                

def checkNext(selfIn,nextIn):
    if nextIn==0:
        return True
    elif nextIn==selfIn:
        return True
    else:
        return False

def moveBlock(Board,direction):
    
    if direction==LEFT:
        for r in range(len(Board)):
            for c in range(len(Board[0])):
                if Board[r][c]==0:
                    continue
                Combined=False
                for t in range(c):
                    if Board[r][c-t-1]==0:
                        Board[r][c-t-1]=Board[r][c-t]+0
                        Board[r][c-t]=0
                    elif Board[r][c-t-1]==Board[r][c-t] and not Combined:
                        Board[r][c-t-1]=Board[r][c-t]+1
                        Board[r][c-t]=0
                        Combined=True
                    else:
                        break

    if direction==RIGHT:
        for r in range(len(Board)):
            c=len(Board)-1
            while c>=0:
                Combined=False
                for t in range(len(Board)-1-c):
                    if Board[r][c+t+1]==0:
                        Board[r][c+t+1]=Board[r][c+t]+0
                        Board[r][c+t]=0
                    elif Board[r][c+t+1]==Board[r][c+t] and not Combined:
                        Board[r][c+t+1]=Board[r][c+t]+1
                        Board[r][c+t]=0
                        Combined=True
                    else:
                        break
                c-=1
    if direction==UP:
        for c in range(len(Board[0])):
            for r in range(len(Board)):
                Combined=False
                for t in range(r):
                    if  Board[r-t-1][c]==0:
                        Board[r-t-1][c]=Board[r-t][c]+0
                        Board[r-t][c]=0
                    elif Board[r-t-1][c]==Board[r-t][c] and not Combined:
                        Board[r-t-1][c]=Board[r-t][c]+1
                        Board[r-t][c]=0
                        Combined=True
                    else:
                        break
    if direction==DOWN:
        for c in range(len(Board[0])):
            r=len(Board[0])-1
            while r>=0:
                Combined=False
                for t in range(len(Board[0])-1-r):
                    if Board[r+t+1][c]==0:
                        Board[r+t+1][c]=Board[r+t][c]
                        Board[r+t][c]=0
                    elif Board[r+t+1][c]==Board[r+t][c] and not Combined:
                        Board[r+t+1][c]=Board[r+t][c]+1
                        Board[r+t][c]=0
                        Combined=True
                    else:
                        break
                r-=1


pygame.display.init()
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048")

def drawBackgroundLines():
    for x in range(1,4):
        pygame.draw.line(SCREEN,WHITE,[0,x*int(HEIGHT/4)],[WIDTH,x*int(HEIGHT/4)])
        pygame.draw.line(SCREEN,WHITE,[x*int(WIDTH/4),0],[x*int(WIDTH/4),HEIGHT])

Addnum(Board,Chance2,Chance4)

while not Game_Over:
    SCREEN.fill((0,0,0))
    drawBlock(Board)
    drawBackgroundLines()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Game_Over=True
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                direction=UP
                temp=copy.deepcopy(Board)
                moveBlock(Board,direction)
                if not Board==temp:
                    Addnum(Board,Chance2,Chance4)
            elif event.key==pygame.K_DOWN:
                direction=DOWN
                temp=copy.deepcopy(Board)
                moveBlock(Board,direction)
                if not Board==temp:
                    Addnum(Board,Chance2,Chance4)
            elif event.key==pygame.K_LEFT:
                direction=LEFT
                temp=copy.deepcopy(Board)
                moveBlock(Board,direction)
                if not Board==temp:
                    Addnum(Board,Chance2,Chance4)
            else:
                direction=RIGHT
                temp=copy.deepcopy(Board)
                moveBlock(Board,direction)
                if not Board==temp:
                    Addnum(Board,Chance2,Chance4)
            
    
    pygame.display.flip()
    
        
