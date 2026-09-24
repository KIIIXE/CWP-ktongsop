num = int(input("Enter number less than 25: "))
if num > 25:
    print("Error")
else:
    while num <= 25:
        print("Instide the loop, My variable is " + str(num))
        num += 1