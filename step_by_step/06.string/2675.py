# 문자열 반복

T = int(input());
for i in range(T):
    n,m = map(str,input().split());
    n = int(n);
    for j in m:
        for k in range(n):
            print(j,end='');
    print()
    
# T = int(input());
# for i in range(T):
#     n,m =input().split();
#     text = ''
#     for i in m:
#         text += int(n)*i
#     print(text)