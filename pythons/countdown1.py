#It's a countdown program. 01:00:00 --> 00:00:00

import time

my_time = int(input("Please enter time in seconds: " ))



for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)   
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

print("Time's up!")
