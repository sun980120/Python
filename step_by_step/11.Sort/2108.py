# 통계학

import sys
import math
from collections import Counter
input = sys.stdin.readline;
n = int(input())
data_list=[]
for i in range(n):
    data_list.append(int(input()))
data_list.sort()
cnt = Counter(data_list)
mode = cnt.most_common(len(cnt))
max_mode = 0
max_cnt = 0
for i in range(len(cnt)):
    if max_mode < mode[i][1]:
        max_mode = mode[i][1]
for i in range(len(cnt)):
    if max_mode == mode[i][1]:
        max_cnt += 1;
    
# print(math.ceil(sum(data_list)/n))
print(round(sum(data_list)/n))
print(data_list[n//2])
if max_cnt>1:
    print(mode[1][0])
else :
    print(mode[0][0])
print(data_list[n-1]-data_list[0])