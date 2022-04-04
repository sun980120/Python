# 알파벳 찾기

S = list(map(str,input()))
S_data = [-1]*26;
for i in range(len(S)):
    if S_data[ord(S[i])-97] == -1:
        S_data[ord(S[i])-97] = i;
for i in range(len(S_data)):
    print(S_data[i], end=' ')
    
# word = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위

# for x in alphabet :
#     print(word.find(chr(x)),end=' ') 