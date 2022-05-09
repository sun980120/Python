# A,B,V = map(int,input().split())

H = int(input("나무 막대의 높이는 : "))
A = int(input("달팽이가 하루에 올라갈 수 있는 높이는 : "))
B = int(input("달팽이가 자는 동안 미끄러지는 높이는 : "))

CNT = 0
TMP = 0
while True:
    # print(TMP)
    TMP += A
    CNT += 1;
    if TMP >= H:
        break
    else:
        TMP-=B
print(CNT)