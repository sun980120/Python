# 약수
import sys
input = sys.stdin.readline;
N = int(input())
data_list = list(map(int,input().split()))
data_list.sort()
if len(data_list) == 1:
    print(data_list[0]*2,end='')
else:
    print(data_list[0]*data_list[-1],end='')