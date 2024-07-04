def sumanavg():
    sum = 0
    for i in range(1,11):
        mark = int(input(f"Enter score of student {i} "))
        sum += mark
    avg=sum/10
    return sum, avg

a,b=sumanavg()
print("\n Sum of marks is ",a)
print("\n Aerage marks is ",b)