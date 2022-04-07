# 더하기 사이클
import math

n = int(input())
m = n
cnt = int(0)

while True:
    a = m // 10
    b = m % 10
    c = (a+b)%10
    m = (b*10)+c
    cnt = cnt + 1
    if m == n:
        break;
    
print(cnt)