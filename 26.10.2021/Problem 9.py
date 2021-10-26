# Write a program that compares 3 integers and prints them out in descending order
# e.g. Input: 234, 542, 123 Output: 542, 234, 123

a = int(input())
b = int(input())
c = int(input())

if a > b:
    if b > c:
        print(f"{a} > {b} > {c}")
        # a > b > c
    else:
        print(f"{a} > {c} > {b}")
        # a > c > b
elif b > a:
    if a > c:
        print(f"{b} > {a} > {c}")
        # b > a > c
    else:
        print(f"{b} > {c} > {a}")
        # b > c > a
elif c > a:
    if a > b:
        print(f"{c} > {a} > {b}")
        # c > a > b
    else:
        print(f"{c} > {b} > {a}")
        # c > b > a
