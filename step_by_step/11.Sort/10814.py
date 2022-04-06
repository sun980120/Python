# 나이순 정렬
import sys
input = sys.stdin.readline;
x = int(input())
data=[]
for i in range(x):
    n,m = map(str,input().split());
    data.append([int(n),m])
    
b = sorted(data,key=lambda x : x[0])
for i,j in b:
    print(i,j)
