list_of_numbers = []

numbers_of_inputs = int(input("Input how numbers you will input: "))
second_list = []
for i in range(numbers_of_inputs):
    added_number = int(input(f"Input {i + 1} number: "))
    list_of_numbers.append(added_number)

print("1. even numbers from this list")
print("2. odd numbers from this list")
print("3. negative numbers from this list")
print("4. positive numbers from this list")
your_choice = int(input("what choice you want: (type only number) "))


def get_even_numbers(my_list):
    even_list = []
    for number in my_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def get_odd_numbers(my_list):
    odd_list = []
    for number in my_list:
        if not number % 2 == 0:
            odd_list.append(number)
    return odd_list


def get_negative_numbers(my_list):
    negative_list = []
    for number in my_list:
        if number < 0:
            negative_list.append(number)
    return negative_list


def get_positive_numbers(my_list):
    positive_list = []
    for number in my_list:
        if number > 0:
            positive_list.append(number)
    return positive_list


if your_choice == 1:
    second_list = get_even_numbers(list_of_numbers)

elif your_choice == 2:
    second_list = get_odd_numbers(list_of_numbers)

elif your_choice == 3:
    second_list = get_negative_numbers(list_of_numbers)

elif your_choice == 4:
    second_list = get_positive_numbers(list_of_numbers)

print(second_list)
