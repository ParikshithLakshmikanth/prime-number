num = int(input("Enter number to be checked: "))

flag = False

if num>1:
    for i in range(2,num):
        if num%i == 0:
            flag == True
            break
if flag == False:
    print(num,"not prime")
else:
    print(num,"prime")