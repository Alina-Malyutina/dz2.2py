import fractions

number1 = (input("Enter your number in format a/b: "))
number2 = (input("Enter your number in format a/b: "))

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
 
def reduction(den3, num3):
    common_factor = gcd(num3, den3)
    den3 = int(den3 / common_factor)
    num3 = int(num3 / common_factor)
    print(num3, "/", den3)
 
def addFraction(num1, den1, num2, den2):
 
    den3 = gcd(den1, den2)
    den3 = (den1 * den2) / den3
    num3 = ((num1) * (den3 / den1) +
            (num2) * (den3 / den2))
    reduction(den3, num3)
num1 = int(number1[0])
den1 = int(number1[2])
num2 = int(number2[0])
den2 = int(number2[2])

print("Sum of this is ", end = "")
addFraction(num1, den1, num2, den2)

mylty_num = num1 * num2
mylty_den = den1 * den2
print("Multiply of this is ", end = "")
reduction(mylty_den, mylty_num)

number1_f = fractions.Fraction(int(number1[0]), int(number1[2]))
number2_f = fractions.Fraction(int(number2[0]), int(number2[2]))

print("Check me:", number1_f + number2_f)
print("Check me:", number1_f * number2_f)

