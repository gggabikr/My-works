def evenOddDifference():
    integer = int(raw_input("Enter an integer:"))
    integer2 = integer
    if integer%2 ==0:
        even = integer
        for a in range(integer):
            if a %2 ==0:
                even = even + a
        
        odd = integer2-1
        integer2 -=1
        for b in range (integer2):
            if b %2 !=0:
                odd = odd +b

    else:
        odd = integer
        for a in range(integer):
            if a %2 !=0:
                odd = odd + a
        
        even = integer2-1
        integer2 -=1
        for b in range (integer2):
            if b %2 ==0:
                even = even +b
                
    print "Sum of even numbers:", even
    print "Sub of odd numbers:", odd
    print "Difference between the sum of the even integers and sum of the odd integers:", abs(even-odd)
evenOddDifference()
        
