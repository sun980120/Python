# 스택
import sys
input = sys.stdin.readline

n = int(input())
stack = []

def push(x):
    stack.append(x);

def top():
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])

def pop():
    if len(stack) == 0:
        print(-1);
    else:
        print(stack.pop());

def size():
    print(len(stack))

def empty():
    if len(stack)==0:
        print(1)
    else:
        print(0)

for i in range(n):
    a = sys.stdin.readline().split();
    if(a[0]=='push'):
        push(a[1]);
    elif a[0]=='top':
        top();
    elif a[0]=='size':
        size();
    elif a[0]=='empty':
        empty();
    elif a[0]=='pop':
        pop();