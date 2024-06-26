a = [2,4,5,6,7,8,13,15,17,20]
prime_count = 0

for num in a:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print("Prime number:", num)
            prime_count += 1

print("Total number of prime numbers:", prime_count)
