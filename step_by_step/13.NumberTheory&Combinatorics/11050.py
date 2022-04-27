# 이항 계수 1
import sys
input = sys.stdin.readline;
import math

n,k = map(int,input().split())
data = math.comb(n,k)%10007
print(data, end='')