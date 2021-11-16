numbers = []

while True:
    command = input()
    if command == "end":
        break
    else:
        command_number = int(command)
        numbers.append(command_number)

even_numbers = [x for x in numbers if x % 2 == 0]
print(numbers)
print(even_numbers)
