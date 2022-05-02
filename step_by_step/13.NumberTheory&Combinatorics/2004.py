# # 조합 0의 개수
# import sys,math
# input = sys.stdin.readline;

# n,k = map(int,input().split())
# cnt = 0
# for i in reversed(str(math.comb(n,k))):
#     if int(i) == 0:
#         cnt+=1;
#     else:
#         break;
# print(cnt,end='')