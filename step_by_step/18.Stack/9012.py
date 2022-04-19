# 괄호
import sys
input= sys.stdin.readline;


T = int(input())
for i in range(T):
    data = input()
    data = data.strip('\n')
    stack = []
    a=0
    for j in data:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack)==0:
                a += 1;
            else:
                stack.pop()
    if a!=0:
        print('NO')
    elif a==0:
        if len(stack)!=0:
            print('NO')
        else :
            print('YES')