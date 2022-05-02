# 이항 계수 1
import sys
input = sys.stdin.readline;
import math

n,k = map(int,input().split())
print(math.comb(n,k), end='')