number = int(input("Enter your number. It must be positive and more than 0: "))

hexadecimal_digits = "0123456789ABCDEF"
SYS_16 = 16
hexadecimal_number = []

while number > 0:
    hexadecimal_number.insert(0, hexadecimal_digits[int(number % SYS_16)])
    number //= SYS_16

print("Your number in hexadecimal system is", *hexadecimal_number)