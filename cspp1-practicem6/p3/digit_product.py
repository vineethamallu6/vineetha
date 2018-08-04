num=int(input())
mul=1
while num>0:
    temp=num%10
    mul=mul*temp
    num=num//10
print(mul)
