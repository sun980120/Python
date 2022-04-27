# 이항 계수 2
import sys
input = sys.stdin.readline;
import math

n,k = map(int,input().split())
print(math.comb(n,k)%10007, end='')