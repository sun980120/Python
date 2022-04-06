# 단어 정렬

import sys
input = sys.stdin.readline;
N = int(input())

data=[]
for i in range(N):
    data.append(input())
    
data_set = set(data)
data = list(data_set)

for i in range(len(data)):
    data[i] = data[i].strip('\n')

data.sort()
data.sort(key=lambda x:len(x))
for i in data:
    print(i)