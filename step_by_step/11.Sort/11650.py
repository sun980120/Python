# 좌표 정렬하기

import sys
input = sys.stdin.readline;
N = int(input())
data=[]
for i in range(N):
    x,y=map(int,input().split())
    data.append([x,y])
data.sort()
for i in range(len(data)):
    print(data[i][0],data[i][1])