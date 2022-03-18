# 평균
n = int(input())
data_list = list(map(int,input().split()))
result = sum(data_list)
max_data_list = max(data_list)
sum_data = (result / max_data_list * 100) / n
print(sum_data)