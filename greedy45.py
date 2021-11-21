array = input()
number = []
answer = 0
temp = ""
for i in range(0,len(array)):
    number.append(int(array[i]))
print(number)
if(0 not in number or sum(number) % 3 != 0):
    answer = -1
else:
    number.sort(reverse = True)
    print(number)
    for i in range(0,len(number)):
        temp += str(number[i])
    answer = int(temp)
print(answer)