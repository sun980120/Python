# 최댓값

max = int(-999)

for i in range(1,10):
    n = int(input())
    if max <= n:
        max = n
        max_i = i;
print(max)
print(max_i)