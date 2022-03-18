a,b,c = map(int,input().split())

if a==b and b==c:
    sum = 10000 + (a * 1000)
elif a==b or b==c or a==c:
    if a==b:
        sum = 1000 + (b * 100)
    elif b==c:
        sum = 1000 + (b * 100)
    elif a==c:
        sum = 1000 + (c * 100)

else:
    sum = max(a,b,c) * 100
print(sum)