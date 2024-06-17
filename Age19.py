age = int(input("Enter your age: "))
education_level = int(input("Enter your education level: "))
glass_power = float(input("Enter your glass power: "))

if age > 18:
    if education_level > 10:
        if glass_power < -6:
            print("Sorry, you are not eligible for a driving license due to your glass power.")
        else:
            print("Congratulations! You are eligible for a driving license.")
    else:
        print("Sorry, you are not eligible for a driving license due to your education level.")
else:
    print("Sorry, you are not eligible for a driving license due to your age.")