# 직각삼각형
import sys
input = sys.stdin.readline

while True:
    check=0
    x,y,z = map(int,input().split())
    if x==y==z==0:
        break;
    if x**2 == y**2 + z**2:
        print('right')
    elif y**2 == x**2 + z**2:
        print('right')
    elif z**2 == y**2 + x**2:
        print('right')
    else:
        print('wrong')