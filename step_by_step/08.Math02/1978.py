# 소수 찾기
import sys
input = sys.stdin.readline;
n = int(input())
data = list(map(int,input().split()))
cnt=0

for i in data:
    if i == 1:
        continue;
    elif i == 2:
        cnt += 1;
    else :
        for j in range(2,i):
            if i%j==0:
                break;
        if j+1 == i:
            cnt+=1;
print(cnt)