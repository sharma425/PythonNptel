import random
doors = [0]*3
goatdoor = [0]*2
swap = 0        #no of swaps wins
dont_swap=0         #no of dont swaps wins
for i in range(40):
    x=random.randint(0,2)   #xth door will comprise of BMW
    doors[x]='BMW'
    for i in range(0,3):
        if (i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoor.append(i)
    choice = int(input("Enter Your Choice"))
    door_open = random.choice(goatdoor) #open a door that comprises of goat
    while(door_open == choice):  #door_open should'nt be equal to choice made by the participant
        door_open = random.choice(goatdoor)
    ch = input("do you esnt to swap")
    if (ch=='y'):
        if(doors[choice]=='Goat'):
            print("Player wins")
            swap=swap+1
        else:
            print("player lost")
    else:
        if(doors[choice]=='Goat'):
            print("Player lost")
           
        else:
            print("player win")
            dont_swap+=1
            
            
print(swap)
print(dont_swap)