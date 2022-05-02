# 팩토리얼 0의 개수
import sys,math
input = sys.stdin.readline;

n = int(input())
data = math.factorial(n)
cnt=0;
for i in reversed(str(data)):
    if int(i) == 0:
        cnt+=1;
    else:
        break;
print(cnt,end='')