num=[]
for j in range(9):
    num.append(int(input()))
max=0
cnt=0
for i in num:
    cnt+=1
    if i>max:
        max=i
        max_index=cnt
print(max)
print(max_index)