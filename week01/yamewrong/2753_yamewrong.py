a = int(input())
flag=0
if(a%4==0 and a%100!=0 or a%400==0):
    flag=1
print(flag)