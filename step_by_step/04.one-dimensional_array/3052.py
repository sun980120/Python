# 나머지
data = [0]*10
for i in range(10):
    n = int(input())
    data[i] = n%42
data_set = set(data)
print(len(data_set))