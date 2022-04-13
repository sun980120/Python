# ACM호텔
import sys
input = sys.stdin.readline;

T = int(input())
for i in range(T):
    x,y,z=0,0,1
    H,W,N = map(int,input().split())
    while True:
        # print(N)
        # print(x,y,z)
        if N>H:
            z+=1;
            N-=H;
        else:
            x=N;
            break;
    print(x*100+y*10+z*1)