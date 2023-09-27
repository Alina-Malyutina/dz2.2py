number = int(input("Enter your number. It must be positive and more than 0: "))

hexadecimal_digits = "0123456789ABCDEF"
SYS_16 = 16
hexadecimal_number = []
input_num = number
while input_num > 0:
    hexadecimal_number.insert(0, hexadecimal_digits[int(input_num % SYS_16)])
    input_num //= SYS_16

print("Your number in hexadecimal system is", *hexadecimal_number)

print("Check by function:", hex(number))