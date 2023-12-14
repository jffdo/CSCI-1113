def compute_tax(married, taxable_income):
    '''
    Purpose:
        To return the amount of taxes a user owes depending on if they are
        married and given taxable income
    Input Parameter(s):
        married = a boolean anwering if they are married or not with True or
        False
        taxable_income = the taxable income given
    Return Value:
        the amount of taxes the user owes rounded to 2 decimal places
    '''
    if married == False:
        if 0 <= taxable_income < 40000:
            tax = taxable_income * .10
        elif 40000 <= taxable_income < 160000:
            tax = 4000 + ((taxable_income - 40000) * .20)
        elif 160000 <= taxable_income:
            tax = 28000 + ((taxable_income - 160000) * .30)
    else:
        if 0 <= taxable_income < 80000:
            tax = taxable_income * .10
        elif 80000 <= taxable_income < 320000:
            tax = 8000 + ((taxable_income - 80000) * .20)
        elif 320000 <= taxable_income:
            tax = 56000 + ((taxable_income - 320000) * .30)
    return round(tax,2)

def choice(text, optionA, optionB, optionC):
    '''
    Purpose:
        Takes 4 strings of text representing the prompt and choices and returns
        the user's choice as a character.
    Input Parameter(s):
        text = the prompt
        optionA = first option
        optionB = second option
        optionC = third option
    Return Value:
        the chracter of the user's choice
    '''
    print(text)
    print("A.", optionA)
    print("B.", optionB)
    print("C.", optionC)
    userChoice = input("Choose A, B, or C: ")
    if (userChoice == "A") or (userChoice == "B") or (userChoice == "C"):
        return userChoice
    else:
        print("Invalid option, defaulting to A")
        return "A"

def adventure():
    '''
    Purpose:
        A text adventure game
    Input Parameter(s):
        none
    Return Value:
        a boolean value representing True for a good ending and False for bad
    '''
    def start():
        '''
        Purpose:
            Starts the text adventure game
        Input Parameter(s):
            none
        Return Value:
            a boolean value representing True for a good ending and False for bad
        '''
        prompt = choice("You are in an empty room. You see 2 doors.",
                        "Go to the left door","Wait","Go to the right door")
        if prompt == "A":
            return stateTwo()
        elif prompt == "B":
            print("The doors slowly dissapear in front of you "
                "and notice that you are forever trapped in this empty room.")
            return False
        else:
            return stateThree()
    def stateTwo():
        '''
        Purpose:
            Continues the text adventure game, by representing one of the
            places the user chose to go.
        Input Parameter(s):
            none
        Return Value:
            a boolean value representing True for a good ending and False for bad
        '''
        prompt = choice("You are in another room. There is an exit sign. "
                        "You see 2 doors.","Go to the left door","Go Back",
                        "Go to the right door")
        if prompt == "A":
            print("You exit the room.")
            return True
        elif prompt == "B":
            return stateFour()
        else:
            return stateThree()
    def stateThree():
        '''
        Purpose:
            Continues the text adventure game, by representing one of the
            places the user chose to go.
        Input Parameter(s):
            none
        Return Value:
            a boolean value representing True for a good ending and False for bad
        '''
        prompt = choice("You are in another room. There is an exit sign. "
                        "You see 2 doors.","Exit the left door","Go back",
                        "Exit the right door")
        if prompt == "A":
            print("You are in another room. You see no doors. "
                "The door closes behind you and slowly dissapears.")
            return False
        elif prompt == "B":
            return stateFour()
        else:
            print("You exit the room")
            return True
    def stateFour():
        '''
        Purpose:
            Continues the text adventure game, by representing one of the
            places the user chose to go.
        Input Parameter(s):
            none
        Return Value:
            a boolean value representing True for a good ending and False for bad
        '''
        prompt = choice("You go back. Nothing seems to have changed. "
                        "An exit sign appears.","Exit the left door.",
                        "Go Back","Exit the right door")
        if prompt == "A":
            print("You exit the room")
            return True
        elif prompt == "B":
            print("You lost your sense of direction. "
                "Miraculously, you found an exit. ")
            return True
        else:
            print("You lost your sense of direction. "
                "You have been wandering around in circles.")
            return False
    ending = start()
    return ending
