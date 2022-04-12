# 소수
import sys
input = sys.stdin.readline;
sum_data=0
min_data=999
n = int(input())
m = int(input())
data=[]
for i in range(n, m+1):
    if i == 1:
        continue;
    elif i == 2:
        data.append(2)
    else :
        for j in range(2,i):
            if i%j==0:
                break;
        if j+1 == i:
            data.append(i)

if len(data)!=0:
    print(sum(data))
    print(min(data))
else:
    print(-1)