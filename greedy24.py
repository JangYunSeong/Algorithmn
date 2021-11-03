#15904
string = input()
check = 0
for i in range(0,len(string)):
    if(check == 0 and string[i] == "U"):
        check = 1
    if(check == 1 and string[i] == "C"):
        check = 2
    if(check == 2 and string[i] == "P"):
        check = 3
    if(check == 3 and string[i] == "C"):
        check = 4
if(check == 4):
    print("I love UCPC")
else:
    print("I hate UCPC")