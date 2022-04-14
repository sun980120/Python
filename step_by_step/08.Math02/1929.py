# 소수 구하기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def isPrime(a):
  if a < 2:
    return False
  for i in range(2, int(a**0.5)+1):
    if a % i == 0:
      return False
  return True


for i in range(n, m+1):
    if isPrime(i):
        print(i)
