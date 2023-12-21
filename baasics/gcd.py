def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(gcd(a,b))