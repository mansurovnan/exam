def fibonacci(n):
    a, b = 0, 1
    for f in range(n):
        yield a
        a, b = b, a + b


n = int(input("n = "))

for i in fibonacci(n):
    print(i)