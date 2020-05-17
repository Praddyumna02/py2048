import random
import sys
import copy
n=int(input("n="))
win=int(input("win="))
bsize=n
board=[]

#blank board 
for i in range(n):
    row=[]
    for j in range(n):
        row.append(0)
    board.append(row)
board[0][0]=2
    

#board current element
def output():
 for row in board:
     crow="  |  "
     for ele in row:
      if ele==0:
       crow+=" "+"  |  "
      else:
       crow+= str(ele)+ '  |  '
     print(crow)
output()
#making element as far as possible based on input

def left(newboard):
    for i in range(bsize):
        newboard[i]=merge(newboard[i])
        
    return newboard
    
def merge(row):
    for j in range(bsize-1):
     for i in range(bsize-1,0,-1):
        if row[i-1]==0:
            row[i-1]=row[i]
            row[i]=0
            
    for i in range(bsize-1):
        if row[i]==row[i+1]:
            row[i]+=row[i+1]
            row[i+1]=0
            
    for i in range(bsize-1,0,-1):
        if row[i-1]==0:
            row[i-1]=row[i]
            row[i]=0
    return row    
    

def reverse(row):
    new=[]
    for i in range(bsize-1,-1,-1):
        new.append(row[i])
    return new

def right(newboard): 
    for i in range(bsize):
     newboard[i]=reverse(newboard[i])
     newboard[i]=merge(newboard[i])
     newboard[i]=reverse(newboard[i]) 
    
    return newboard
     
def transpose(newboard):
    for i in range(bsize):
     for j in range(i,bsize):
        if i!=j:
            temp=newboard[i][j]
            newboard[i][j]=newboard[j][i]
            newboard[j][i]=temp
    return newboard
 
def up(newboard):
  
    newboard=transpose(newboard)
    newboard=left(newboard)
    newboard=transpose(newboard)
    
    return newboard
    
def down(newboard):
    
    newboard=transpose(newboard)
    newboard=right(newboard)
    newboard=transpose(newboard)
    
    return newboard

def lose():
    temp1=copy.deepcopy(board)
    temp2=copy.deepcopy(board)
    temp1=left(temp1)
    if temp1==temp2:
        temp1=right(temp1)
    if temp1==temp2:
        temp1=up(temp1)
    if temp1==temp2:
        temp1=down(temp1)
    if temp1==temp2:
        return True

def probability():
    if random.randint(1,9)==1:
        return 4
    else:
        return 2
    
condition=True   
while condition:
    for row in board:
     if win in row:
        print("YOU WON!")
        sys.exit()
   
    control=input("Enter buttons w for up, s for down, a for left, d for right  ") 
    if control=="w":
        up(board)
    elif control=="s":
        down(board)
    elif control=="a":
        left(board)
    elif control=="d":
        right(board)
    else:
        print("wrong key")
        sys.exit()
    
    randomrow=random.randint(0,n-1)
    randcolumn=random.randint(0,n-1)
    if board[randomrow][randcolumn]==0:
        board[randomrow][randcolumn]=probability()
    
    if lose():
        print("OUT OF MOVES")
        sys.exit()
   
    output()



    
