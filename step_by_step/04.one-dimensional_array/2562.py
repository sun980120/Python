# 최댓값

# max = int(-999)

# for i in range(1,10):
#     n = int(input())
#     if max <= n:
#         max = n
#         max_i = i;
# print(max)
# print(max_i)

data = []
for i in range(9):
    data.append(int(input()))
    
print(max(data))
print(data.index(max(data))+1)