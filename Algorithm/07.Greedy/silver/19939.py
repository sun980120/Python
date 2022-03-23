# 박 터뜨리기

n,k = map(int,input().split())
k_data = (k*(k+1)) //2
if k_data > n:
    print(-1)
elif (n-k_data)%k==0:
    print(k-1)
else:
    print(k)