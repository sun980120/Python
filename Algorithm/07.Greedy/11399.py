n = int(input())
m = list(map(int,input().split()))
sum = 0;
for i in range(n):
    for j in range(i):
        sum = sum + m[j];
print(sum)