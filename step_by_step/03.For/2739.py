# 구구단

n = int(input())

for i in range(1,10):
    print(n, end=' ')
    print("*",end=' ')
    print(i,end=' ')
    print("=",end=' ')
    print(n * i)