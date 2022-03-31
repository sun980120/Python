# X보다 작은 수
n,m = map(int,input().split())
data = list(map(int,input().split()))
for i in range(n):
    if data[i]<m:
        print(data[i],end=" ")