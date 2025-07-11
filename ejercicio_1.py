def fib(numero):
    a = 0
    b = 1

    while a < numero:
        print(a, end='')
        a = b
        b = a + b 
        print()

    print("fin del programa")




fib(1000)