# 피보나치 함수

# def soultion(N,data_list):
#     if N==0:
#         data_list[0]+=1;
#         return data_list;
#     elif N==1:
#         data_list[1]+=1;
#         return data_list;
#     else:
#         return soultion(N-1,data_list)+soultion(N-2,data_list)

# T = int(input())

# for i in range(T):
#     data_list=[0,0];
#     N = int(input())
#     data=list(soultion(N,data_list))
#     for j in range(len(data)-2,len(data)):
#         print(data[j],end=' ')
#     print()