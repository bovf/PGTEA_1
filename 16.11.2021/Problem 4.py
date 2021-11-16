# On the first line we receive an number - n that is an integer.
# add 100
# leave 100 3
# insert 100 2
# "End"
# Output [x, x1, x2....xn]

n = int(input())
train = []

for _ in range(n):
    train.append(0)

while True:
    choice = input()

    if choice == "End":
        break
    else:
        choice_list = choice.split(" ")
        command = choice_list[0]
        number_of_passengers = int(choice_list[1])

        if command == "add":
            train[-1] = train[-1] + number_of_passengers
        elif command == "leave":
            wagon_index = int(choice_list[2]) - 1
            train[wagon_index] = train[wagon_index] - number_of_passengers
        else:
            wagon_index = int(choice_list[2]) - 1
            train[wagon_index] = train[wagon_index] + number_of_passengers

print(train)
