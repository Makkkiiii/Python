n = int(input("Enter a number: "))

for i in range(1, 11):
    for j in range(1, n+1):
        print(f"{j} * {i} = {j*i}", end="\t")
    print("\n")