a,b = map(int,input().split())
c = int(input())

b = b + c

if int(b/60)>0:
    imsi = int(b/60)
    a = a + imsi
    b = b - (60*imsi)
    if a>=24:
        a = a % 24;
print(int(a),int(b))