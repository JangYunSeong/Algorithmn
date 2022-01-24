height, width = input().split()
width = int(width)
height = int(height)
answer = 1
if(height >= 3):
    if(width >= 7):
        answer += 4 + (width - 7)
    else:
       answer += width - 1
       if(answer > 4):
           answer = 4
        
else:
    answer += (width-1) // 2
    if(answer > 4):
        answer = 4
if(height == 1 or width == 1):
    answer = 1
print(answer)