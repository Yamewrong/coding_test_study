a = int(input())
res=[]
for i in range(a):
    x = input().split()
    y = int(x[0])
    b = x[1]
    temp=""
    for j in range(len(b)):
        for k in range(y):
            tmp=b[j]
            temp+=tmp
    res.append(temp)
for i in range(a):
    print(res[i])
