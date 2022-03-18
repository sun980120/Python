a = int(input())
b = int(input())
c = b
while(b!=0):
    data = b%10
    b=int(b/10);
#     print(data)
    print(a*data)

print(a*c)