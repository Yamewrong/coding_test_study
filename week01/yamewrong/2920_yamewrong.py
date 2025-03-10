num =list(map(int,input().split()))

cnt = 0
for i in range(7):
    if num[i]>num[i+1]:
        if num[i]-num[i+1]==1:
            cnt = 0
        else: 
            cnt = 1
            break
    elif num[i]<num[i+1]:
        if num[i+1]-num[i]==1:
            cnt = 2
        else : 
            cnt = 1
            break
if cnt==0:
    print("descending")
elif cnt ==2:
    print("ascending")
else: print("mixed")