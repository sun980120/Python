# 전자레인지

a = int(input())
n=[300, 60, 10]
check=[0,0,0]
cnt = 0;
for i in n:
    check[cnt] = a//i;
    cnt+=1;
    a%=i;
if a!=0:
    print(-1)
else:
    for i in check:
        print(i,end=' ')