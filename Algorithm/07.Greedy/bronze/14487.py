# 욱제는 효도쟁이야!!

n = int(input())

data = list(map(int,input().split()))

data.sort()

data_sum=0
for i in range(len(data)-1):
    data_sum+=data[i]
print(data_sum)

# n=int(input())
# tmp=list(map(int,input().split()))
# print(sum(tmp)-max(tmp))