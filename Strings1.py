t=input()  #a1b2c3
letter=[t[i] for i in range(0,len(t),2)]
num=[t[i] for i in range(1,len(t),2)]
for i in range(len(num)):
    print(letter[i]*int(num[i]),end='')
# output abbcc