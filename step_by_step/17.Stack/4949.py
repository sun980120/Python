# 균형잡힌 세상
import sys
input = sys.stdin.readline;

while True: 
    N = input();
    if N[0]=='.' and len(N):
        break;
    a=0;
    stack=[]
    for i in N:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if len(stack)==0:
                a+=1;
            elif len(stack)!=0 and stack[-1]=='(':
                stack.pop();
            elif len(stack)!=0 and stack[-1]!='(':
                a+=1;
        elif i==']':
            if len(stack)==0:
                a+=1;
            elif len(stack)!=0 and stack[-1]=='[':
                stack.pop();
            elif len(stack)!=0 and stack[-1]!='[':
                a+=1;
 
    if a!=0:
        print('no')
    elif a==0:
        if len(stack)!=0:
            print('no')
        else :
            print('yes')