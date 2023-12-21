def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def find_inverse(a, b):
    gcd, x, _ = extended_gcd(a, b)
    if gcd == 1:
        return x % b
    else:
        raise ValueError("The inverse does not exist.")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

inverse = find_inverse(a, b)
print(inverse)  
