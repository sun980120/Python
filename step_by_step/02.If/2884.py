a,b = map(int,input().split())

if b-45<0:
    b=b+15;
    if a-1<0:
        a=a+23
    else:
        a=a-1
else:
    b=b-45;
    
print(a,b)