num1 = int(input("Enter the value ="))
num2 = int(input("Enter the value ="))
opr =input("Enter the opr = (+,-,*,/)")

if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("Invalid operator")