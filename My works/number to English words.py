# Version: 0.0.01
# Programmed by Jason Sejik Lee
# Student number: 300115708
# Contact via Email: gggabikr@gmail.com

# getting an input
inputInt = input("Enter a integer: ")

# Two dictionaries as a database for numbers in English
numberInEng = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
               6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
               11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
               15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
               19: "nineteen", 20: "twenty", 30: "thirty", 40: "fourty",
               50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

# I will take a numbber less than one trillion
digitplace = {0: "", 2: "hundred", 3: "thousand", 6: "million",
              9: "billion"}


# A function to print up to 3 digit number.
def numberToEnglish_3(input):
    input = str(input)
    input = list(input)
    # In the case the input is 3 digit number
    if len(input) == 3:
        # hundreds place
        if input[0] != "0":
            print(f"{numberInEng[int(input[0])]} {digitplace[2]} ", end="")
        # tens and ones pleces
        # for the number bewteen 10 to 19 because they are irregulars
        if int(input[1]) == 1:
            input[2] = "1"+input[2]
            print(numberInEng[int(input[2])])
        else:
            print(
                f"{numberInEng[int(input[1]+'0')]} {numberInEng[int(input[2])]} ", end="")
    # In the case the input is 2 digit number
    elif len(input) == 2:
        if int(input[0]) == 1:
            input[1] = "1"+input[1]
            print(numberInEng[int(input[1])])
        else:
            print(
                f"{numberInEng[int(input[0]+'0')]} {numberInEng[int(input[1])]} ", end="")
    # In the case the input is 1 digit number
    else:
        if input[0] == "0":
            print("", end="")
        else:
            print(f"{numberInEng[int(input[0])]} ", end="")

# Main function


def numberToEnglish(input):
    # A list to divide and put three numbers each
    processedList1 = []
    processedList2 = []

    while len(input) > 0:
        # put last three numbers in to processedList1
        processedList1.append(input[-3:])
        input = input[:-3]

    # Reverse the order of the list because processedList1 is in a wrong order
    processedList2 = processedList1[::-1]
    # print(processedList2)

    if len(processedList2) > 0:
        for i in range(len(processedList2)):
            # execute numberToEnglish_3 for each element in the list2
            numberToEnglish_3(processedList2[i])

            # print addition word like thousand, million and billion
            # do it only when the three digit is not 000
            if processedList2[i] != "000":
                print(digitplace[(len(processedList2)-1-i)*3], end=" ")
            else:
                continue


numberToEnglish(inputInt)
