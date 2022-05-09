# fibo = [1,1]
# for i in range(2,11):
#     fibo.append(fibo[i-1]+fibo[i-2])
# for i in fibo:
#     print("fibo = ", i)
fibo1 = 1
fibo2 = 1
print("fibo = ",fibo1)
print("fibo = ",fibo2)
for i in range(9):
    fiboN = fibo1 + fibo2
    fibo1 = fibo2
    print("fibo = ", fiboN)
    fibo2 = fiboN