# 평균은 넘겠지
n = int(input())
for i in range(n):
    result = 0
    count = 0
    avg_sum = 0
    m_list = list(map(int,input().split()))
    for j in range(1,m_list[0]+1):
        result += m_list[j]
    result = result / m_list[0]
    for j in range(1,m_list[0]+1):
        if m_list[j] > result:
            count += 1;
    avg_sum = (count / m_list[0]) * 100
    print("{:.3f}%".format(avg_sum))