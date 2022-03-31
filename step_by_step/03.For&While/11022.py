# A+B-8

n = int(input())
for i in range(1,n+1):
    a,b = map(int,input().split())
    print("Case #"+str(i)+":",end=' ')
    print(str(a)+" + "+str(b)+" = ",end='')
    print(a+b)