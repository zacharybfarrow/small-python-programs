from cs50 import get_string
import re

# Ask user for Credit Card number
ccNumber = get_string("Credit card number: ")
digits = len(ccNumber)
while True:
    # If user input is not numerical, ask again
    if ccNumber.isnumeric() is False:
        print("Only numbers accepted")
        ccNumber = get_string("Credit card number: ")
    # If user input is not valid length, print invalid
    elif digits < 13 or digits > 16:
        print("INVALID")
        exit(1)
    # If credit card number passes these tests, move on
    else:
        break

# Apply Luhn's Algorithm to Credit Card number and determine if valid number
checkSum = 0
# Starting at last digit, add every other digit to checkSum
for digit in range(digits - 1, -1, -2):
    checkSum += int(ccNumber[digit])
# Starting at 2nd to last digit, multiply every other digit by 2, if product is 2 digit number, add digits together. Add result to checkSum
for digit in range(digits - 2, -1, -2):
    product = int(ccNumber[digit]) * 2
    if len(str(product)) > 1:
        product = sum(int(digit) for digit in str(product))
    checkSum += product
# If checksum does not end in zero, card number is invalid
if checkSum % 10 != 0:
    print("INVALID")
    exit(1)

# If number is valid, look at first 2 digits and determine credit card company
if re.search("^(34|37)", ccNumber):
    print("AMEX")
if re.search("^5[1-5]", ccNumber):
    print("MASTERCARD")
if re.search("^4", ccNumber):
    print("VISA")
    exit(0)