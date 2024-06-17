import random

lottery_number = random.randint(1, 99)
user_number = int(input("Enter your lottery number (between 1 and 99): "))

if user_number == lottery_number:
    print("Congratulations! You have won the lottery!")
else:
        print("Sorry, you didn't win. The lottery number was", lottery_number)