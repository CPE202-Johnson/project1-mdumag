def bears(n):
# n is an integer
# boolean base case

    if n == 42: 
        return True

# operations according to game rules
    if n > 42:  
        last = n % 10
        temp = n - last
        secondtemp = temp % 100
        second = secondtemp / 10
        give = last * second
        remainder = n - give

        if remainder == 42: 
            if n % 3 == 0 or n % 4 == 0:
                return True
        else:
            pass

        if n % 5 == 0 and n > 83:
            return bears(n - 42)

        if n % 2 == 0 and n > 83:
            return bears(n/2)



# anything not applicable is false

    elif n < 42:
        return False
