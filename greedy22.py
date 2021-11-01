answer = 0
crane_size = int(input())
temp = input().split()
crane = [0] * crane_size
for i in range(0,crane_size):
    crane[i] = int(temp[i])
crane.sort(reverse=1)
box_size = int(input())
temp2 = input().split()
box = [0] * box_size
for i in range(0,box_size):
    box[i] = int(temp2[i])
box.sort(reverse=1)
piv = 0
if(max(crane) < max(box)):
    answer = -1
else:
    while(1):
        if(box_size == 0):
            answer = (piv // crane_size) + 1
            break 
        pivot = crane[piv % crane_size]
        for i in range(0,box_size):
            if(pivot >= box[i]):
                del box[i]
                box_size -= 1
                piv += 1
                break
print(answer)
            
