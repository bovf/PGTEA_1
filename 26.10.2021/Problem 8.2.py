first_number = int(input())
second_number = int(input())
is_it_greater = first_number > second_number
if is_it_greater:
    print(f"The first number is {first_number}")
    print(f"The second number is {second_number}")
    print(f"{first_number} is greater than {second_number}")

elif not is_it_greater:
    print(f"The first number is {first_number}")
    print(f"The second number is {second_number}")
    print(f"{second_number} is greater than {first_number}")
