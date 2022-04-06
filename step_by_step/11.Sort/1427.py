# 소트인사이드

N=input();
data=[]
for i in N:
    data.append(int(i))
data.sort(reverse=True);
for i in data:
    print(i,end='')