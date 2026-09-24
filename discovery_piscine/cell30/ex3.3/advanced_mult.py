table = 0

while table <= 10:
    number = 0
    print("Table de", table, end=":")

    while number <= 10:
        print("", table * number, end="")
        number += 1

    print()
    table += 1