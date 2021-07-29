import random
import turtle
turtle.bgcolor("black")
seurat = turtle.Turtle()
widtg =5 
height =7
dot_distance = 25
seurat.setpos(-250,250)

seurat.penup()      #up the pen not draw a line
list_color=["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]

def col():
    return random.randint(0,10 )

def spiral(m,n):
    f=0
    #m is no of rows m is no of rows and a is list of list
    r=0;c=0
    #k=index of starting row    
    #l=index of starting column
    while(r<m and c<n):
        if(f==1):
            seurat.right(90)
        
        seurat.color(list_color[col()])
        #printing the first row from remaning rows
        for i in range(c,n):
            seurat.dot()
            seurat.forward(dot_distance)
            
        r+=1
        f=1
        seurat.right(90)
        
        for i in range(r,m):
            seurat.dot()
            seurat.forward(dot_distance)
            
        n-=1
        seurat.right(90)
        
        
        if(r<m):
            for i in range(n-1,c-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                
            m-=1
            
        seurat.right(90)
        
        if(c<n):
            
            for i in range(m-1,r-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                
            c+=1
     
                
        
        
spiral(20, 20)