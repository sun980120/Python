# 1로 만들기
X = int(input());

data = [0]*1000001;
for i in range(2,X+1):
    data[i] = data[i-1]+1;
    if i%3==0:
        data[i] = min(data[i],data[i//3]+1)
    if i%2==0:
        data[i] = min(data[i],data[i//2]+1)
    else :
        data[i] = min(data[i],data[i-1]+1)
print(data[X]);