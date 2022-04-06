# 좌표 정렬하기2

import sys
input = sys.stdin.readline;
N = int(input())
data=[]
for i in range(N):
    x,y=map(int,input().split())
    data.append([x,y])
data.sort()
b = sorted(data,key=lambda x : x[1])
for i in range(len(data)):
    print(b[i][0],b[i][1])