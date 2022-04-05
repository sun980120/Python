# 수 정렬하기 3
import sys
input = sys.stdin.readline

data_list = [0] * 10001
n = int(input())
for i in range(n):
    data_list[int(input())] += 1;
for i in range(10001):
    if data_list[i] != 0:
        for j in range(data_list[i]):
            print(i)