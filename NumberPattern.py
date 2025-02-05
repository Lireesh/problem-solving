n=6
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print(n,end=" ")
        elif(i==1 or j==1 or j==n-2 or i==n-2):
            print(n-1,end=" ")
        else:
            print(n-2,end=" ")
    print()