# Write a program that compares two integers and prints out if the first is greater than the second
first_number = int(input())
second_number = int(input())
if first_number > second_number:
    print(True)
elif second_number > first_number:
    print(False)
else:
    print("Equal")
