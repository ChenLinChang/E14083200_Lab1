#引入模組RANDOM
import random
#介紹詞
print("Welcome to ROCK, PAPER, SCISSORS game !\n")
ties=0
lose=0
#遊戲迴圈
while 1:
    #使用者出拳
    move=str(input("Enter yout move: (r)ock (p)aper (s)cissors "))
    if move=='r':
        print('ROCK versus...\n')
    elif move=='p':
        print('Paper versus...\n')
    elif move=='s':
        print('SCISSORS versus...\n')
    #電腦隨機出拳,並比較勝負
    x=random.randint(1,3)
    if x==1:
        print('ROCK\n')
    elif x==2:
        print('Paper\n')
    elif x==3:
        print('SCISSORS\n')

    if x==1 and move=='r':
        print('It is a tie !')
        ties=ties+1
    elif x==1 and move=='p':
        print('You win !')
        break
    elif x==1 and move=='s':
        print('You loss !')
        loss=lose+1
    elif x==2 and move=='r':
        print('You loss !')
        loss=lose+1
    elif x==2 and move=='p':
        print('It is a tie !')
        ties=ties+1
    elif x==2 and move=='s':
        print('You win !')
        break
    elif x==3 and move=='p':
        print('You loss !')
        lose=loss+1
    elif x==3 and move=='s':
        print('It is a tie !')
        ties=ties+1
    elif x==3 and move=='r':
        print('You win !')
        break
#輸出結果
print('You have ',loss,' losses and ',ties,"ties before your first win.",sep="")
