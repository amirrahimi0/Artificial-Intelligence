import numpy as np
sudoku = [[0 for j in range(9)] for i in range(9)]
empty = []
domainforeachrow=[list(range(1,10)) for i in range(1,10)]
domainforeachcollum=[list(range(1,10)) for i in range(1,10)]
domainforeachbox=[list(range(1,10)) for i in range(1,10)]

def boxnumber(row, col):
        return row // 3 * 3 + col // 3
        
def domainfinder(sudoku):
    global domainforeachbox,domainforeachcollum,domainforeachrow
    domainforeachrow=[list(range(1,10)) for i in range(1,10)]
    domainforeachcollum=[list(range(1,10)) for i in range(1,10)]
    domainforeachbox=[list(range(1,10)) for i in range(1,10)]
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                continue
            try:
                domainforeachrow[i].remove(sudoku[i][j])
            except:
                print ("invalid board")
                exit()
            
    for j in range(9):
        for i in range(9):
            if sudoku[i][j]==0:
                continue
            try:
                domainforeachcollum[j].remove(sudoku[i][j])
            except:
                print ("invalid board")
                exit()
    for i in range(9):
        firstrow = i // 3 * 3
        firstcol = i % 3 * 3
        for j in range(firstrow, firstrow + 3):
            for k in range(firstcol, firstcol + 3):
                if sudoku[j][k]==0:
                    continue
                try:
                    domainforeachbox[i].remove(sudoku[j][k])
                except:
                    print ("invalid board")
                    exit()

def get_domain(i,j):
    domain=set(domainforeachrow[i])
    domain.intersection_update(set(domainforeachcollum[j]))
    domain.intersection_update(set(domainforeachbox[boxnumber(i,j)]))
    return list(domain)


def get_min_domain(sudoku):
    mindomainrow=-1
    mindomaincol=-1
    min_size=10
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                n=len(get_domain(i,j))
                if n< min_size:
                    mindomainrow=i
                    mindomaincol=j
                    min_size=n
    if min_size==10:
        return None
    return mindomainrow,mindomaincol
        
def is_valid(sudoko):
    for i in range(9):
        for j in range(9):
            if len(get_domain(i,j))==0 and sudoko[i][j]==0:
                return False
    return True

def sudoku_solver (sudoku):
  
   x=get_min_domain(sudoku)
   if x==None:
       print(sudoku)
       return True
   domain=get_domain(x[0],x[1])
   for i in domain:
    
       sudoku[x[0]][x[1]]=i
       domainfinder(sudoku)
       if is_valid(sudoku):
           res=sudoku_solver(sudoku)
           if res:
               return True
       sudoku[x[0]][x[1]]=0
       domainfinder(sudoku)
   return False
           

   


    





for i in range(9):
    row_input = input("Enter row number %d: " % (i+1))
    row_values = row_input.split(" ")
    
    for j in range(9):
        val = int(row_values[j])
        sudoku[i][j] = val
domainfinder(sudoku)
a=sudoku_solver(sudoku)
print(a)

