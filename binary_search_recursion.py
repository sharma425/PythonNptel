def binary_search(l,x,start,end):
    #base case is 1 element
    if start == end:
        if l[start] ==x:
            return start
        else:
            return -1
    else:
        #divide th array into halves
        mid =(start+end)//2
        if l[mid]==x:
            return mid
        elif l[mid] > x :
            return binary_search(l, x, start, mid-1)
        else:
            return binary_search(l, x, mid+1, end)
            
            


l=[]        
for i in range(101):
    l.append(i)
print(l)
x=input("Enter the number to find : ")
result = binary_search(l,int(x) , 0, len(l))
if result==-1:
    print(x,"not found")
else:    
    print(x," is found at index :" ,result+1)