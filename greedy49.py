sugar = int(input('input sugar gram :'))
box1 = 5
box2 = 3
size = 0
count = 0
top = 0
array = [0] * 100

while((sugar - size) > 5):
    array[top] = box1
    size += box1
    top += 1
while(top > 0):
    if(sugar == size):
        break
    if((sugar -size) % 3 != 0):
        top -= 1
        size -=array[top]
        array[top] = 0
    if((sugar -size) % 3 == 0):
        while(1):
            size += box2
            array[top] = box2
            top +=1
            if(sugar == size):
                break
if(top == 0):
    print(-1)
else:
    print(array[0:top])
    print(top)
    

