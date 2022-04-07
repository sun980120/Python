# 스택 수열
import sys
input = sys.stdin.readline;

n = int(input())
stack = []
op = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)

# data=[]
# data_list=[]
# stack=[0,1]
# n = int(input())
# for i in range(n):
#     data.append(int(input()))
# while True:
#     print(cnt)
#     print(n)
#     print(stack)
#     if cnt == n:
#         break;
#     for i in range(2,n+1):
#         if data[cnt]!=stack[-1]:
#             stack.append(i)
#             # print('+')
#         else:
#             cnt += 1;
#             # print('-')
# cnt = 1;           
# for i in range(1,n+1):
#     for j in range(cnt,n+1):
        
# data_i, stack_i,cnt = 0, 1, 1;
# while_cnt=0
# while True:
#     if while_cnt>2*n:
#         print('NO')
#         exit(1);
#     while_cnt+=1;
#     if data[data_i] != stack[stack_i]:
#         if cnt <= n:
#             stack.append(cnt)
#             cnt+=1;
#             stack_i += 1;
#             data_list.append('+')
#         else: continue;
#     else:
#         stack.pop();
#         stack_i -= 1;
#         data_i += 1;
#         data_list.append('-')
#     if data_i == n:
#         break;
# for i in data_list:
#     print(i)