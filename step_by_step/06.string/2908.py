# 상수

from re import L


n,m = input().split()
n_text='';
m_text='';
for i in reversed(n):
    n_text+=i
for i in reversed(m):
    m_text+=i
if int(n_text)>int(m_text):
    print(n_text);
else:
    print(m_text)
    
# num1, num2 = input().split()
# num1 = int(num1[::-1])  # [::-1] : 역순
# num2 = int(num2[::-1])

# if num1 > num2:
#     print(num1)
# else :
#     print(num2)