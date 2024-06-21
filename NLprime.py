a = [2,4,5,6,7,8,13,15,17,20]
prime_numbers = []

for num in a:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                i = num
        if is_prime:
            prime_numbers.append(num)

print("Prime numbers: ", prime_numbers)
print("Total number of prime numbers: ", len(prime_numbers))