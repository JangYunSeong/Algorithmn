size = int(input())
array = []
for i in range(0,size):
    temp = input().split()
    array.append([int(temp[1]),temp[0]])
array.sort(reverse = True)
check = [0] * (size + 1)

for n,k in array:
    if(check[k] == 0):
        check[k] = n
    else:
        for j in range(k-1,0,-1):
            if(check[j] == 0):
                check[j] = n
                break
print(sum(check))
