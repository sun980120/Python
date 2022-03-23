# 우유 축제

n = int(input())
n_list = list(map(int,input().split()))
cnt=0;
start_data = 0
max_cnt = -999
n_data=[0,1,2]
for i in range(n):
    if n_list[i] == n_data[start_data%3]:
        cnt+=1;
        start_data+=1;
        if max_cnt < cnt:
            max_cnt = cnt;
print(max_cnt)

# n = int(input())
# milk = list(map(int,input().split()))

# count = 0

# for i in range(n):
#     if milk[i] == count % 3:
#         count += 1

# print(count)