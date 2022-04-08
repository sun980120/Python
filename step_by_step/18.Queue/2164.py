# 카드 2
import sys
input = sys.stdin.readline;
from collections import deque

queue = deque([])

n = int(input())
for i in range(1,n+1):
    queue.append(i)
while True:
    if len(queue)==1:
        break;
    queue.popleft()
    a = queue.popleft()
    queue.append(a)
print(queue[0])