import random
def evolve(x):
    global j
    index = random.randint(0, len(x)-1)
    #a random index no in list x
    p= random.randint(1,100)
    if (p==1):
        if(x[index]=='0'):
            x[index]='1'
        else:
            x[index]='0'
                


with open("DNA_code.txt") as myfile:
    x=myfile.read()
    x=list(x)
for i in range(0,10000):
    evolve(x)
print(x)
    