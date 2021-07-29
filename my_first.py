import random
def play():
    p1name=input("player 1 please input your name : ")
    p2name=input("player 2 please input your name : ")
    pp1 = 0
    pp2 = 0
    #player 1
    turn=0
    while(1):
        #computers task
        picked_word= choose()
        #create question
        qn=jumble(picked_word)
        print (qn)
        if turn%2==0:
            print(p1name,"This is your turn")
            ans = input("What is on your mind : ")
            if ans == picked_word:
                pp1+=1
                print("Your Score is :",pp1)
            else:
                print("Brtter luck next time. I thought : ",picked_word)
            c=int(input("press 1 to continue and 0 for quit : "))
            print (c)
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        #player 2
        else:
            print(p2name,"This is your turn")
            ans = input("What is on your mind : ")
            if ans == picked_word:
                pp2+=1
                print("Your Score is :",pp2)
            else:
                print("Brtter luck next time. I thought : ",picked_word)
            c=int(input("press 1 to continue and 0 for quit : "))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn+=1
def thank(p1name,p2name,pp1,pp2):
    print(p1name,"score is :",pp1)
    print(p2name,"score is :",pp2)
def choose():
    words=['rainbow','computer','science','programming','player','condition','reverse','water','board']
    pick = random.choice(words)
    return pick
def jumble(word):
    jumbled_word = "".join(random.sample(word, len(word)))
    return jumbled_word
play()