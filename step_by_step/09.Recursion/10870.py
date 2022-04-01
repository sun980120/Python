# 피보나치 수 5

def fibo(N):
    if N<=1:
        return N;
    else:
        return fibo(N-1)+fibo(N-2)

n = int(input());
print(fibo(n))