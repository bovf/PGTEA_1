# Write a program that gets 6 strings as input, prints the list, reverses the list and prints the elements on new lines
# e.g. Input: apple     Output: ["apple", "orange", "banana", "apple1", "orange1", "banana1"]
#             orange            ["banana1", "orange1", "apple1", "banana", "orange", "apple"]
#             banana            banana1
#             apple1            orange1
#             orange1           .......
#             banana1

my_list = []
for _ in range(6):
    new_string = input()
    my_list.append(new_string)
my_list_reverse = my_list.copy()
my_list_reverse.reverse()
print(my_list)
print(my_list_reverse)
for string in my_list_reverse:
    print(string)
