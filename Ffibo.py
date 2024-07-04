def fibo():
    n = int(input("How many terms to generate?"))
    a,b = 0,1
    for i in range (n):
        print(a, end = "\t")
        c=a+b
        a=b
        b=c
        
        
fibo()        
