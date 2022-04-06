# 좌표 압축
import sys
input=sys.stdin.readline
# print=sys.stdout.write

N=int(input())
arr=list(map(int,input().split()))
sort_arr=sorted(set(arr))
for i in sort_arr:
    print(i ,end =' ')
arr_dict={i:v for v,i in enumerate(sort_arr)}
for i in arr:
    print(f'{arr_dict[i]} ')