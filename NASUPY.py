import pygame
import os,json,time,random

if not os.path.exists('save.json'):
    with open('save.json','w') as f:
        f.write("{\"highscore\": 0}")
pygame.init();
pygame.mixer.init();
screen=pygame.display.set_mode(size=(600,438));
from pygame import image,mixer
Border=image.load('assets/waku.png')
Title=image.load('assets/title.png')
Nasu=image.load('assets/nasu.png')
Akanasu=image.load('assets/akanasu.png')
Getting=image.load('assets/getting.png')
START=image.load('assets/START.png')
Char=image.load('assets/char.png')
Char2=image.load('assets/char2.png')
CharGt=image.load('assets/char-getting.png')
Char2Gt=image.load('assets/char2-getting.png')
Bg=image.load('assets/bg.png')
Bg2=image.load('assets/bg2.png')
Font1=image.load('assets/1.png')
Font2=image.load('assets/2.png')
Font3=image.load('assets/3.png')
Font4=image.load('assets/4.png')
Font5=image.load('assets/5.png')
Font6=image.load('assets/6.png')
Font7=image.load('assets/7.png')
Font8=image.load('assets/8.png')
Font9=image.load('assets/9.png')
Font0=image.load('assets/0.png')
lst={}
with open('save.json','r') as f:
        lst=json.load(f)
        highScore=str(lst['highscore'])
score=0
timer=0
initSpeed = -15
accel = 1
CurrentPos=(270,304)
CurrentChar=Char
CurrentNasu=Nasu
NasuY=24
nasuTimer=0
randXPos=200
AkanasuScore=random.randint(20,30)
        
fontDic={'1':Font1,'2':Font2,'3':Font3,'4':Font4,'5':Font5,'6':Font6,'7':Font7,'8':Font8,'9':Font9,'0':Font0}

isPressedEnter=False
isPlayedTitle=False
isPlayedGaming=False
isJumping=False
isJumpedHighest=False
isNasuFloating=False
isLeft=False
while True:
    time.sleep(0.02)

    if isPressedEnter:
        if not isPlayedGaming:
            mixer.music.load('assets/audio/bgm-gaming.wav')
            mixer.music.play(-1,0)
            isPlayedGaming=True
        screen.blit(Border,(0,0))
        screen.blit(Bg,(24,24))
        screen.blit(CurrentChar,CurrentPos)
        i=0
        for char in str(score):
            screen.blit(fontDic[char],(467+24*i,383))
            i=i+1
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if CurrentPos[0]>0:
                x,y=CurrentPos
                x=x-4
                CurrentPos=x,y
                isLeft=True
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if CurrentPos[0]<519:
                x,y=CurrentPos
                x=x+4
                CurrentPos=x,y
                isLeft=False
        if pygame.key.get_pressed()[pygame.K_SPACE] and not isJumping:
            speed = initSpeed
            isJumping=True
        if isJumping:
            x,y = CurrentPos
            y += speed
            speed += accel
            CurrentPos = x,y
            if speed > 15:
                isJumping = False
        if isNasuFloating:
            screen.blit(CurrentNasu,(randXPos,NasuY))
            NasuY=NasuY+3
        else:
            nasuTimer=nasuTimer+1
            if nasuTimer>30:
                isNasuFloating=True
                randXPos=random.randint(20,532)
                CurrentNasu=Nasu if random.random()>0.2 else Akanasu
        if abs(CurrentPos[0]+24-randXPos)<20 and abs(CurrentPos[1]+24-NasuY)<20 and isJumping and not isJumpedHighest:
            isNasuFloating=False
            NasuY=24
            nasuTimer=0
            score=score+AkanasuScore if CurrentNasu == Akanasu else score+random.randint(10,23)
            if CurrentNasu==Akanasu:
                AkanasuScore=round(AkanasuScore*1.1+random.randint(5,10))
        if NasuY>414:
            if score>int(highScore):
                lst['highscore']=score
                with open('save.json','w') as f:
                    f.write(json.dumps(lst))
                print(f"{score}!RECORD BREAKING!")
            else:
                print(f'{score}!')
            pygame.quit()
            break
        if isJumping:
            if isLeft:
                CurrentChar=CharGt
            else:
                CurrentChar=Char2Gt
        else:
            if isLeft:
                CurrentChar=Char
            else:
                CurrentChar=Char2

        
    else:
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            mixer.music.stop()
            
            isPressedEnter=True
        screen.blit(Border,(0,0))
        screen.blit(Title,(24,24))
        i=0
        for char in highScore:
            screen.blit(fontDic[char],(362+24*i,318))
            i=i+1
        
        if not isPlayedTitle:
            mixer.music.load('assets/audio/bgm-title.wav')
            mixer.music.play(-1,0)
            isPlayedTitle=True
    pygame.display.flip()
    for evt in pygame.event.get():
            if evt.type==pygame.QUIT:
                os._exit(0)

print("Press ENTER to exit...")
import platform
if platform.system()=="Windows":
    input()

