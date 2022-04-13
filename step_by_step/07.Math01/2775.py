# 부녀회장이 퇼테야
import sys
input = sys.stdin.readline;

T = int(input())
for i in range(T):
    N = int(input())
    K = int(input())
    data=[i for i in range(1,K+1)]
    for j in range(N):
        for k in range(1,K):
            data[k]+=data[k-1]
    print(data[-1])

