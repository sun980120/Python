# 네 번째 점
x_=[]
y_=[]
for i in range(3):
    tmp_x,tmp_y = map(int, input().split())
    x_.append(tmp_x)
    y_.append(tmp_y)
for i in range(3):
    if x_.count(x_[i]) == 1:
        x = x_[i]
    if y_.count(y_[i]) == 1:
        y = y_[i]
print(x,y)