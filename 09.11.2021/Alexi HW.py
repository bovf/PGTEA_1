import timeit

start = timeit.default_timer()
# Write a program that prints out the timestamps of our broken clock
# even hour minutes % 7 == 0
# odd hour minutes % 2 == 0
# using loop in loop

hours = 0
minutes = 0
while hours < 24:
    while hours % 2 == 0:
        if minutes % 7 == 0:
            print (f"{hours}:{minutes}")

        minutes += 1

        if minutes == 60:
            hours += 1
            minutes = 0

    while hours % 2 == 1:
        if minutes % 2 == 0:
            print (f"{hours}:{minutes}")

        minutes += 1

        if minutes == 60:
            hours += 1
            minutes = 0
stop = timeit.default_timer()

print('Time: ', stop - start)
