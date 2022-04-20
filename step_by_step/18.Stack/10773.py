# 제로
import sys
input = sys.stdin.readline;

stack = []
K = int(input())
for i in range(K):
    N = int(input())
    if N==0:
        stack.pop();
    else:
        stack.append(N)
print(sum(stack))