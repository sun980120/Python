# 세탁소 사장 동혁

n = int(input())
data=[25,10,5,1]
for i in range(n):
    m = int(input());
    for j in data:
        print(m//j,end=' ');
        m%=j;
    print();