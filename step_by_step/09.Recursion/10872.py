# 팩토리얼

from re import S


def soultion(N,cnt):
    if N == 0:
        print(cnt)
    else :
        cnt*=N;
        soultion(N-1, cnt);

# def factorial(N):
#     result = 1;
#     if N>0:
#         result = N * factorial(N-1);
#     return result;



n = int(input());

soultion(n,1);
# print(factorial(n))
