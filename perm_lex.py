def perm_gen_lex(a): 
# a should be a string and the program will return a list of strings
# the purpose is to return all possible permutations of the letters of a string
# base cases: returns an empty list if length is 0, returns the letter if length is 1
    if len(a) == 0:
        return [a]
    
    if len(a) == 1:
        return [a]
    
    else:

        wordlist = []


        for word in perm_gen_lex(a[ : -1]):


            for index in range(len(word)+1):

                permuted = word[:index] + a[-1] + word[index:]


                wordlist.append(permuted)


        return sorted(wordlist)
