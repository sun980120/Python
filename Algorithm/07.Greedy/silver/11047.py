# 동전 0
N,K = map(int,input().split())
data_list=[]
for i in range(N):
    data_list.append(int(input()))
data_list.sort(reverse=True)
count=0;
for i in data_list:
    count+=K//i
    K%=i;
print(count)