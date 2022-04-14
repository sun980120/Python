# # 숫자의 개수
# a = int(input())
# b = int(input())
# c = int(input())
# sum = a * b * c
# number_list=[0,0,0,0,0,0,0,0,0,0]
# while sum!=0:
#     data = sum % 10
#     sum = sum // 10
#     for i in range(10):
#         if i==data:
#             number_list[i]+=1
# for i in range(10):
#     print(number_list[i])

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))