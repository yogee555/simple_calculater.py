# A simple calculater
print("enter the number 1 is addition")
print("enter the number 2 is subtraction")
print("enter the number 3 is multiplication")
print("enter the number 4 is division")
print("==============================")
choice = int(input("enter the number "))
num1 = int(input("enter the number "))
num2 = int(input("enter the number "))
if choice == 1:
    c = num1+num2
    print("enter the num add is = ",c)
elif choice == 2:
    c= num1-num2
    print("enter the num sub is = ",c)
elif choice == 3:
    c = num1*num2
    print("enter the num mul is = ",c)
elif choice ==4:
    c=num1/num2
    print("enter the num divi is = ",c)
else:
    print("invalid choice")