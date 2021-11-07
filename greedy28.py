str = input()
zero = 0
one = 0
pivot = str[0]
if(pivot == '0'):
    zero += 1
else:
    one += 1
for i in range(1,len(str)):
    if(str[i] != pivot):
        if(str[i] == '0'):
            zero += 1
        else:
            one += 1
        pivot = str[i]
print(min(zero,one))
