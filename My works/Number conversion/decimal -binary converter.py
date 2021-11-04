import math

decimalNum = int(input("Enter a decemal number: "))
initialValue = decimalNum
i = 0
binaryNum = 0

while decimalNum != 0:
    remainder = decimalNum % 2
    binaryNum += remainder*pow(10, i)
    decimalNum = decimalNum//2
    # decimalNum = math.floor(decimalNum/2)
    i += 1
print(
    f'A binary number conversion of decimal number {initialValue} is : ', binaryNum)
