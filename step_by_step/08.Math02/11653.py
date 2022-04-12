# 소인수분해
import sys
input = sys.stdin.readline;
n = int(input())
cnt=2;
data=[]
while n!=1:
    if n%cnt==0:
        data.append(cnt)
        n/=cnt;
    else:
        cnt+=1;
for i in data:
    print(i)