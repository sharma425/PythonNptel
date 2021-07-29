def ladder(p):
    if p==1:
        p=38
    elif p==4:
        p=14
    elif p==8:
        p=30
    elif p==21:
        p=42
    elif p==28:
        p=74
    elif p==50:
        p=67
    elif p==71:
        p=92
    elif p==80:
        p=99
    return p
     
def snake(p):
    if p==63:
        p=18
    elif p==36:
        p=6
    elif p==32:
        p=10
    elif p==88:
        p=24
    elif p==95:
        p=56
    elif p==97:
        p=78
    elif p==48:
        p=26
    elif p==89:
        p=13
    return p
   
        


from PIL import Image
import random

def show_board():
    img = Image.open('snakeladder.jpg')
    img.show()
    
def print_position(pp1,pp2):
    print("Player 1 position is :",pp1)    
    print("Player 2 position is :",pp2)    
    
    

def play():
    p1_name = input('Player 1 Please Enter Your Name : ')
    p2_name = input('Player 2 Please Enter Your Name : ')
    pp1=0
    pp2=0
    turn = 0
    while(1):
        if turn%2 == 0:
            print(p1_name,"player 1 turn : Press enter for roll the dice ")
            input()
            dice = random.randint(1,6)
            print("Dice Shown : ",dice)
            pp1=pp1+dice
            pp=snake(pp1)
            pp=ladder(pp1)
            if pp1 < pp:
                print("Congrats ! you climbed a ladder")
            elif pp1 > pp:
                print("OOPS ! you have biten by a snake")
            pp1=pp
            turn+=1
            if pp1>end :
                print(p1_name," won")
                break
            print_position(pp1,pp2)
            show_board()
        else:
                        
            print(p2_name," turn : Press enter for roll the dice ")
            input()
            dice = random.randint(1,6)
            print("Dice Shown : ",dice)
            pp2=pp2+dice
            pp=snake(pp2)
            pp=ladder(pp2)
            if pp2 < pp:
                print("Congrats ! you climbed a ladder")
            elif pp2 > pp:
                print("OOPS ! you have biten by a snake")
            pp2=pp
            turn+=1
            if pp2>end :
                print(p2_name," won")
                break
            print_position(pp1,pp2)
                
    
end =100
show_board()
play()