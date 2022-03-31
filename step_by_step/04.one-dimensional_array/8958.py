# OX퀴즈
n = int(input())
max_list = int(0)
for i in range(n):
    count=0
    str_data = str(input())
    str_list = list(str_data)
    for j in range(len(str_list)):
        count+=1;
        if str_list[j]=='X':
            count=0;
        else:
            max_list+=count
    print(max_list)
    max_list=0;