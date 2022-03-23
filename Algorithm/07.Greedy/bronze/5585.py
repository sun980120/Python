# 거스름돈

# n = int(input())
# m = 1000-n;
# cnt=0;
# while m!=0:
#     cnt += m//500;
#     m=m%500;
#     cnt += m//100;
#     m=m%100;
#     cnt += m//50;
#     m=m%50;
#     cnt += m//10;
#     m=m%10;
#     cnt += m//5;
#     m=m%5;
#     cnt += m//1;
#     m=m%1;
    
# print(cnt)

a = 1000 - int(input())
b = [500,100,50,10,5,1]
count=0;
for i in b:
    count+=a//i
    a%=i
print(count)