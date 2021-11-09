import timeit

start = timeit.default_timer()
# even hour  minutes % 7 == 0
# odd hour  minutes % 2 == 0
# 02: 00
# 02: 07
# f"0{hours}:0{minutes}"
hour = 0
minutes = 0

while hour < 24:
    while minutes < 60:
        if (hour % 2) == 0:
            if minutes % 7 == 0:
                if hour < 10:
                    if minutes < 10:
                        print(f"0{hour}:0{minutes}")
                    else:
                        print(f"0{hour}:{minutes}")
                else:
                    if minutes < 10:
                        print(f"{hour}:0{minutes}")
                    else:
                        print(f"{hour}:{minutes}")
        else:
            if minutes % 2 == 0:
                if hour < 10:
                    if minutes < 10:
                        print(f"0{hour}:0{minutes}")
                    else:
                        print(f"0{hour}:{minutes}")
                else:
                    if minutes < 10:
                        print(f"{hour}:0{minutes}")
                    else:
                        print(f"{hour}:{minutes}")
        minutes += 1
    hour += 1
    minutes = 0




stop = timeit.default_timer()

print('Time: ', stop - start)
