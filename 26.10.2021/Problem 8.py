# Compare two numbers and print out the greater one or say that they're equal.
# "The first number is {}"
# "The second number is {}"
# "{} is greater than {}"

first_number = int(input())
second_number = int(input())

if first_number > second_number:
    print(f"The first number is {first_number}")
    print(f"The second number is {second_number}")
    print(f"{first_number} is greater than {second_number}")

elif second_number > first_number:
    print(f"The first number is {first_number}")
    print(f"The second number is {second_number}")
    print(f"{second_number} is greater than {first_number}")

else:
    print(f"The first number is {first_number}")
    print(f"The second number is {second_number}")
    print(f"Both of them have the same value")
