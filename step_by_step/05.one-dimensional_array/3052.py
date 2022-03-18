# 나머지
data = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    n = int(input())
    data[i] = n%42
data_set = set(data)
data = list(data_set)
print(len(data))