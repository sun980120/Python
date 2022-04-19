# 큐 2
import sys
input = sys.stdin.readline;
from collections import deque

queue=deque([])
n = int(input())

def push(x):
    queue.append(x)
def front():
    if not len(queue):
        print(-1)
    else:
        print(queue[0])
def back():
    if not len(queue):
        print(-1)
    else:
        print(queue[len(queue)-1])
def empty():
    if not len(queue):
        print(1)
    else:
        print(0)
def size():
    print(len(queue))
def pop():
    if not len(queue):
        print(-1)
    else:
        print(queue.popleft())

for i in range(n):
    a = input().split()
    if a[0]=='push':
        push(a[1]);
    elif a[0]=='front':
        front();
    elif a[0]== 'back':
        back();
    elif a[0]== 'empty':
        empty();
    elif a[0]== 'size':
        size();
    elif a[0] == 'pop':
        pop();