# 분수 찾기
import sys
input = sys.stdin.readline;

X=int(input())

line=1
while X>line:
    X-=line
    line+=1
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(str(a)+'/'+str(b))