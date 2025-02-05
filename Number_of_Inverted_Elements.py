#arrays
A=[10,20,30,40]
B=[10,40,20,30]
count=0
for i in range(len(A)):
    for j in range(len(B)):
        if(A[i]==B[j]):
            if(i==j):
                continue
            else:
                temp=B[j]
                B[j]=B[i]
                B[i]=temp
                count+=1
print(count%3+1)