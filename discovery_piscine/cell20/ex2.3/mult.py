first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
result = first_num * second_num
print(str(first_num) + " x " + str(second_num) + " = " + str(result))
if result == 0:
    print("The result is positive and negative")
elif result > 0:
    print("The result is positive")
else:
    print("The result is negative")