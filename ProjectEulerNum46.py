# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import time # This program takes < 1 sec to run -- Matthew Bruno Jan 8, 2021
start = time.time()

answer = 0
primes = []
odds = [2*k + 1 for k in range(1, 5000)]

def sieve_eratosthenes(n):
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primes

sieve_eratosthenes(10000)

odd_comp_nums = [x for x in odds if x not in primes]

squares = [y**2 for y in range(1, 100)]

def check_goldman(num):
    for k in primes:
        for c in squares:
            if k + 2 * c == num:
                return True

for a in odd_comp_nums:
    if answer < 1:
        if check_goldman(a) is True:
            continue
        else:
            answer += a
    else:
        break

print(answer)

stop = time.time()
print("Time: ",stop-start)