a = int(input())
char=[]
for i in range(a):
    char.append(input())
for i in range(a):
    cnt=0
    res=0
    tmp=char[i]
    for j in range(len(char[i])):
        if tmp[j]=="O":
            cnt+=1
            res+=cnt
        else:
            cnt=0
    char[i]=res
for i in range(a):
    print(char[i])