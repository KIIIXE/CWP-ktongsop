original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []

for number in original_array:
    if number > 5:
        new_value = number + 2

        if new_value not in new_array:
            new_array.append(new_value)

print("Original array:", original_array)
print("New array:", new_array)