import string
flames = {'f':'friend','l':'love','a':'affirmative','m':'marriage','e':'enemy','s':'sister'}
p1=list(input("Please Input Your Name : ").lower().replace(" ", ""))
p2=list(input("Please Input Your Name : ").lower().replace(" ", ""))
def remove_matching_letters():
    for i in p1:
        for j in p2:
            if (i==j):
                p1.remove(j)
                p2.remove(j)
                return True
            
    return False

def find_relation(n):
    
    s=list("flames")
    count =0
    while True:
        index = 0
        while (index < len(s)):
            if count == n:
                s.remove(s)
                count = 0
            else:
                count +=1
            index+=1
        
            
                                  
                
proceed = True
while proceed:
    proceed = remove_matching_letters()

my_number = len(p1)+len(p2)

s=find_relation(my_number)
print(my_number)
print(p1)
print(p2)
print(s)