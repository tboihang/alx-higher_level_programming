#!/usr/bin/python3
import random
random_number = random.randint(-10, 10)
if random_number > 0:
    print("{} is a positive number".format(random_number))
else if random_number == 0:
    print("{} is zero".format(random_number))
else:
    print("{} is a negative number".format(random_number))
