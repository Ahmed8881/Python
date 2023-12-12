def oddish_evenish(number):
    digit_sum = sum(int(digit) for digit in str(number))
    if digit_sum % 2 == 0:
        return "Evenish"
    else:
        return "Oddish"
number = int(input("Enter a number: "))
print(oddish_evenish(number))

