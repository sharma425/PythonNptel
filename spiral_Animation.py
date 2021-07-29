# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:13:35 2021

@author: Keshav
"""
import turtle
turtle.bgcolor("black")
seurat = turtle.Turtle()
widtg =5 
height =7
dot_distance = 25
seurat.setpos(-250,250)




def spiral(m,n):
    seurat.color("yellow")
    f=0
    
    
    
    
    #m is no of rows m is no of rows and a is list of list
    r=0;c=0
    #k=index of starting row    
    #l=index of starting column
    while(r<m and c<n):
        if(f==1):
            seurat.right(90)
        
       
        #printing the first row from remaning rows
        for i in range(c,n):
            seurat.forward(dot_distance)
            #print(a[r][i],end= " ")
        r+=1
        f=1
        seurat.right(90)
        #printing last column from remaining column
        for i in range(r,m):
            seurat.forward(dot_distance)
            #print(a[i][n-1],end= " ")
        n-=1
        seurat.right(90)
        
        if(r<m):
            for i in range(n-1,c-1,-1):
               seurat.forward(dot_distance)
                #print(a[m-1][i],end= " ") 
            m-=1
        seurat.right(90)
        if(c<n):
            
            for i in range(m-1,r-1,-1):
                seurat.forward(dot_distance)
                #print(a[i][c],end=' ')
            c+=1
        print("hello")
                
        
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#print(a[3][2])
spiral(20, 20)