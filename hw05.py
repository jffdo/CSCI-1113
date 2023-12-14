import random
# Problem A: six_tails
def six_tails():
    '''
    Purpose:
        Simulates flipping a coin by using the random.randint(0,1) and counts
        how many attempts it takes to receive 6 tails
    Input Parameter(s):
        none
    Return Value:
        An int value on how many attempts it took to receive 6 tails
    '''
    streak = 0
    total = 0
    while streak != 6:
        flip = random.randint(0, 1)
        if flip == 1:
            streak += 1
        else:
            streak = 0
        total += 1
    return total


# Problem B: average_six
def average_six(n):
    '''
    Purpose:
        Runs the six_tails function n times and returns the average
    Input Parameter(s):
        n = the number of times the six_tails function will run
    Return Value:
        A float value on the average of the results of six_tails
    '''
    i = 0
    total = 0
    while i < n:
        result = six_tails()
        total += result
        i += 1
    avg = total / i
    return avg

# Problem C: population
def population(small, middle, big):
    '''
    Purpose:
        Simulates the populations of three types of fish living in an isolated
        lake
    Input Parameter(s):
        small = an int of the number of small fish
        middle = an int of the number of middle fish
        big = an int of the number of big fish
    Return Value:
        An int of the number of weeks it take for one of the populations to
        reach less than 10 members, or 30 if all survive.
    '''
    week = 0
    wiped = False
    while (week < 30) and (wiped == False):
        if small < 10:
            wiped = True
        elif middle < 10:
            wiped = True
        elif big < 10:
            wiped = True
        else:
            week += 1
            new_small = int(1.1*small - 0.0002*small*middle)
            new_middle = int(0.95*middle + 0.0001*small*middle - 0.00025*middle*big)
            new_big = int(0.9*big + 0.0002*middle*big)
            print("Week", week, "- Small:", new_small, " Middle:", new_middle,
            " Big:", new_big)
            small = new_small
            middle = new_middle
            big = new_big
    return week

# Problem D: find_password
def find_password(filename):
    '''
    Purpose:
      Given an encrypted file, tries every possible four letter lowercase
      password for that file until one works, and then returns the password.
    Input Parameter(s):
      filename is a string representing the name of the encrypted file.
      The file must be in the same folder as this script.
    Return Value:
      Returns the password that successfully decrypts the given file
    '''
    fp = open(filename)
    data = fp.read()

    for i in range(97,123):
        for j in range(97,123):
            for k in range(97,123):
                for l in range(97,123):
                    password = chr(i) + chr(j) + chr(k) + chr(l)
                    if decrypt(data,password):
                        return password
    return False


#DO NOT EDIT ANYTHING BELOW THIS LINE
#Below are helper functions used for decrypting the text files.
#You don't have to understand how any of these work.

def decrypt(data, password):
    '''
    Purpose:
      Check whether the password is correct for a given encrypted
      file, and print out the decrypted contents if it is.
    Input Parameter(s):
      data is a string, representing the contents of an encrypted file.
      password is a four letter lowercase string, representing the password
      used to encrypt/decrypt the file contents.
    Return Value:
      Returns True if the password is correct and the file contents
      were printed.  Returns False and prints nothing otherwise.
    '''
    data = data.split('\n')
    if encode(password) == int(data[0]):
        print(vigenere(data[1],password))
        return True
    return False

def encode(key):
    '''
    Purpose:
      Turn a password into a ~9 digit number
    Input Parameter(s):
      key is a four letter string representing a password
    Return Value:
      Returns a number between 0 and 547120140, using modular exponentiation
      to make it difficult to reverse engineer the password from the number.
    '''
    total = 0
    for ltr in key:
        total += ord(ltr)
        total *= 123
    return pow(total,2011,547120141)

def vigenere(msg,key):
    '''
    Purpose:
      Decipher a message using the Vigenere cipher
    Input Parameter(s):
      msg a string, representing the encrypted message
      key is a four letter string, representing the cipher key
    Return Value:
      Returns a string representing the deciphered text
    '''
    i = 0
    out_msg = ''
    for ltr in msg:
        out_msg += chr((ord(ltr)-ord(key[i]))%28 +97)
        i = (i+1)%len(key)
    return out_msg.replace('{',' ').replace('|','.')
