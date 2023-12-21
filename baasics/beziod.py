def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, s, t = extended_gcd(b, a % b)
        return gcd, t, s - (a // b) * t

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd, s, t = extended_gcd(a, b)
print(f"Bezout coefficients for {a} and {b}: s = {s}, t = {t}")

