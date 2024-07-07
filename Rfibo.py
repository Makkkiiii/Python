def fibo(n, a=0, b=1):
    if n > 0:
        print(a, end=' ')
        fibo(n-1, b, a+b)

n = int(input("Enter the number of terms: "))
fibo(n)