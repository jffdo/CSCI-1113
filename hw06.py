
def rps_game(rounds):
    '''
    Purpose: Plays multiple rounds of Rock-Paper-Scissors
    Input Parameter(s):
        rounds - an integer representing the number of rounds to play
    Return Value: A dictionary representing the computer's win
        differential for each of the three possible choices
    '''
    diff = {"R":0, "S":0, "P":0}
    for i in range(rounds):
        comChoice = rpsComputer(diff)
        plyrChoice = rpsPlayer()
        print("Player Selects", plyrChoice)
        print("Computer Selects", comChoice)
        if plyrChoice == comChoice:
            print("Tie!")
        elif plyrChoice == "R":
            if comChoice == "P":
                print("Computer wins!")
                diff[comChoice] += 1
            elif comChoice == "S":
                print("Player wins!")
                diff[comChoice] -= 1
        elif plyrChoice == "P":
            if comChoice == "S":
                print("Computer wins!")
                diff[comChoice] += 1
            elif comChoice == "R":
                print("Player wins!")
                diff[comChoice] -= 1
        elif plyrChoice == "S":
            if comChoice == "R":
                print("Computer wins!")
                diff[comChoice] += 1
            elif comChoice == "P":
                print("Player wins!")
                diff[comChoice] -= 1
    return diff

def rpsPlayer():
    '''
    Purpose:
        Prompts the user to choose 'R', 'P', or 'S'
    Input Parameter(s): None
    Return Value:
        a string representing the user's choice
    '''
    choice = ""
    while choice not in ("R","P","S"):
        choice = input("Enter R, P, or S: ")
        if choice == "R":
            return choice
        elif choice == "P":
            return choice
        elif choice == "S":
            return choice
        else:
            print("Invalid input, try again.")

def rpsComputer(winDiff):
    '''
    Purpose:
        Returns "R", "P" or "S", depending on the value of the dictionary given
    Input Parameter(s):
        winDiff = the dictionary consisting of the win differential
    Return Value:
        A string consisting of "R", "P", or "S"
    '''
    r = winDiff["R"]
    p = winDiff["P"]
    s = winDiff["S"]
    if (r >= s) and (r >= p):
        return "R"
    elif (s > r) and (s >= p):
        return "S"
    elif (p > r) and (p > s):
        return "P"


def print_104():
    '''
    Purpose: Prints "Who needs loops?" 104 times
    Input Parameter(s): None
    Return Value: None
    '''
    prompt2()
    prompt2()
    prompt2()
    prompt2()
def prompt():
    '''
    Purpose: Prints "Who needs loops?" 5 times
    Input Parameter(s): None
    Return Value: None
    '''
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
def prompt2():
    '''
    Purpose: Prints "Who needs loops?" 26 times
    Input Parameter(s): None
    Return Value: None
    '''
    prompt()
    prompt()
    prompt()
    prompt()
    prompt()
    print("Who needs loops?")

if __name__ == '__main__':

    #TODO: Write test cases for your Problem A Helper functions here
    #Make sure you include Expected Return and Input Sequence (if applicable)

    #Input sequence: R
    #Expected Return: 'R'
    #print(rpsPlayer())

    #Input sequence: r, p, s, P
    #Expected Return: 'P'
    #print(rpsPlayer())

    #Input sequence: None
    #Expected Return: 'R'
    #print(rpsComputer({"R":0, "P":0, "S":0}))

    #Input sequence: None
    #Expected Return: 'P'
    #print(rpsComputer({"R":2, "P":3, "S":2}))

    #Input sequence: None
    #Expected Return: 'S'
    #print(rpsComputer({"R":1, "P":2, "S":2}))

    #Input sequence: S
    #Expected Return: {'R': 1, 'S': 0, 'P': 0}
    #print(rps_game(1))

    #Input sequence: Scissors, P, r, 4, P, P
    #Expected Return: {'R': -1, 'S': 2, 'P': 0}
    #print(rps_game(3))

    #Input sequence: R, P, P, R, R, S, P, P, P, S
    #Expected Return: {'R': -2, 'S': 1, 'P': -1}
    #print(rps_game(10))

    #No return value, but should print "Who needs loops" 104 times
    print_104()
