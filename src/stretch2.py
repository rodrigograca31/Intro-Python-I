import time
import math

times = 1000000


def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def is_prime2(number):
    for num in range(2, int(math.sqrt(number))):
        if number % num == 0:
            return False
    return True


print(is_prime(17))
print(is_prime(18))
print(is_prime(19))


start = time.time()
for x in range(times):
    is_prime(19)
print("Perf 1: \t%.8f" % float(time.time() - start))

start = time.time()
for x in range(times):
    is_prime2(19)
print("Perf 2: \t%.8f" % float(time.time() - start))
