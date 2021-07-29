import random
import matplotlib.pyplot as plt
x=[]
y=[]



account = 0
i=1
while i<=365 :
    x.append(i)
    i+=1
    bet = random.randint(0, 5)
    #bet = int(input("Your bet from 1 to 10 : "))
    lucky_draw=random.randint(0, 5)
    print(lucky_draw)
    if bet == lucky_draw:
        account = account + 900 -100#100 is money spent for this game
        print("Congrets you won")
    else:
        account = account - 100
        print("sorry ! you loose")
    y.append(account)
    print("Your balance is ",account)
    
    
plt.plot(x, y)
plt.show()