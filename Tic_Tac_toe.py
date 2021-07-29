import numpy

            
            
board = numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p1s = 'X'
p2s = 'O'
def check_rows(symbol):
    print(symbol)
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count == 3:
            return True
    return False

def check_column(symbol):
    print(symbol)
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count == 3:
            return True
    return False

def check_diagonals(symbol):
    print(symbol)
    count = 0
    for d in range(3):
        if board[d][d]==symbol:
            count+=1
        if count==3:
             return True
    r=0;c=2;count=0
    while (r <3 and c>=0):
        if board[d][d]==symbol:
            count+=1
        r+=1;c-=1
        if count==3:
            return True
    return False
        
        
       


def won(symbol):
    return check_rows(symbol)or check_column(symbol)or check_diagonals(symbol)
    
    
    
def place(symbol):
    while(True):
        print(numpy.matrix(board))
        row= int(input("Choose your row position 1 or 2 or 3 : "))
        column= int(input("Choose your column position 1 or 2 or 3 : "))
        
        if row > 0 and row < 4 and column > 0 and column <4 and board[row-1][column-1]=='_':
            board[row-1][column-1]=symbol
            break
            
        else:
            print("Invalid Input. Please enter again")
        

def play():
    for turn in range(9):

        if turn%2 ==0 :
            print('X turn')
            place(p1s)
            if won(p1s):
                print(p1s,"won")
                break
        else:
            print('O turn')
            place(p2s)
            if won(p2s):
                print(p2s,"Won")
                break
    if not (won(p1s)) and not (won(p2s)):
        print('Draw')


play()