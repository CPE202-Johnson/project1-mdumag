
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    
    # num and b are integers
    # base case negative numbers

    if num < 0:
        return 0

    #finding quotient and remainders
    if num < b:
        if (num == 10):
            digit = str("A")
        if (num == 11):
            digit = str("B")
        if (num == 12):
            digit = str("C")
        if (num == 13):
            digit = str("D")
        if (num == 14):
            digit = str("E")
        if (num == 15):
            digit = str("F")
        else:
            digit = str(num)
        return str("" + digit)
    else:
        remainder = num % b

        if (remainder == 10):
            remainder_string = str("A")
        if (remainder == 11):
            remainder_string = str("B")
        if (remainder == 12):
            remainder_string = str("C")
        if (remainder == 13):
            remainder_string = str("D")
        if (remainder == 14):
            remainder_string = str("E")
        if (remainder == 15):
            remainder_string = str("F")
        elif(remainder < 10):
            remainder_string = str(remainder)

        return convert(num//b, b) + ("" + remainder_string)
