size = int(input())
rope = [0] * size
for i in range(0,size):
    rope[i] = int(input())
rope.sort()
max = 0
for i in range(0,size):
    temp = rope[i] * (size - i)
    if(max < temp):
        max = temp
print(max)