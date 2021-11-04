# binary - decimal converter

binaryNum = (input("Enter a binary number: "))
binaryNumList = list(binaryNum)

checker = 0

for a in binaryNumList:
    if int(a) == 0 or int(a) == 1:
        checker += 1

if checker == len(binaryNumList):
    binaryNumList.reverse()
    decimalNum = 0

    print(binaryNumList)
    i = len(binaryNumList)

    for j in range(0, i):
        decimalNum += int(binaryNumList[j])*pow(2, j)
    print(
        f'A decimal number conversion of binary number {binaryNum} is :', decimalNum)
else:
    print("This is not a binary number")
