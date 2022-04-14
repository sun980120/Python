# 베르트랑 공준
import sys
input = sys.stdin.readline

def isPrime(a):
  if a < 2:
    return False
  for i in range(2, int(a**0.5)+1):
    if a % i == 0:
      return False
  return True

data = list(range(2,246912))
memo=[]
for i in data:
    if isPrime(i):
        memo.append(i)

while True:
    N = int(input())
    if N==0: break;
    cnt=0
    for i in memo:
        if N<i <=2*N:
            cnt+=1
    print(cnt)