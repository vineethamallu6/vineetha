string=input()
s=' '
for i in string:
    if i in '!@#$%^&*':
        i=' '
    s=s+i
print(str(s))
