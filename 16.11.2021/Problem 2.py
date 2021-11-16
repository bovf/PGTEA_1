# # 1, 52, 3, 4, 5
# numbers = input().split(", ")
# for index in range(len(numbers)):
#     numbers[index] = int(numbers[index])
#
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
#
# print(even_numbers)


numbers = [even_x for even_x in [int(x) for x in input().split(", ")] if even_x % 2 == 0]
print(numbers)
