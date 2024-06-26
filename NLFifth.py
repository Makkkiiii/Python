sum_even = 0
even_count = 0

while even_count < 5:
    number = int(input("Enter an integer number: "))
    if number % 2 == 0:
        sum_even += number
        even_count += 1

print(f"The sum of the five even numbers is: {sum_even}")