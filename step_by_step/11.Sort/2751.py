# 수 정렬하기 2
import sys
input = sys.stdin.readline

data_list = []
n = int(input())
for i in range(n):
    data_list.append(int(input()))
data_list.sort()
for i in data_list:
    print(i)