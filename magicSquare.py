# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:04:28 2021

@author: Keshav
"""

def magic_square(n):
    magicSquare = []
    
    #initializing magic square to all 0
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
    i=n//2
    j=n-1
    num = n*n #total no of blocks
    count = 1 # my elements
    while (count<=num):
        if (i==-1 and j==n):     # condition 4
            i=0;j=n-2
        else:
            if(j==n):       # column is exceeding
                j=0
            if(i<0):         #row is becoming -1
                i=n-1
        if (magicSquare[i][j]!=0):
            i=i+1
            j=j-2
            continue        #for checking above conditions again
        else:  
            magicSquare[i][j]=count
            count+=1
            i=i-1
            j=j+1
            
        
    #printing the magic square
    for i in range(n):
        for j in range(n):
            print(f'{magicSquare[i][j]:5}',end="")
        print()
    print("The sum of each row/column/diagonal is : "+str((n*(n**2+1))/2) )
    

magic_square(13)