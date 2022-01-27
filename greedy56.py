num1, num2 = input().split()
min1 = num1.replace('6','5')
min2 = num2.replace('6','5')
max1 = num1.replace('5','6')
max2 = num2.replace('5','6')

min = int(min1) + int(min2)
max = int(max1) + int(max2)
print(min, max)

