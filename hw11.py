import os
def count_e_vs_t(path):
    '''
    Purpose:
        Counts the number of Es vs Ts in given directory
    Input Parameters:
        path = a string representing the given directory
    Return Value:
        a int representing the number of Es vs Ts
    '''
    total = 0
    for file in os.listdir(path):
        if os.path.isfile(path+'/'+file):
            fname = path+'/'+file  #This is a file, print out the path
            with open(fname, 'r') as fp:
                text = fp.read()
                sumE = text.count('e') + text.count('E')
                sumT = text.count('t') + text.count('T')
                total += sumE-sumT
        else:
            total += count_e_vs_t(path+'/'+file)  #Go into a subdirectory
    return total

def palindrome(phrase):
    '''
    Purpose:
        Checks if the phrase given is a palindrome
    Input Parameters:
        phrase: a string of lowercase letters seperated by spaces
    Return Value:
        a boolean value representing if the phrase is a palindrome or not
    '''
    if phrase == '':
        return True
    else:
        while (phrase[0] == ' ' or phrase[-1] == ' '):
            if phrase[0] == ' ':
                phrase = phrase[1:]
            if phrase[-1] == ' ':
                phrase = phrase[:-1]
        if phrase[0] != phrase[-1]:
            return False
        return palindrome(phrase[1:-1])

def collatz(n):
    '''
    Purpose:
        Creates a collzatz sequence of given number n
    Input Parameters:
        n = an int representing the number to start the collztz sequence
    Return Value:
        a list representing the collatz sequence
    '''
    if n == 1:
        return [1]
    else:
        if n % 2 == 0:
            return [n] + collatz(n//2)
        else:
            return [n] + collatz((n*3)+1)
