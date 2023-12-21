def lcm(a, b):
    # Find the greater number between a and b
    max_num = max(a, b)
    
    # Start with the greater number and check if it is divisible by both a and b
    while True:
        if max_num % a == 0 and max_num % b == 0:
            lcm = max_num
            break
        max_num += 1
    
    return lcm

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(lcm(a,b))
