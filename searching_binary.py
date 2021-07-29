def linear_search(a,x):
    
    flag =0
    for i in a :
        if (i==x):
            print("yes !! found my number at position",str(i))
            flag =1
            break
    if (flag==0):
        print("Number not found")


def binary_search(a,x):
    first_pos = 0
    last_pos = len(a)-1
    flag = 0
    while(first_pos<=last_pos and flag == 0):
        mid_pos = (first_pos + last_pos)//2
        if(a[mid_pos]==x):
            flag=1
            print("The element present in position: "+str(mid_pos))
        elif(a[mid_pos]<x):
            first_pos = mid_pos
        else:
            last_pos = mid_pos
            
        print(mid_pos)
    if (flag == 0):
        print("your number is not present in list")
        
a=[]        
for i in range(1000001):
    a.append(i)
#linear_search(100000000,67)

print(a)
#binary_search(a, 88)