# 요세푸스 문제 0
import sys
input = sys.stdin.readline;
from collections import deque

queue=deque([])
n,m = map(int,input().split())
for i in range(1,n+1):
    queue.append(i)
print('<',end='')
while queue:
    for j in range(m-1):
        queue.append(queue[0])
        queue.popleft();
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
print('>')