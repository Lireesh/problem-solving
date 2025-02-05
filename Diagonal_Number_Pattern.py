n=5
list1=[[0]*n for i in range(n,0,-1)]
number=1
list1[0][0]=number
number+=1
row=0
def printpattern(i,j,number,row):
    if(row>n):
        return
    if(j>=0 and j<n and i<n):
        list1[i][j]=number
        return printpattern(i+1,j-1,number=number+1,row=row)
    elif(j<0 and i<n):
        return printpattern(0,j=i,number=number,row=row)
    else:
        row+=1
        return printpattern(i=row,j=4,number=number,row=row)
        
    
printpattern(0,1,number,row)

for i in range(n):
    for j in range(n):
        print(list1[i][j],end="   ")
    print()
    print()